# sqlalchemy-challenge

This is SQLAlchemy challenge undertakes a climate analysis of weather and station data 
from Honolulu, Hawaii between 01/01/2010 and 23/08/2017.

The analysis has been broken up into two parts:

**Part 1: Analysing and Exploring the Climate Data**
Use SQLAlchemy ORM queries, Pandas and Matplotlib to undertake the analysis from an SQL database.

    * Precipitation Analysis
        * Identify the most recent date from the dataset\

        * Using the recent date to calculate the precipitation data for previous 12 months - the dates sorted from oldest to newest
        
        * Presenting the data on a bar-graph with dates on the x-axis, and millimetres of rain on the y-axis 

    * Station Analysis
        * Calculate the total number of stations in the dataset
        
        * Identify the most-active stations in the data and confirm:
            - a list of all the stations and their number of observations within the data sorted in descending order 
            thereby identifying the most active station
            - Calculate the minimum, maximum and average temperatures recorded at the most active station
        
        * Identify the temperature observations for the most recent 12 months' temperature data of the most active station as identified. 
        Once identified then present the data on a histogram-graph with the temperature observations on the x-axis, the frequency of temperature 
        observations on the y-axis with the observations combined into 12 bins. 

**Part 2: Designing a Climate App**
Design a Climate API application to access the SQL database using FLASK to present information in JSON format based on various API URLs

    * Creating a homepage
        * Developed homepage that list the API routes for a user to query the data:
            /api/v1.0/precipitation
            /api/v1.0/stations
            /api/v1.0/tobs
            /api/v1.0/<start> (enter start date in the format: 'yyyy-mm-dd'. Dates entered must be between 2010-01-01 to 2017-08-23.)
            /api/v1.0/<start>/<end> (enter start & end in the format: (start)/(end) 'yyyy-mm-dd/'yyyy-mm-dd'. Dates entered must be between 2010-01-01 to 2017-08-23.)

    * /api/v1.0/precipitation
        * Returns a JSON list of the dates and precipitation for the most recent year of data

    * /api/v1.0/stations
        * Returns a JSON list of all the information about the stations in the data

    * /api/v1.0/tobs
        * Returns a JSON list of the dates and temperature observations for the most active stations in the most recent year of data

    * /api/v1.0/<start> 
        * Returns the minimum, average and maximum temperature for all dates greater than or equal the input date (start date) provided by the user
        * User to enter their choice of start date in the format: 'yyyy-mm-dd'
        * Dates entered must be between 2010-01-01 to 2017-08-23

    * /api/v1.0/<start>/<end> 
        * Returns the minimum, average and maximum temperature for all dates between   the users' input start date and end date, inclusive
        * User to enter their choice of start date in the format: 'yyyy-mm-dd'
        * Dates entered must be between 2010-01-01 to 2017-08-23
