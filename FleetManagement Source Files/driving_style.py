from DBHandler import MongoDBSingleton
from constants import COLLECTION_DRIVING_STYLE


data = [
    {
        "driver_id": "D001",
        "safety_score": 85,
        "aggressive_driving_behaviors": {"speeding": 3, "harsh_braking": 2, "harsh_acceleration": 1},
    },
    {
        "driver_id": "D002",
        "safety_score": 90,
        "aggressive_driving_behaviors": {"speeding": 1, "harsh_braking": 1, "harsh_acceleration": 0},
    },
 
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_DRIVING_STYLE,data)

for record in db.fetchall(COLLECTION_DRIVING_STYLE):
    
    print(record)




