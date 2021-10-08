# Data-Modeling-With-PostgreSQL
## Sparkify ETL 
In this project, the following concepts have been used.
  1. Design Database - Star Schema
  2. Develop ETL Pipeline - Python, Pandas
### Project Introduction:
A startup company Sparkify, wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### Objective:
Create Postgres analytical database with tables designed for running queries. As a Data Engineer, my role is to create a database schema and ETL pipeline for this analysis. 
### Prerequisites:
This project makes the folowing assumptions:

  1. Python 3 is available
  2. pandas and psycopg2 are available
  3. A PosgreSQL database is available on localhost
### Database Schema:
![image](https://user-images.githubusercontent.com/91047428/136537443-16d79c4d-5a2a-4785-9f47-28f74637a39b.png)
### ETL Process:
**Song Dataset**

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

  >song_data/A/B/C/TRABCEI128F424C983.json

  >song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```
{
    "num_songs": 1,
    "artist_id": "ARJIE2Y1187B994AB7",
    "artist_latitude": null,
    "artist_longitude": null,
    "artist_location": "",
    "artist_name": "Line Renaud",
    "song_id": "SOUPIRU12A6D4FA1E1",
    "title": "Der Kleine Dompfaff",
    "duration": 152.92036,
    "year": 0
}
```

This information is parsed to populate the Songs and Artists Dimension tables.

**Log Dataset**

The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.

  >log_data/2018/11/2018-11-12-events.json
  
  >log_data/2018/11/2018-11-13-events.json
  
This data contains information of which songs Users listened to at a specific time. Information is parsed to provide data for the Songplays Fact table and the Users and Time Dimension tables. The `songplays.artist_id` and `songplays.song_id` columns are populated by a lookup based on the Song Title, Artist Name and song Duration.


### Project structure:
**Files used in the project:**

  -**data** folder nested at the home of the project, where all needed jsons reside.
  
  -**sql_queries.py** contains all the SQL queries, and is imported into the files bellow.
  
  -**create_tables.py** drops and creates tables.Run this file to reset your tables before each time you run ETL scripts.
  
  -**test.ipynb** displays the first few rows of each table to check the data.
  
  -**etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into respective tables (sample data).
  
  -**etl.py** reads and processes files from song_data and log_data and loads them into tables.
  
  -**README.md** current file, provides discussion on my project.

