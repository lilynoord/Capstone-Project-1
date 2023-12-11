from flask import Flask, render_template, redirect, request
from models import db, connect_db, User, Game


app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///sequence_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "ihaveasecret"

connect_db(app)
# Global variables to hold various paths and templates so that I can change them easily later on
homepage = "/gameboard"
homepageTemplate = "gameboard"
board = [
    [
        ["XX", "clear"],
        ["0S", "clear"],
        ["QS", "clear"],
        ["KS", "clear"],
        ["AS", "clear"],
        ["2D", "clear"],
        ["3D", "clear"],
        ["4D", "clear"],
        ["5D", "clear"],
        ["XX", "clear"],
    ],
    [
        ["9S", "clear"],
        ["0H", "clear"],
        ["9H", "clear"],
        ["8H", "clear"],
        ["7H", "clear"],
        ["6H", "clear"],
        ["5H", "clear"],
        ["4H", "clear"],
        ["3H", "clear"],
        ["6D", "clear"],
    ],
    [
        ["8S", "clear"],
        ["QH", "clear"],
        ["7D", "clear"],
        ["8D", "clear"],
        ["9D", "clear"],
        ["0D", "clear"],
        ["QD", "clear"],
        ["KD", "clear"],
        ["2H", "clear"],
        ["7D", "clear"],
    ],
    [
        ["7S", "clear"],
        ["KH", "clear"],
        ["6D", "clear"],
        ["2C", "clear"],
        ["AH", "clear"],
        ["KH", "clear"],
        ["QH", "clear"],
        ["AD", "clear"],
        ["2S", "clear"],
        ["8D", "clear"],
    ],
    [
        ["6S", "clear"],
        ["AH", "clear"],
        ["5D", "clear"],
        ["3C", "clear"],
        ["4H", "clear"],
        ["3H", "clear"],
        ["0H", "clear"],
        ["AC", "clear"],
        ["3S", "clear"],
        ["9D", "clear"],
    ],
    [
        ["5S", "clear"],
        ["2C", "clear"],
        ["4D", "clear"],
        ["4C", "clear"],
        ["5H", "clear"],
        ["2H", "clear"],
        ["9H", "clear"],
        ["KC", "clear"],
        ["4S", "clear"],
        ["0D", "clear"],
    ],
    [
        ["4S", "clear"],
        ["3C", "clear"],
        ["3D", "clear"],
        ["5C", "clear"],
        ["6H", "clear"],
        ["7H", "clear"],
        ["8H", "clear"],
        ["QC", "clear"],
        ["5S", "clear"],
        ["QD", "clear"],
    ],
    [
        ["3S", "clear"],
        ["4C", "clear"],
        ["2D", "clear"],
        ["6C", "clear"],
        ["7C", "clear"],
        ["9C", "clear"],
        ["9C", "clear"],
        ["0C", "clear"],
        ["6S", "clear"],
        ["KD", "clear"],
    ],
    [
        ["2S", "clear"],
        ["5C", "clear"],
        ["AS", "clear"],
        ["KS", "clear"],
        ["QS", "clear"],
        ["0S", "clear"],
        ["9S", "clear"],
        ["8S", "clear"],
        ["7S", "clear"],
        ["AD", "clear"],
    ],
    [
        ["XX", "clear"],
        ["6C", "clear"],
        ["7C", "clear"],
        ["8C", "clear"],
        ["9C", "clear"],
        ["0C", "clear"],
        ["QC", "clear"],
        ["KC", "clear"],
        ["AC", "clear"],
        ["XX", "clear"],
    ],
]

# Useful Globals
currentUser = None


def getUsername():
    if currentUser != None:
        return currentUser.username
    else:
        return "login/"


# app routes
@app.route("/")
def redirect_to_home():
    return redirect("/home")


@app.route("/home")
def route_to_home():
    return render_template("home.html", username=getUsername())


@app.route("/gameboard")
def route_to_gameboard():
    return render_template(
        "gameboard.html",
        username=getUsername(),
        board=board,
        rownum=0,
        colnum=0,
        isdisabled="true",
        gameID=1,
    )


@app.route("/login")
def route_to_login():
    return render_template("login.html", username=getUsername())


@app.route("/login/submit", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]
    submitType = request.form["submitType"]

    if submitType == "login":
        currentUser = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one()
        return redirect("/home")
    elif submitType == "signup":
        newUser = User(username=username, password=password)
        db.session.add(newUser)
        db.session.commit()
        currentUser = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one()
        return redirect("/home")
