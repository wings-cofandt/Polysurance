from DBHandler import MongoDBSingleton
from constants import COLLECTION_VEHICLE_MAINTAINENCE


data = [
    {
        "vehicle_id": "V001",
        "maintenance_task": "Oil Change",
        "completion_date": "2024-02-04",
        "cost": 50,
        "downtime_hours": 2,
    },
    {
        "vehicle_id": "V002",
        "maintenance_task": "Brake Replacement",
        "completion_date": "2024-02-04",
        "cost": 120,
        "downtime_hours": 4,
    },
   
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_VEHICLE_MAINTAINENCE,data)

for record in db.fetchall(COLLECTION_VEHICLE_MAINTAINENCE):
    
    print(record)

