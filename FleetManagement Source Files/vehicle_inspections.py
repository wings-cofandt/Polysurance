from DBHandler import MongoDBSingleton
from constants import COLLECTION_VEHICLE_INSPECTIONS


data = [
    {
        "vehicle_id": "V001",
        "inspection_date": "2024-02-04",
        "inspection_result": "Pass",
        "faults_and_defects_reported": "None",
        "repair_and_maintenance_follow-ups": "None",
    },
    {
        "vehicle_id": "V002",
        "inspection_date": "2024-02-04",
        "inspection_result": "Fail",
        "faults_and_defects_reported": "Brake issues",
        "repair_and_maintenance_follow-ups": "Immediate brake repair",
    },
    
]



# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_VEHICLE_INSPECTIONS,data)

for record in db.fetchall(COLLECTION_VEHICLE_INSPECTIONS):
    
    print(record)














