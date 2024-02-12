from DBHandler import MongoDBSingleton
from constants import COLLECTION_UTILIZATION


data = [
    {
        "vehicle_id": "V001",
        "usage_statistics": {"total_distance_driven": 500, "engine_time_on": 60, "idling_duration": 20},
        "resource_utilization": "Optimal",
        "asset_lifecycle_analysis": "Within expected lifespan",
    },
    {
        "vehicle_id": "V002",
        "usage_statistics": {"total_distance_driven": 600, "engine_time_on": 70, "idling_duration": 25},
        "resource_utilization": "Suboptimal",
        "asset_lifecycle_analysis": "Maintenance required",
    },
    
]



# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_UTILIZATION,data)

for record in db.fetchall(COLLECTION_UTILIZATION):
    
    print(record)

