from DBHandler import MongoDBSingleton
from constants import COLLECTION_GEOFENCE_REPORTS


data ={
        "vehicle_id": "V001",
        "geofence_id": "G001",
        "entry_timestamp": "2024-02-04T12:30:00",
        "exit_timestamp": "2024-02-04T13:30:00",
        "duration": 1.0,
        "violation_status": False,
    }

# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert a record
db.insert(COLLECTION_GEOFENCE_REPORTS,data)


for record in db.fetchall(COLLECTION_GEOFENCE_REPORTS):
    print(record)