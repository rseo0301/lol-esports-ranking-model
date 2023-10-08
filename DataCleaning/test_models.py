import pandas as pd
import json
from database_accessor import Database_Accessor
import sklearn

db_accessor: Database_Accessor = Database_Accessor(db_name = 'games', 
    db_host = 'riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com', 
    db_user = 'data_cleaner')

gameCount: int = 0
cumulative_stats = db_accessor.getDataFromTable(tableName="cumulative_data", columns=["id", "scale_by_90"], limit=10, offset=gameCount)
for id, stats in cumulative_stats:
    stats = json.loads(stats)
    print(stats)