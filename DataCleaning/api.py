import json
from database_accessor import Database_Accessor
from flask import Flask, request, jsonify
from mwrogue.esports_client import EsportsClient
import urllib.request
from flask_cors import CORS
from flask import send_file


app = Flask(__name__)
CORS(app) 

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
    db = db_accessors.getDataFromTable(tableName="tournaments", 
                                   columns=["tournament"], 
                                   where_clause=f"id={id}")
    print(db)
    return jsonify(db)

if __name__ == '__main__':
     app.run(debug=True)

