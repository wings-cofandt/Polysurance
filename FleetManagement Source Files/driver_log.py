from DBHandler import MongoDBSingleton
from constants import COLLECTION_DRIVER_LOG


data = [
    {
        "driver_id": "D001",
        "date": "2024-02-04",
        "shift_start_time": "08:00:00",
        "shift_end_time": "16:00:00",
        "breaks_and_idle_times": "Break: 12:00-12:30, Idle: 15 mins",
        "time_spent_at_each_job_or_location": "Job A: 3 hours, Job B: 4 hours",
    },
    {
        "driver_id": "D002",
        "date": "2024-02-04",
        "shift_start_time": "10:00:00",
        "shift_end_time": "18:00:00",
        "breaks_and_idle_times": "Break: 13:30-14:00, Idle: 20 mins",
        "time_spent_at_each_job_or_location": "Job C: 5 hours, Job D: 2.5 hours",
    },
   
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_DRIVER_LOG,data)

for record in db.fetchall(COLLECTION_DRIVER_LOG):
    
    print(record)














