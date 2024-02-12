from DBHandler import MongoDBSingleton
from constants import COLLECTION_USER_ACTIVITY


data = [
    {
        "user_id": "U001",
        "timestamp": "2024-02-04T08:00:00",
        "activity_type": "login",
        "frequency_and_duration": "Daily, 8 hours",
        "user_activity_logs": ["Reports generated", "Alerts set"],
    },
    {
        "user_id": "U002",
        "timestamp": "2024-02-04T12:30:00",
        "activity_type": "logout",
        "frequency_and_duration": "Daily, 6 hours",
        "user_activity_logs": ["Reports generated"],
    },
   
]

# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_USER_ACTIVITY,data)


for record in db.fetchall(COLLECTION_USER_ACTIVITY):
    print(record)