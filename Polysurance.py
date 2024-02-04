from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId  # Import ObjectId from bson
# Replace the placeholder with your Atlas connection string
uri = "mongodb://localhost:27017"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

# Create a database
db = client["FleetManagementDB"]

# Create collections
vehicle_locations_collection = db["VehicleLocations"]
geofence_reports_collection = db["GeofenceReports"]
travel_stops_work_orders_collection = db["TravelStopsWorkOrders"]
user_activity_collection = db["UserActivity"]
sensor_activity_collection = db["SensorActivity"]
distance_traveled_collection = db["DistanceTraveled"]
daily_timecard_collection = db["DailyTimecard"]
weekly_timesheet_collection = db["WeeklyTimesheet"]
cost_analysis_collection = db["CostAnalysis"]
speeding_collection = db["Speeding"]
harsh_driving_incidents_collection = db["HarshDrivingIncidents"]
driving_style_collection = db["DrivingStyle"]
driver_log_collection = db["DriverLog"]
vehicle_inspections_collection = db["VehicleInspections"]
hos_violations_collection = db["HOSViolations"]
vehicle_maintenance_collection = db["VehicleMaintenance"]
fuel_purchased_collection = db["FuelPurchased"]
fuel_efficiency_collection = db["FuelEfficiency"]
daily_collection = db["Daily"]
fleet_summary_collection = db["FleetSummary"]
customer_summary_collection = db["CustomerSummary"]
exception_collection = db["Exception"]
utilization_collection = db["Utilization"]


#Sample data goes into each respective documents
vehicle_locations_data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T12:30:00",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "activity": "start",
    },
    
    
]
vehicle_locations_collection.insert_many(vehicle_locations_data)

geofence_reports_data = [
    {
        "vehicle_id": "V001",
        "geofence_id": "G001",
        "entry_timestamp": "2024-02-04T12:30:00",
        "exit_timestamp": "2024-02-04T13:30:00",
        "duration": 1.0,
        "violation_status": False,
    },
    
]
geofence_reports_collection.insert_many(geofence_reports_data)

# TravelStopsWorkOrders collection
travel_stops_work_orders_data = [
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
travel_stops_work_orders_collection.insert_many(travel_stops_work_orders_data)

# UserActivity collection
user_activity_data = [
    {
        "user_id": "U001",
        "timestamp": "2024-02-04T08:00:00",
        "activity_type": "login",
        "frequency_and_duration": "Daily, 8 hours",
        "user_activity_logs": ["Reports generated", "Alerts set"],
    },
    {
        "user_id": "U002",
        "timestamp": "2024-02-04T12:30:00",
        "activity_type": "logout",
        "frequency_and_duration": "Daily, 6 hours",
        "user_activity_logs": ["Reports generated"],
    },
   
]
user_activity_collection.insert_many(user_activity_data)

# SensorActivity collection
sensor_activity_data = [
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
sensor_activity_collection.insert_many(sensor_activity_data)

# DistanceTraveled collection
distance_traveled_data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T12:30:00",
        "total_distance": 50.0,
        "state": "NY",
        "geofence_id": "G001",
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T14:45:00",
        "total_distance": 75.0,
        "state": "CA",
        "geofence_id": "G002",
    },
    
]
distance_traveled_collection.insert_many(distance_traveled_data)

