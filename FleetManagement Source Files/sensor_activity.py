from DBHandler import MongoDBSingleton
from constants import COLLECTION_SENSOR_ACTIVITY


data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T10:45:00",
        "sensor_type": "Temperature",
        "duration_of_sensor_activity": 1.5,
        "alerts_for_abnormal_sensor_activity": "None",
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T14:00:00",
        "sensor_type": "Door",
        "duration_of_sensor_activity": 0.75,
        "alerts_for_abnormal_sensor_activity": "Door open during transit",
    },
    
]

# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_SENSOR_ACTIVITY,data)


for record in db.fetchall(COLLECTION_SENSOR_ACTIVITY):
    print(record)