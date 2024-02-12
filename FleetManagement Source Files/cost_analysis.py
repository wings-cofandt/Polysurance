from DBHandler import MongoDBSingleton
from constants import COLLECTION_COST_ANALYSIS


data = [
    {
        "vehicle_id": "V001",
        "trip_job_id": "TJ001",
        "cost_per_trip_job": 200,
        "fuel_costs": 100,
        "maintenance_and_operational_costs": 50,
    },
    {
        "vehicle_id": "V002",
        "trip_job_id": "TJ002",
        "cost_per_trip_job": 180,
        "fuel_costs": 90,
        "maintenance_and_operational_costs": 40,
    },
   
]



# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_COST_ANALYSIS,data)


for record in db.fetchall(COLLECTION_COST_ANALYSIS):
    print(record)