# DailyTimecard collection
daily_timecard_data = [
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
daily_timecard_collection.insert_many(daily_timecard_data)

weekly_timesheet_data = [
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
weekly_timesheet_collection.insert_many(weekly_timesheet_data)

# CostAnalysis collection
cost_analysis_data = [
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
cost_analysis_collection.insert_many(cost_analysis_data)

# Speeding collection
speeding_data = [
    {
        "driver_id": "D001",
        "timestamp": "2024-02-04T14:00:00",
        "duration": 0.5,
        "severity": "Moderate",
        "location": "Highway A",
    },
    {
        "driver_id": "D002",
        "timestamp": "2024-02-04T16:30:00",
        "duration": 0.75,
        "severity": "High",
        "location": "Highway B",
    },
    
]
speeding_collection.insert_many(speeding_data)

# HarshDrivingIncidents collection
harsh_driving_incidents_data = [
    {
        "driver_id": "D001",
        "incident_type": "Harsh Braking",
        "timestamp": "2024-02-04T12:45:00",
        "location": "Intersection A",
        "severity": "Moderate",
    },
    {
        "driver_id": "D002",
        "incident_type": "Harsh Acceleration",
        "timestamp": "2024-02-04T15:30:00",
        "location": "Highway B",
        "severity": "High",
    },
    
]
harsh_driving_incidents_collection.insert_many(harsh_driving_incidents_data)

# DrivingStyle collection
driving_style_data = [
    {
        "driver_id": "D001",
        "safety_score": 85,
        "aggressive_driving_behaviors": {"speeding": 3, "harsh_braking": 2, "harsh_acceleration": 1},
    },
    {
        "driver_id": "D002",
        "safety_score": 90,
        "aggressive_driving_behaviors": {"speeding": 1, "harsh_braking": 1, "harsh_acceleration": 0},
    },
 
]
driving_style_collection.insert_many(driving_style_data)

# DriverLog collection
driver_log_data = [
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
driver_log_collection.insert_many(driver_log_data)

# VehicleInspections collection
vehicle_inspections_data = [
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
vehicle_inspections_collection.insert_many(vehicle_inspections_data)

# HOSViolations collection
hos_violations_data = [
    {
        "driver_id": "D001",
        "violation_type": "Exceeding daily driving hours",
        "timestamp": "2024-02-04T18:30:00",
        "severity": "Major",
        "remedial_actions_taken": "Driver sent for mandatory rest",
    },
    {
        "driver_id": "D002",
        "violation_type": "Incomplete rest break",
        "timestamp": "2024-02-04T15:45:00",
        "severity": "Minor",
        "remedial_actions_taken": "Driver advised to take proper rest breaks",
    },
    
]
hos_violations_collection.insert_many(hos_violations_data)

# VehicleMaintenance collection
vehicle_maintenance_data = [
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
vehicle_maintenance_collection.insert_many(vehicle_maintenance_data)

# FuelPurchased collection
fuel_purchased_data = [
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
fuel_purchased_collection.insert_many(fuel_purchased_data)

# FuelEfficiency collection
fuel_efficiency_data = [
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
fuel_efficiency_collection.insert_many(fuel_efficiency_data)

# Daily collection
daily_data = [
    {
        "date": "2024-02-04",
        "activities": {
            "start_time": "08:00:00",
            "end_time": "17:00:00",
            "jobs_completed": 5,
            "breaks_taken": 2,
            "idle_time": 30, 
        },
    },
    {
        "date": "2024-02-05",
        "activities": {
            "start_time": "09:00:00",
            "end_time": "18:00:00",
            "jobs_completed": 7,
            "breaks_taken": 3,
            "idle_time": 45,
        },
    },
  
]
daily_collection.insert_many(daily_data)

# FleetSummary collection
fleet_summary_data = [
    {
        "start_date": "2024-02-01",
        "end_date": "2024-02-07",
        "total_engine_time_on": 120,  
        "total_driving_duration": 90,
        "total_idling_duration": 30,
        "total_distance_driven": 800,
    },
    {
        "start_date": "2024-02-08",
        "end_date": "2024-02-14",
        "total_engine_time_on": 130,
        "total_driving_duration": 95,
        "total_idling_duration": 35,
        "total_distance_driven": 850,
    },
    
]
fleet_summary_collection.insert_many(fleet_summary_data)

# CustomerSummary collection
customer_summary_data = [
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
customer_summary_collection.insert_many(customer_summary_data)

# Exception collection
exception_data = [
    {
        "vehicle_id": "V001",
        "timestamp": "2024-02-04T15:00:00",
        "exception_type": "Unauthorized use",
        "location": "Outside working hours",
        "remedial_actions_taken": "Driver warned, additional training provided",
    },
    {
        "vehicle_id": "V002",
        "timestamp": "2024-02-04T18:30:00",
        "exception_type": "Long unauthorized stop",
        "location": "Geofence G002",
        "remedial_actions_taken": "Driver counseling session, geofence adjusted",
    },
    
]
exception_collection.insert_many(exception_data)

# Utilization collection
utilization_data = [
    {
        "vehicle_id": "V001",
        "usage_statistics": {"total_distance_driven": 500, "engine_time_on": 60, "idling_duration": 20},
        "resource_utilization": "Optimal",
        "asset_lifecycle_analysis": "Within expected lifespan",
    },
    {
        "vehicle_id": "V002",
        "usage_statistics": {"total_distance_driven": 600, "engine_time_on": 70, "idling_duration": 25},
        "resource_utilization": "Suboptimal",
        "asset_lifecycle_analysis": "Maintenance required",
    },
    
]
utilization_collection.insert_many(utilization_data)

# Close the MongoDB connection
client.close()