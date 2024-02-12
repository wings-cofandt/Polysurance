from DBHandler import MongoDBSingleton
from constants import COLLECTION_FLEET_SUMMARY


data = [
    {
        "start_date": "2024-02-01",
        "end_date": "2024-02-07",
        "total_engine_time_on": 120,  
        "total_driving_duration": 90,
        "total_idling_duration": 30,
        "total_distance_driven": 800,
    },
    {
        "start_date": "2024-02-08",
        "end_date": "2024-02-14",
        "total_engine_time_on": 130,
        "total_driving_duration": 95,
        "total_idling_duration": 35,
        "total_distance_driven": 850,
    },
    
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_FLEET_SUMMARY,data)

for record in db.fetchall(COLLECTION_FLEET_SUMMARY):
    
    print(record)

