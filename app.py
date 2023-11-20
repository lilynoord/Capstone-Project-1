from flask import Flask, render_template, redirect, request
from models import db, connect_db


app = Flask(__name__)

# Global variables to hold various paths and templates so that I can change them easily later on
homepage = "/gameboard"
homepageTemplate = "gameboard"


@app.route("/")
def route_to_home():
    return redirect("/gameboard")
