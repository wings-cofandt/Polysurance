from DBHandler import MongoDBSingleton
from constants import COLLECTION_HARSH_DRIVING_INCIDENTS


data = [
    {
        "driver_id": "D001",
        "incident_type": "Harsh Braking",
        "timestamp": "2024-02-04T12:45:00",
        "location": "Intersection A",
        "severity": "Moderate",
    },
    {
        "driver_id": "D002",
        "incident_type": "Harsh Acceleration",
        "timestamp": "2024-02-04T15:30:00",
        "location": "Highway B",
        "severity": "High",
    },
    
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_HARSH_DRIVING_INCIDENTS,data)

for record in db.fetchall(COLLECTION_HARSH_DRIVING_INCIDENTS):
    print(record)