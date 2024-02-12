from DBHandler import MongoDBSingleton
from constants import COLLECTION_EXCEPTION


data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T15:00:00",
        "exception_type": "Unauthorized use",
        "location": "Outside working hours",
        "remedial_actions_taken": "Driver warned, additional training provided",
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T18:30:00",
        "exception_type": "Long unauthorized stop",
        "location": "Geofence G002",
        "remedial_actions_taken": "Driver counseling session, geofence adjusted",
    },
    
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_EXCEPTION,data)

for record in db.fetchall(COLLECTION_EXCEPTION):
    
    print(record)

