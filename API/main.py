
import argparse
from enum import Enum
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, ".."))

from flask.json import dump

from Models.ranking_model_interface import Ranking_Model
from Models.mock_ranking_model import Mock_Ranking_Model
from dao.database_accessor import Database_Accessor

import json
from flask import Flask, request, jsonify
from mwrogue.esports_client import EsportsClient
import urllib.request
from flask_cors import CORS
from flask import send_file


app = Flask(__name__)
CORS(app) 

__dao: Database_Accessor = None

# Database accessor
def get_dao():
    global __dao
    if not __dao:
        __dao = Database_Accessor(
            db_name="games",
            db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
            db_user="data_cleaner",
            )
    return __dao

# Will return the appropriate model, given the model anem
def get_model(model_name: str):
    if not model_name:
        return Mock_Ranking_Model()
    match model_name.lower():
        case "bayesian":
            return Mock_Ranking_Model()
        case "logisticregression":
            return Mock_Ranking_Model()
        case "randomforest":
            return Mock_Ranking_Model()
        case _:
            return Mock_Ranking_Model()


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
    db_accessors = get_dao()
    tournament_json = fetch_tournament_data(db_accessors, tournament_id)
    rankings = tournament_json["stages"][0]["sections"][0]["rankings"]
    tournament_name_type = tournament_json["stages"][0]["name"]
    newData = []
    updatedRankings = []
   
    for team in rankings:
            team_info = {}
            try:
                team_info = fetch_team_data(db_accessors, team["teams"][0]["id"])
            except:
                team_info= {}
                print("error",team)
        
            updated_ranking = {
                "ranking": team["ordinal"],
                "team_info": team_info,
                "record": team["teams"][0]["record"]
            }
            updatedRankings.append(updated_ranking)
    newData.append({"tournamentName": tournament_json["slug"],"tournamentStandings": updatedRankings})
    return jsonify(newData)


@app.route("/leagueTeams/<int:leagues_id>", methods=["GET"])
def generate_league_teams(leagues_id):
    db_accessors = get_dao()
    league_json = fetch_leagues_data(db_accessors,leagues_id)
   
    index = 0
    while True:
        try:
            recent_tournament_id = league_json["tournaments"][index]["id"]
            tournament_json = fetch_tournament_data(db_accessors, recent_tournament_id)
            rankings = tournament_json["stages"][0]["sections"][0]["rankings"]
            if rankings:
                break  
        
            
        except:
            print("dont exist")
        index += 1
    teamList=[]
    for team in rankings:
        team_info = {}
        try:
            team_info = fetch_team_data(db_accessors, team["teams"][0]["id"])
        except:
            team_info= {}
            print("error",team)
        updatedTeamObject = {
                "id": team["teams"][0]["id"],
                "team_info":team_info
            }
        teamList.append(updatedTeamObject)
   
        
    return jsonify(teamList)


# This is for the folders
@app.route("/leagues", methods=["GET"])
def generate_leagues():
    db_accessors = get_dao()
    leagues_data = db_accessors.getDataFromTable(
        tableName="leagues",
        columns=["league"])
    leagueArr=[]
    for league in leagues_data:
        league_object = json.loads(league[0])
        if(league_object["name"]!="TFT Rising Legends"):
         updatedData={
            "name":league_object["name"],
            "leagues_id": league_object ["id"],
            "image": league_object["image"],
            "priority":league_object["priority"],
            "region": league_object["region"],
            # "tournaments":league_object["tournaments"]
        }
        leagueArr.append(updatedData)
        
    sorted_leagueArr = sorted(leagueArr, key=lambda x: x["priority"])
    return jsonify(sorted_leagueArr)


@app.route("/leagueTournaments/<league_id>", methods=["GET"])
def generate_league_tournaments(league_id: str):
    dao = get_dao()
    league_data = dao.getDataFromTable(tableName="leagues", columns=["league"], where_clause=f"id={league_id}")
    league_tournaments = json.loads(league_data[0][0])['tournaments']
    tournament_ids = [t['id'] for t in league_tournaments]
    where_filter = [f"id='{id}'" for id in tournament_ids]
    tournaments_data = dao.getDataFromTable(tableName="tournaments", columns=['tournament'], where_clause=" OR ".join(where_filter))
    ret = []
   
    for tournament_data in tournaments_data:
        tournament = json.loads(tournament_data[0])
        if(tournament["stages"][0]["sections"][0]["rankings"] != [ ]):
            ret.append({
                        "id": tournament['id'],
                        "name": tournament['name'],
                        'startDate': tournament['startDate']
                    })
            ret = sorted(ret, key=lambda x: x["startDate"], reverse=True)
    return {
        'tournaments': ret
    }


@app.route("/model/tournamentsStandings/<tournament_id>")
@app.route("/tournament_rankings/<tournament_id>")
def generate_tournament_standings_by_model(tournament_id):
     model_name = request.args.get("model")
     stage = request.args.get("stage")
     if not stage:
         return "Please provide a tournament 'stage' as a query parameter", 400
     model = get_model(model_name=model_name)
     return model.get_tournament_rankings(tournament_id=tournament_id, stage=stage)


@app.route("/model/globalRankings", methods=["GET"])
@app.route("/globalRankings", methods=["GET"])
def generate_model_global_rankings():
    model_name = request.args.get('model')
    n_teams = request.args.get('n_teams')
    model = get_model(model_name=model_name)
    return model.get_global_rankings(n_teams=int(n_teams))


@app.route("/model/customRankings", methods=["GET"])
@app.route("/team_rankings", methods=["GET"])
def generate_custom_rankings():
    model_name = request.args.get('model')
    team_ids = request.args.get('team_ids')
    if not team_ids:
        return "Expecting 'team_ids' as a list of team ids in query", 400
    try:
        team_ids = json.loads(team_ids)
    except json.JSONDecodeError as e:
        return 'Error parsing "team_ids". Please ensure it is a properly json formatted array (eg. ["team1_id", "team2_id", ...]', 400
    
    model = get_model(model_name=model_name)
    return model.get_custom_rankings(team_ids=team_ids)


# Health check endpoint for aws ECS service
@app.route("/healthCheck", methods=["GET"])
def health_check():
    return jsonify({"message": "Health check OK"}), 200


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--production', help='Set this flag to run the flask app in production mode', action="store_true", default=False)
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=5001, debug = not args.production)

