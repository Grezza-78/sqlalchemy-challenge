#################################################
# Importing libraries for access
#################################################


import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# Setting the connection to the data base
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflecting an existing database into a new model
Base = automap_base()

# Reflecting the tables
Base.prepare(autoload_with=engine)

# Save references to new tables for access
measure_table = Base.classes.measurement
station_table = Base.classes.station


#################################################
# Flask Setup
#################################################


# Initiliasing Flask setup
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


# Setting variavbles that will be used in several routes
session = Session(engine)

# Finding the most recent date in the data set
most_recent_dt = session.query(measure_table.date).order_by(measure_table.date.desc()).first()[0]

# Calculating the date one year from the last date in the data set
most_recent_date = dt.datetime.strptime(most_recent_dt, "%Y-%m-%d")
most_recent_date = most_recent_date.date()
year_ago = most_recent_date - dt.timedelta(days=365)

session.close()

# Establising homepage route outling the API routes for the various applications
@app.route("/")
def homepage():
    return (
        """Welcome to the Hawaiian Climate Application<br/> <br/>"""
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> (enter start date in the format: 'yyyy-mm-dd'). Dates entered must be between 2010-01-01 to 2017-08-23.<br/>"
        f"/api/v1.0/<start>/<end> (enter start & end in the format: (start)/(end) 'yyyy-mm-dd/'yyyy-mm-dd'). Dates entered must be between 2010-01-01 to 2017-08-23.<br/>"
    )

# Returns a listing of the most recent 12 months's precipation amounts recorded in the data
@app.route("/api/v1.0/precipitation")
def date_prcp():

    # Connecting to the sqlite file   
    session = Session(engine)
    
    # Extracting date and perpciptation from the Measurement table 
    # fitlering the date on the date from a year ago
    results = session.query(measure_table.date, measure_table.prcp).\
                     filter(measure_table.date >= year_ago).all()

    # Disconnecting to the sqlite file   
    session.close()

    # Setting up a dictonary to append cycle through the data found in results
    all_date_prcp_points = []

    for date, prcp in results:
        date_prcp_dict = {}
        date_prcp_dict["date"] = date
        date_prcp_dict["prcp"] = prcp
        all_date_prcp_points.append(date_prcp_dict)

    # Returning JSON list of the dictionary
    return jsonify(all_date_prcp_points)


# Return a listing of all the Hawaiian Weather station information 
# contained in the Stations table data
@app.route("/api/v1.0/stations")
def temp_obs():

    # Connecting to the sqlite file   
    session = Session(engine)

    # Extracting all the stations information from the Stations table
    results = session.query(station_table.id, station_table.station, station_table.name,\
                            station_table.latitude, station_table.longitude,\
                            station_table.elevation).all()

    # Disconnecting to the sqlite file   
    session.close()

    # Setting up a dictonary to append cycle through the data found in results
    station_points = []
    for id, station, name, lat, long, elev in results:
        stations_info_dict = {}
        stations_info_dict["Id"] = id
        stations_info_dict["Station Code"] = station
        stations_info_dict["Station Name"] = name
        stations_info_dict["Latitude"] = lat
        stations_info_dict["Longitute"] = long
        stations_info_dict["Elevation"] = elev
        station_points.append(stations_info_dict)

    # Returning JSON list of the dictionary    
    return jsonify(station_points)


# Returns a listing of the most recent 12 months's tempreature observations recorded
# for the most active station in the data
@app.route("/api/v1.0/tobs")
def stations():

    # Connecting to the sqlite file
    session = Session(engine)

    # Identifying the most active station in the dataset
    most_active_stn = session.query(measure_table.station, func.count(measure_table.station)).\
                           group_by(measure_table.station).\
                           order_by(func.count(measure_table.station).desc()).first()
    most_active_stn_id = most_active_stn[0]

    # Extracting the date and temp observations data from the Measurement table 
    # filtering on most active station and date data for one year
    results = session.query(measure_table.station, measure_table.date, measure_table.tobs).\
                     filter(measure_table.station == most_active_stn_id).\
                     filter(measure_table.date >= year_ago).all()

    # Disconnecting to the sqlite file         
    session.close()

    # Setting up a dictonary to cycle through the data found in results
    all_date_tobs_points = []
    for station, date, tobs in results:
        date_tobs_dict = {}
        date_tobs_dict["Station ID"] = station
        date_tobs_dict["Date"] = date
        date_tobs_dict["Observed Temparature"] = tobs
        all_date_tobs_points.append(date_tobs_dict)

    # Returning JSON list of the dictionary    
    return jsonify(all_date_tobs_points)


# Returns a listing maximum, minimum and average temperatures 
# between user selected start date
@app.route("/api/v1.0/<start>", defaults = {"end" : None})

# Returns a listing maximum, minimum and average temperatures 
# between user selected start and end date
@app.route("/api/v1.0/<start>/<end>")
def temp_dates(start, end=None):

    # Converting user start date to date time format to assist 
    # with filerting of data
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    start_date = start_date.date()

    # Coverting end date to date time format to assist with filerting of data
    # If no end date is received then route uses most current date from the 
    # data set as last data point to assist with filerting of data
    if end is None:
        end_date = most_recent_date
    # If user end date is received then coverts date to date time format 
    # to assist with filerting of data
    else:
        end_date = dt.datetime.strptime(end, "%Y-%m-%d")
        end_date = end_date.date()

    # Connecting to the sqlite file      
    session = Session(engine)

    # Extracting the date and temp observations data from the Measurement table 
    # filtering on date data between the start and end date variables received
    results = session.query((func.min(measure_table.tobs)), 
                            (func.avg(measure_table.tobs)),
                            (func.max(measure_table.tobs))).\
                            filter(measure_table.date >= start_date).\
                            filter(measure_table.date <= end_date).all()

    # Disconnecting to the sqlite file     
    session.close()

    # Setting up a dictonary to cycle through the data found in results
    date_tobs_points = []
    for min, avg, max in results:
        date_tobs_dict = {}
        date_tobs_dict["Temp Minimum"] = min
        date_tobs_dict["Temp Average"] = avg 
        date_tobs_dict["Temp Maximum"] = max
        date_tobs_points.append(date_tobs_dict)

    # Returning JSON list of the dictionary    
    return jsonify(date_tobs_points)


# Defining the main behaviour and running the application
if __name__ == "__main__":
    app.run(debug=True)