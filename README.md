# GLADiator - Emotion Detection
Psychiatric disorders are present in nearly all suicide victims. Depression is normally the root of suicidal thoughts. While there are anti-depressant drugs and psychiatric treatments available for these patients, these options can be expensive and hard to get. Thats where out app Gladiator comes in. There are few forms of devices available that can detect depression episode in these patients. Such episodes can be detected and characterized by monitoring vocal tone. Since such episodes can occur at any time, an immediate psychiatric treatment may not be available. A simpler form of treatment could be to have a conversation with someone, however if no one is nearby that could be difficult. With Gladiator you can talk to us and we can make your day better with a cheerful joke or a motivational quote depending on how you are feeling. While this solution is not medically studied to help someone with depression we believe it is good stepping stone in talking about your feelings and even help alleviate any emotional distress you may have.

### Live Demo
Gladiator is hosted on a Google VM and it costs money to run it! So the web server may or may no be running. (The main feature i.e. voice recording does not work on the web server. Obiously not ideal and in the process of solving the issue.) www.glad-iator.com 

## Getting Started
If you'd like to run this project on your system here's how.

### Prerequisites
* Windows OS only (at the moment)
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* PyCharm

### Installation
* Download this repository as a zip.
* Unpack and open the downloaded folder as a new project in PyCharm.
* In PyCharm go to File > Settings > Project:EmotionDetection-master > Project Interpreter,  then click the gear icon and then add.
* Keep everything default but for the base interpreter. Select the path where python.exe was saved for Pyhon 3.6 (ex. C:\Users\Username\AppData\Local\Programs\Python\Python36-32\python.exe) 
* In the terminal in PyCharm you should see (venv) or (vurtual). If you don't, navigate to your virtual (or venv) folder in the project explorer. Expand Scripts folder, then find “activate” (NOT activate.bat) and right click then copy path. Paste that into the terminal and hit enter. You should now see (virtual) or (venv).
* In the terminal:
```
pip install -r requirements.txt
```
* Right click on app.py in the Project Explorer and click Run 'app'.

## Acknowledgments
BIG thanks to the people who wrote these tutorials
* https://realpython.com/flask-google-login/
* https://www.thepythoncode.com/article/building-a-speech-emotion-recognizer-using-sklearn
* Certificate: https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx
