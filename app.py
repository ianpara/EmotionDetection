# imports
# Python standard libraries
import json
import os
import sqlite3
from datetime import timedelta

#from db_connect import Database #mysql local db

# Third-party libraries
from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)


from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from database.db import init_db_command
from database.user import User
from database.models import Database
from audio.test import predict_mood
from audio.test import test_predict_mood

# Google Login Configuration
# FUTURE FIX - make variables env variables and not shown here
# GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_ID = '945666069099-6bgc35j8iqjrej43svhts9u87a8g0cdi.apps.googleusercontent.com'
# GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_CLIENT_SECRET = 'DDwwaYEca2jAv5c0EBRsp3hI'
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# create the application object
app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass


client = WebApplicationClient(GOOGLE_CLIENT_ID)


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    print(User.get(user_id))
    return User.get(user_id)


# either login page or home page depending if user is logged in
@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html', title="Home")  # render a template
    else:
        return render_template('login.html', title="Login")  # render a template


# function for retrieving Google’s provider configuration:
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


# route for handling the login page logic
@app.route('/login')
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    # Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)
        new_user = True
        return new_user

    # Begin user session by logging the user in
    login_user(user, remember=True, duration=timedelta(days=30))

    # Send user back to homepage
    return redirect(url_for("home"))

# logout function
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

# record page
@app.route('/record')
@login_required
def record():
    return render_template('record.html', title="Record Mood")


# background process happening without any refreshing
@app.route('/result', methods=['GET', 'POST'])
@login_required
def start_record():
    # result = test_predict_mood()
    result = predict_mood()
    output = Database.feelBetter(result)
    return render_template('result.html', title="Result", output=output, result=result)



# log page
@app.route('/logs', methods=['GET', 'POST'])
@login_required
def logs():
    table=[] # save table as empty tuple
    if request.method == 'POST':
        return render_template('logs.html', title="Logs")
    else:
        table = Database.retrieveMoods() # puts moods inside table tuple
        return render_template('logs.html', title="Logs", table=table)

# account page
@app.route('/account')
@login_required
def account():
    return render_template('account.html', title="My Account")

# background process happening without any refreshing
@app.route('/delete_account')
@login_required
def delete_account():
    Database.remove_user()
    print ("User deleted")
    return redirect(url_for("home"))


# error pages
@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 405


@app.errorhandler(401)
def page_not_found(e):
    return render_template('401.html'), 401


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug="true", ssl_context='adhoc')
