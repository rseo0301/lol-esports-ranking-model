import json
from database_accessor import Database_Accessor


db_access = Database_Accessor(
    db_name="games",
    db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
    db_user="data_cleaner",
)


cumulative_stats = db_access.getDataFromTable(tableName="games", columns=["id"], limit=10, offset=0)
print("cum stats", cumulative_stats)
for id, stats in cumulative_stats:
    stats = json.loads(stats)
    print(stats)