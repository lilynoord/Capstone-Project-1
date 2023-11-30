from flask import Flask, render_template, redirect, request
from models import db, connect_db


app = Flask(__name__)

# Global variables to hold various paths and templates so that I can change them easily later on
homepage = "/gameboard"
homepageTemplate = "gameboard"
board = [
    ["XX", "0S", "QS", "KS", "AS", "2D", "3D", "4D", "5D", "XX"],
    ["9S", "0H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "6D"],
    ["8S", "QH", "7D", "8D", "9D", "0D", "QD", "KD", "2H", "7D"],
    ["7S", "KH", "6D", "2C", "AH", "KH", "QH", "AD", "2S", "8D"],
    ["6S", "AH", "5D", "3C", "4H", "3H", "0H", "AC", "3S", "9D"],
    ["5S", "2C", "4D", "4C", "5H", "2H", "9H", "KC", "4S", "0D"],
    ["4S", "3C", "3D", "5C", "6H", "7H", "8H", "QC", "5S", "QD"],
    ["3S", "4C", "2D", "6C", "7C", "9C", "9C", "0C", "6S", "KD"],
    ["2S", "5C", "AS", "KS", "QS", "0S", "9S", "8S", "7S", "AD"],
    ["XX", "6C", "7C", "8C", "9C", "0C", "QC", "KC", "AC", "XX"],
]


@app.route("/")
def route_to_home():
    return redirect("/gameboard")


@app.route("/gameboard")
def rout_to_gameboard():
    return render_template("gameboard.html", board=board, rownum=0, colnum=0)
