# Web_App/Twitoff/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print('vsited the home page')
    return render_template("prepare_to_predict.html")

@home_routes.route("/hello")
def hello():
    print('vsited the hello page')
    return "Hello World!"

@home_routes.route("/about")
def about():
    print('visited the about page')
    return "About me."