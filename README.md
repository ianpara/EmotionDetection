# GLADiator - Emotion Detection
Psychiatric disorders are present in nearly all suicide victims. Depression is normally the root of suicidal thoughts. While there are anti-depressant drugs and psychiatric treatments available for these patients, these options can be expensive and hard to get. Thats where out app Gladiator comes in. There are few forms of devices available that can detect depression episode in these patients. Such episodes can be detected and characterized by monitoring vocal tone. Since such episodes can occur at any time, an immediate psychiatric treatment may not be available. A simpler form of treatment could be to have a conversation with someone, however if no one is nearby that could be difficult. With Gladiator you can talk to us and we can make your day better with a cheerful joke or a motivational quote depending on how you are feeling. While this solution is not medically studied to help someone with depression we believe it is good stepping stone in talking about your feelings and even help alleviate any emotional distress you may have.

### Live Demo
GLADiator is hosted on a Google VM and it costs money to run it! So the web server may or may no be running. (The main feature i.e. voice recording does not work on the web server. Obviously not ideal and in the process of solving the issue.) www.glad-iator.com 

## Getting Started with PyCharm
If you'd like to run this project on your system like we did to develop it follow these instructions. If you'd like to run the project via Windows Command prompt go to **Getting Started with Windows CMD**.

### Prerequisites
* Windows OS only (at the moment)
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* PyCharm

### Installation
* Download this repository as a zip.
* Unpack and open the downloaded folder as a new project in PyCharm.
* In PyCharm go to File > Settings > Project:EmotionDetection-master > Project Interpreter,  then click the gear icon and then add.
* Keep everything default but for the base interpreter. Select the path where python.exe was saved for Pyhon 3.6 (ex. C:\Users\Username\AppData\Local\Programs\Python\Python36-32\python.exe) 
* In the terminal in PyCharm you should see (venv) or (virtual). If you don't, navigate to your virtual (or venv) folder in the project explorer. Expand Scripts folder, then find “activate” (NOT activate.bat) and right click then copy path. Paste that into the terminal and hit enter. You should now see (virtual) or (venv).
* In the terminal:
```
pip install -r requirements.txt
```
* Right click on app.py in the Project Explorer and click Run 'app'.

## Getting Started with Windows CMD

### Prerequisites
* Windows OS
 
### Setup
* Install Python
* Install VirtualEnv
* Install VirtualEnvWrapper-win
* Download Project

### Install Python
Download Python 3.6 from [here](https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe).

Run the installer.

**Make sure to check "Add Python 3.6 to PATH".**

To test Python was installed properly open a command prompt (win+r->’cmd’->Enter) and try `pip help`.
You should see a list of available commands including install, which we’ll use for the next part.
### Install virtualenv
Now that you have Python installed and a command prompt open we need to install virtualenv to our root Python installation by typing `pip install virtualenv`. 

Now we have virtualenv installed which will make it possible to create individual environments to test our code in. But managing all these environments can become cumbersome. So we’ll pip install another helpful package…
### Install virtualenvwrapper-win
Use pip to install virtualenvwrapper-win. `pip install virtualenvwrapper-win.`

### Download the project
[Download](https://github.com/ianpara/EmotionDetection/archive/master.zip) the project anywhere you'd like on your system.
Unzip the downloaded folder. 

### Getting the project to work
* Make a Virtual Environment
* Connect this project to the environment
* Set project directory
* Install and run

### Make a Virtual Environment
In the command prompt navigate to your project `cd path/to/Emotion-Detection-master/`

Lets make a virtual environment called 'virtual'. In the command prompt enter `mkvirtualenv virtual`.  

This will create a folder with python.exe, pip, and setuptools all ready to go in its own little environment. It will also activate the Virtual Environment which is indicated with the (virtual) on the left side of the prompt. If it doesn't activate type `\path\to\virtal\Scripts\activate` to manually activate. 

### Set Project Directory
Now  bind our virtualenv with our current working directory we simply enter `setprojectdir .`  

Now next time we activate this environment we will automatically move into this directory!

### Install requirements and run!
To install everything needed to run the project:

    pip install -r requirements.txt

To run:

    python app.py
In your browser goto https://127.0.0.1:5000/

Thanks to [this](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/) guide for help in writing this tutorial. 

## Acknowledgments
BIG thanks to the people who wrote these tutorials
* https://realpython.com/flask-google-login/
* https://www.thepythoncode.com/article/building-a-speech-emotion-recognizer-using-sklearn
* Certificate: https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx
