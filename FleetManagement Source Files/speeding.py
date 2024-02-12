from DBHandler import MongoDBSingleton
from constants import COLLECTION_SPEEDING


data = [
    {
        "driver_id": "D001",
        "timestamp": "2024-02-04T14:00:00",
        "duration": 0.5,
        "severity": "Moderate",
        "location": "Highway A",
    },
    {
        "driver_id": "D002",
        "timestamp": "2024-02-04T16:30:00",
        "duration": 0.75,
        "severity": "High",
        "location": "Highway B",
    },
    
]




# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_SPEEDING,data)


for record in db.fetchall(COLLECTION_SPEEDING):
    print(record)