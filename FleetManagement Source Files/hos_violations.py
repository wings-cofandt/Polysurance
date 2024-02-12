from DBHandler import MongoDBSingleton
from constants import COLLECTION_HOS_VIOLATIONS


data = [
    {
        "driver_id": "D001",
        "violation_type": "Exceeding daily driving hours",
        "timestamp": "2024-02-04T18:30:00",
        "severity": "Major",
        "remedial_actions_taken": "Driver sent for mandatory rest",
    },
    {
        "driver_id": "D002",
        "violation_type": "Incomplete rest break",
        "timestamp": "2024-02-04T15:45:00",
        "severity": "Minor",
        "remedial_actions_taken": "Driver advised to take proper rest breaks",
    },
    
]




# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_HOS_VIOLATIONS,data)

for record in db.fetchall(COLLECTION_HOS_VIOLATIONS):
    
    print(record)














