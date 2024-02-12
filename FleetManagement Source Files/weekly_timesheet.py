from DBHandler import MongoDBSingleton
from constants import COLLECTION_WEEKLY_TIMESHEET


data= [
    {
        "driver_id": "D001",
        "week_start_date": "2024-02-01",
        "week_end_date": "2024-02-07",
        "daily_totals": {"Monday": 8, "Tuesday": 8, "Wednesday": 8, "Thursday": 8, "Friday": 8},
        "weekly_overtime_analysis": "No overtime",
    },
    {
        "driver_id": "D002",
        "week_start_date": "2024-02-01",
        "week_end_date": "2024-02-07",
        "daily_totals": {"Monday": 9, "Tuesday": 9, "Wednesday": 9, "Thursday": 9, "Friday": 9},
        "weekly_overtime_analysis": "Overtime on Thursday and Friday",
    },
    
]



# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_WEEKLY_TIMESHEET,data)


for record in db.fetchall(COLLECTION_WEEKLY_TIMESHEET):
    print(record)