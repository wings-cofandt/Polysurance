from DBHandler import MongoDBSingleton
from constants import COLLECTION_CUSTOMER_SUMMARY


data = [
    {
        "customer_id": "C001",
        "service_level": "Premium",
        "response_times": {"morning": "On time", "afternoon": "Slight delay"},
        "service_efficiency": "High",
    },
    {
        "customer_id": "C002",
        "service_level": "Standard",
        "response_times": {"morning": "Slight delay", "afternoon": "On time"},
        "service_efficiency": "Medium",
    },
    
]

# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_CUSTOMER_SUMMARY,data)

for record in db.fetchall(COLLECTION_CUSTOMER_SUMMARY):
    
    print(record)

