
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'DataCleaning'))
from database_accessor import Database_Accessor
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Models'))
from ranking_model_interface import Ranking_Model
from mock_ranking_model import Mock_Ranking_Model

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

db_accessors = Database_Accessor(
    db_name="games",
    db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
    db_user="data_cleaner",
)

@app.route('/api/generate_tournament_data/<id>', methods=['GET'])
def generateTournamentData(id):
    tournament_data = db_accessors.getDataFromTable(tableName="tournaments", 
                                   columns=["tournament"], 
                                   where_clause=f"id={id}")
    tournament = json.loads(tournament_data[0][0])
    return jsonify(tournament)

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

