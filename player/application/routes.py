from application import app
from flask import request, Response
import random

@app.route("/player", methods=["GET"])
def get_player():
    players = ["Rooney", "Beckham", "Cole"]
    return Response(str(random.choice(players)), mimetype='text/plain')








"""
@app.route("/player", methods=["GET"])
def get_player():
    players = ["Rooney", "Beckham", "Cole", "Defoe"]
    return Response(str(random.choice(players)), mimetype='text/plain')

@app.route("/player", methods=["GET"])
def get_playergoal():
    players = request.data.decode("utf-8")
    goals = {"Rooney" : 10,
        "Beckham" : 6,
        "Cole" : 4}
    return jsonify(goals[players], mimetype='text/plain')
"""