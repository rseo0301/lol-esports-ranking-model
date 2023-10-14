
from enum import Enum
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from Models.ranking_model_interface import Ranking_Model
from Models.mock_ranking_model import Mock_Ranking_Model
from DataCleaning.database_accessor import Database_Accessor

import json
from flask import Flask, request, jsonify
from mwrogue.esports_client import EsportsClient
import urllib.request
from flask_cors import CORS
from flask import send_file


app = Flask(__name__)
CORS(app) 

# Get icons from Leaguepedia API
def get_filename_url_to_open(site: EsportsClient, filename, team, width=None):
    response = site.client.api(
        action="query",
        format="json",
        titles=f"File:{filename}",
        prop="imageinfo",
        iiprop="url",
        iiurlwidth=width,
    )

    print(response)
    image_info = next(iter(response["query"]["pages"].values()))["imageinfo"][0]

    if width:
        url = image_info["thumburl"]
    else:
        url = image_info["url"]
        
    urllib.request.urlretrieve(url, f"icons/{team}.png")
    return url +".jpg"

# Get icon for team
@app.route('/api/icon/<team>', methods=['GET'])
def get_icon(team):
    site = EsportsClient("lol")
    response = site.cargo_client.query(
        tables="Teams=T",
        fields="T.Name, T.Short",
        where=f"(T.Short = '{team}' OR T.Name = '{team}') AND T.IsDisbanded = false",
    )
    team_name = response[0]["Name"]
    url = f"{team_name}logo square.png"
    try:
        get_filename_url_to_open(site, url, team)
        return send_file(f"icons/{team}.png", mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)})

# Database accessor
def initialize_db_accessors():
    return Database_Accessor(
        db_name="games",
        db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
        db_user="data_cleaner",
    )

# Fetching leagues data from db
def fetch_leagues_data(db_accessors, leagues_id):
    league_data = db_accessors.getDataFromTable(
        tableName="leagues",
        columns=["league"],
         where_clause=f"id={leagues_id}"
    )
    return json.loads(league_data[0][0])

# Fetching tournament data from db
def fetch_tournament_data(db_accessors, tournament_id):
    tournament_data = db_accessors.getDataFromTable(
        tableName="tournaments",
        columns=["tournament"],
        where_clause=f"id={tournament_id}"
    )
    return json.loads(tournament_data[0][0])

# Fetching team data from db
def fetch_team_data(db_accessors, team_id):
    team_data = db_accessors.getDataFromTable(
        tableName="teams",
        columns=["team"],
        where_clause=f"id={team_id}"
    )
    return json.loads(team_data[0][0])


# Get rankings using tournaments json
def get_rankings_data(tournament_json):
    return tournament_json["stages"][0]["sections"][0]["rankings"]

@app.route('/tournamentStandings/<int:tournament_id>', methods=['GET'])
def generate_tournaments_standings(tournament_id):
    db_accessors = initialize_db_accessors()
    tournament_json = fetch_tournament_data(db_accessors, tournament_id)
    rankings = tournament_json["stages"][0]["sections"][0]["rankings"]
    newData = []
    updatedRankings = []
    for team in rankings:
        updated_ranking = {
            "ranking": team["ordinal"],
            "team_info": fetch_team_data(db_accessors, team["teams"][0]["id"]),
            "record": team["teams"][0]["record"]
        }
        updatedRankings.append(updated_ranking)
    newData.append({"tournamentName": tournament_json["slug"],"tournamentStandings": updatedRankings})
    

    return jsonify(newData)

@app.route("/leagueTeams/<int:leagues_id>", methods=["GET"])
def generate_league_teams(leagues_id):
    db_accessors = initialize_db_accessors()
    league_json = fetch_leagues_data(db_accessors,leagues_id)
    # getting the most recent tournament id
    recent_tournament_id = league_json["tournaments"][0]["id"]
    tournament_json = fetch_tournament_data(db_accessors, recent_tournament_id)
    rankings = get_rankings_data(tournament_json)
    teamList=[]
    for team in rankings:
        updatedTeamObject = {
            "id": team["teams"][0]["id"],
            "team_info":fetch_team_data(db_accessors, team["teams"][0]["id"])
        }
        teamList.append(updatedTeamObject)
    return jsonify(teamList)

# This is for the folders
@app.route("/leagues", methods=["GET"])
def generate_leagues():
    db_accessors = initialize_db_accessors()
    leagues_data = db_accessors.getDataFromTable(
        tableName="leagues",
        columns=["league"])
    leagueArr=[]
    for league in leagues_data:
        league_object = json.loads(league[0])
        updatedData={
            "name":league_object["name"],
            "leagues_id": league_object ["id"],
            "image": league_object["image"],
            "priority":league_object["priority"],
            "region": league_object["region"]
        }
        leagueArr.append(updatedData)
    sorted_leagueArr = sorted(leagueArr, key=lambda x: x["priority"])
    return jsonify(sorted_leagueArr)

"""
    ML mock endpoints
"""
machineLearningModel=["Bayesian Model","Logistic Regression", "Random Forest"]

@app.route("/model/tournamentsStandings/<tournament_id>")
def generate_tournament_standings_by_model(tournament_id):
     model_id = request.args.get("model_id")
     model_type = machineLearningModel[int(model_id)]
     model: Ranking_Model = None
     if model_type == "Bayesian Model":
         model = Mock_Ranking_Model()
         bayesian_model = model.get_tournament_rankings(tournament_id,"test")
         return jsonify({"model":model_type,"data":bayesian_model})
     if model_type == "Logistic Regression":
         model = Mock_Ranking_Model()
         logistic_regression_model_data = model.get_tournament_rankings(tournament_id,"test")
         return jsonify({"model":model_type,"data":logistic_regression_model_data})
     if model_type == "Random Forest":
         model = Mock_Ranking_Model()
         random_forest_model_data = model.get_tournament_rankings(tournament_id,"test")
         return jsonify({"model":model_type,"data":random_forest_model_data})

# pseudo-code on how to use mock model. CODE HAS SYNTAX ERRORS
"""
    model: Ranking_Model = None
    if (model_id = "logistic_regression"):
        model = Mock_Ranking_Model()
    model: Ranking_Model = Mock_Ranking_Model
    model.get_custom_rankings({})
"""

    

if __name__ == '__main__':
     app.run(debug=True)

