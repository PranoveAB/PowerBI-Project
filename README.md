# Real-Time System Performance Monitoring Project

## Overview

This project is a real-time system performance monitoring application designed to capture and visualize key metrics every second from a host computer. The metrics include CPU usage, disk usage, memory usage, network activity, CPU calls, CPU interrupts, and more. The data is stored in a MySQL database and presented in a Power BI dashboard for dynamic and intuitive visualization. The PowerBI dashboard consists of multiple visualizations including a line chart, a pie chart and a guage chart. The line chart displays the Network bytes sent and received per second, CPU Interrupts and CPU calls per. The pie chart displays the memory usage out of total virtual memory. The guage chart displays the CPU usage by core, disk usage, and current memory usage. The dashboard is refreshed every second to display the latest system performance metrics. 

## Project Structure

- **`app.py`**: The main Python application that collects system performance metrics using the `psutil` library and stores them in a MySQL database.
- **`requirements.txt`**: Lists the Python dependencies for the project.
- **`power_bi_dashboard.pbix`**: The Power BI file containing the dashboard configuration.

## Requirements

Ensure you have the following installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- psutil
- MySQL database
- Power BI Desktop

## Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/real-time-performance-monitoring.git
   cd real-time-performance-monitoring
    ```
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Create a MySQL database called `system_performance` and update the database connection string in `app.py`:

   ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:3306/db_name'
    ```
4. Run the application:

   ```bash
   python app.py
   ```
5. Open the Power BI dashboard file `PowerBI-Dashboard.pbix` and update the database connection string in the `Edit Queries` section.
6. Refresh the data in the dashboard to view the latest system performance metrics.

## Demo
![Demo](Demo.gif)