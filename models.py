"""SQLAlchemy models for project"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    ! This is not meant to hold any sensitive user info, it's just a way for users to store their win/loss history, if they want to. 
    """

    __tablename__ = "user"

    uuid = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    username = db.Column(db.Text,nullable=False)
    passwordUnsecure = db.Column(db.Text,nullable=False) 
    winCount = db.Column(db.Integer)
    lossCount = db.Column(db.Integer)

    @property
    def calculateWinLossRatio(self):
        winLossRatio = float(self.winCount / self.lossCount)
        return winLossRatio


class Game(db.Model):
    __tablename__ = "game"

    uuid = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    player = db.relationship("user")
   
    #Red tokens
    #Blue Tokens
    #Red Hand
    #Blue Hand
    #Deck ID
    
def connect_db(app):
    db.app = app
    db.init_app(app)
