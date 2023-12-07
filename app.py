from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psutil as ps
import time

# Connect to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:3306/system_performance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

# Create the database object
db = SQLAlchemy(app)
connection = db.engine.connect()

class Performance(db.Model):
    # Define the fields based on the database
    time = db.Column(db.DateTime, primary_key=True)
    cpu_usage = db.Column(db.DECIMAL(5,2))
    memory_usage = db.Column(db.DECIMAL(5,2))
    cpu_interrupts = db.Column(db.DECIMAL(18,0))
    cpu_calls = db.Column(db.DECIMAL(18,0))
    memory_used = db.Column(db.DECIMAL(18,0))
    memory_free = db.Column(db.DECIMAL(18,0))
    bytes_sent = db.Column(db.DECIMAL(18,0))
    bytes_received = db.Column(db.DECIMAL(18,0))
    disk_usage = db.Column(db.DECIMAL(5,2))

    def __init__(self, time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage):
        self.time = time
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.cpu_interrupts = cpu_interrupts
        self.cpu_calls = cpu_calls
        self.memory_used = memory_used
        self.memory_free = memory_free
        self.bytes_sent = bytes_sent
        self.bytes_received = bytes_received
        self.disk_usage = disk_usage

def getMetrics():
    cpu_usage = ps.cpu_percent(interval=1)
    memory_usage = ps.virtual_memory().percent
    cpu_interrupts = ps.cpu_stats().interrupts
    cpu_calls = ps.cpu_stats().syscalls
    memory_used = ps.virtual_memory().used
    memory_free = ps.virtual_memory().free
    bytes_sent = ps.net_io_counters().bytes_sent
    bytes_received = ps.net_io_counters().bytes_recv
    disk_usage = ps.disk_usage('/').percent
    return cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage

def insertMetrics():
    cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage = getMetrics()
    performance = Performance(time.strftime('%Y-%m-%d %H:%M:%S'), cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage)
    db.session.add(performance)
    db.session.commit()

# Insert the metrics into the database
while True:
    insertMetrics()
    print("Inserting metrics into the database...Press Ctrl+C to stop")