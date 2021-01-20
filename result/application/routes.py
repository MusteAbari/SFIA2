from application import app 
from flask import request, Response

@app.route("/result", methods=["GET"])
def result():
    player = request.json["player"]
    team = request.json["team"]

    if player == "Cole" and team == "Chelsea" or team == "Arsenal":
        return Response("Cole won't Score", mimetype='text/plain')
    elif player == "Cole" and team == "Fulham":
        return Response("Cole will Score", mimetype='text/plain')
    elif player == "Beckham" and team == "Arsenal" or team == "Fulham":
        return Response("Beckham will Score", mimetype='text/plain')
    elif player == "Beckham" and team == "Chelsea":
        return Response("Beckham wont score", mimetype='text/plain')
    else:
        return Response("Rooney will score", mimetype='text/plain')