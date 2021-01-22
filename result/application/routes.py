from application import app 
from flask import request, Response

@app.route("/result", methods=["POST"])
def result():
    player = request.json["player"]
    team = request.json["team"]
    
    if player == "Rooney":
        message="Rooney will score"
    elif player == "Beckham":
        if team == "Arsenal" or team == "Fulham":
            message="Beckham will score"
        else:
            message="Beckham will not score"
    elif player == "Cole":
        if team == "Fulham":
            message="Cole will score"
        else:
            message="Cole will not score"       
    return Response(message, mimetype='text/plain')
    