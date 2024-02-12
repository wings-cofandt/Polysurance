from DBHandler import MongoDBSingleton
from constants import COLLECTION_TRAVEL_STOPS_WORK_ORDERS



data = [
    {
        "vehicle_id": "V001",
        "stop_order_id": "SO001",
        "duration": 0.5,
        "planned_vs_actual_routes": "Route A",
        "time_spent_on_each_work_order": 2.0,
        "details_of_unplanned_stops": "None",
    },
    {
        "vehicle_id": "V002",
        "stop_order_id": "SO002",
        "duration": 1.2,
        "planned_vs_actual_routes": "Route B",
        "time_spent_on_each_work_order": 3.5,
        "details_of_unplanned_stops": "Traffic delay",
    },
    
]

# Get instance of MongoDBSingleton
db = MongoDBSingleton.getInstance()

# Insert many records
db.insert_multiple(COLLECTION_TRAVEL_STOPS_WORK_ORDERS,data)


for record in db.fetchall(COLLECTION_TRAVEL_STOPS_WORK_ORDERS):
    print(record)