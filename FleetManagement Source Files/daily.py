from DBHandler import MongoDBSingleton
from constants import COLLECTION_DAILY


data = [
    {
        "date": "2024-02-04",
        "activities": {
            "start_time": "08:00:00",
            "end_time": "17:00:00",
            "jobs_completed": 5,
            "breaks_taken": 2,
            "idle_time": 30, 
        },
    },
    {
        "date": "2024-02-05",
        "activities": {
            "start_time": "09:00:00",
            "end_time": "18:00:00",
            "jobs_completed": 7,
            "breaks_taken": 3,
            "idle_time": 45,
        },
    },
  
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_DAILY,data)

for record in db.fetchall(COLLECTION_DAILY):
    
    print(record)

