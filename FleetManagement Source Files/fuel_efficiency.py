from DBHandler import MongoDBSingleton
from constants import COLLECTION_FUEL_EFFICIENCY


data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T12:30:00",
        "fuel_consumption_rate": 9.5, 
        "actual_fuel_efficiency": 10,
        "expected_fuel_efficiency": 12,
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T14:45:00",
        "fuel_consumption_rate": 8.5,
        "actual_fuel_efficiency": 12,
        "expected_fuel_efficiency": 14,
    },
    
]


# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_FUEL_EFFICIENCY,data)

for record in db.fetchall(COLLECTION_FUEL_EFFICIENCY):
    
    print(record)

