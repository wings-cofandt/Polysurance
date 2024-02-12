from DBHandler import MongoDBSingleton
from constants import COLLECTION_DISTANCE_TRAVELED


data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T12:30:00",
        "total_distance": 50.0,
        "state": "NY",
        "geofence_id": "G001",
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T14:45:00",
        "total_distance": 75.0,
        "state": "CA",
        "geofence_id": "G002",
    },
    
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_DISTANCE_TRAVELED,data)


for record in db.fetchall(COLLECTION_DISTANCE_TRAVELED):
    print(record)