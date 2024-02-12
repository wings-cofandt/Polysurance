from DBHandler import MongoDBSingleton
from constants import COLLECTION_VEHICAL

data = {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T12:30:00",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "activity": "start",
    }


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert a record
db.insert(COLLECTION_VEHICAL,data)


for record in db.fetchall(COLLECTION_VEHICAL):
    print(record)