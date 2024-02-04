# Fleet Management System

## Overview

The Fleet Management System is a comprehensive solution for monitoring and optimizing fleet operations. This system provides real-time insights into vehicle locations, activities, and various performance metrics. It aims to enhance efficiency, reduce costs, and improve overall fleet management.

## Database Connections

1. `weekly_timesheet_collection`: Stores weekly timesheet data for drivers.
2. `cost_analysis_collection`: Tracks the cost analysis of trips and jobs.
3. `speeding_collection`: Captures instances of speeding by drivers.
4. `harsh_driving_incidents_collection`: Records incidents of harsh driving behavior.
5. `driving_style_collection`: Stores information on the driving style of each driver.
6. `driver_log_collection`: Contains daily logs of drivers' activities.
7. `vehicle_inspections_collection`: Logs pre-trip and post-trip inspection details for vehicles.
8. `hos_violations_collection`: Keeps track of hours of service violations.
9. `vehicle_maintenance_collection`: Records summaries and details of vehicle maintenance services.
10. `fuel_purchased_collection`: Provides a detailed review of fuel transactions.
11. `fuel_efficiency_collection`: Stores data related to the fuel efficiency of vehicles.
12. `daily_collection`: Captures daily activities of drivers and vehicles.
13. `fleet_summary_collection`: Provides a high-level summary of fleet activity.
14. `customer_summary_collection`: Breaks down fleet behavior based on customer interactions.
15. `exception_collection`: Summarizes activities that violate company vehicle usage policies.
16. `utilization_collection`: Stores detailed data on vehicle and asset usage.
17. `daily_timecard_collection`: Tracks drivers' daily activities and work shifts.
18. `weekly_timesheet_collection`: Reviews daily totals for regular and overtime hours throughout a driver's workweek.
19. `cost_analysis_collection`: Attaches a monetary value to the time spent traveling and on-site at a job, based on cost assumptions for wages and fuel.
20. `speeding_collection`: Monitors instances of drivers exceeding predefined speeding thresholds.
21. `harsh_driving_incidents_collection`: Provides detailed information about each harsh driving incident triggered by a driver throughout the workday.
22. `driving_style_collection`: Displays summary-level information of aggressive driving behavior, including a safety score ranking for each driver.
23. `driver_log_collection`: Offers a printout of drivers' daily logs, including driving hours, rest periods, breaks, and compliance with regulations.

## Dummy Data

Each collection in the database contains documents with dummy data, providing a representative sample of the kind of information that can be stored and analyzed. Feel free to explore the structure of each collection and adapt the database to meet your specific needs.


## Getting Started

Follow these steps to get a local copy of the project up and running on your machine.

### Prerequisites

&#10004; Python (version 3.11.3)
&#10004; MongoDB installed and running

### Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/wings-cofandt/fleet-management-system.git
