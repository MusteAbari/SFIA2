from application import app
from flask import request, Response
import random


@app.route("/team", methods=["GET"])
def get_team():
    teams = ["Arsenal", "Chelsea", "Fulham"]
    return Response(str(random.choice(teams)), mimetype='text/plain')





"""
@app.route("/team", methods=["GET"])
def get_team():
    teams = ["Arsenal", "Chelsea", "Fulham", "Liverpool"]
    return Response(str(random.choice(teams)), mimetype='text/plain')

@app.route("/teamposition", methods=["GET"])
def get_teamposition():
    team = request.data2.decode("utf-8")
    position = {"Chelsea" : 1,
        "Arsenal" : 2,
        "Fulham" : 3}
    return jsonify(position[team], mimetype='text/plain')
"""