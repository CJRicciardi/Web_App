# app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('vsited the hello page')
    return "Hello World!"

@app.route("/about")
def about():
    print('visited the about page')
    return "About me"
