from DBHandler import MongoDBSingleton
from constants import COLLECTION_FUEL_PURCHASED


data = [
    {
        "vehicle_id": "V001",
        "transaction_date": "2024-02-04",
        "fuel_quantity": 30,
        "cost": 90,
        "fuel_efficiency": 10,  
    },
    {
        "vehicle_id": "V002",
        "transaction_date": "2024-02-04",
        "fuel_quantity": 25,
        "cost": 75,
        "fuel_efficiency": 12,
    },
    
]



# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_FUEL_PURCHASED,data)

for record in db.fetchall(COLLECTION_FUEL_PURCHASED):
    
    print(record)

