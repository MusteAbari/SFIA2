from application import app, db
from application.models import Players, Teams
import requests
from requests import get

@app.route('/', methods=['GET'])
def index():
    player_response = requests.get("http://football_player_backend:5000/player")
    team_response = requests.get("http://football-team_backend:5000/team")
    result_response = requests.post(
        "http://football_outcome:5000/result", 
        json=dict(player=player_response.text, team=team_response.text))
    
    new_player = Players(name = player_response.text)
    new_team = Teams(name = team_response.text)
    db.session.add(new_player)
    db.session.add(new_team)
    db.session.commit()

    view_players = Players.query.all()
    view_teams = Teams.query.query()

    return render_template(
        "index.html", 
        player=player_response.text, team=team_response.text, goal=result_response.text, 
        view_players=view_players, view_teams=view_teams)
