songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# create new tables
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
(songplay_id serial PRIMARY KEY, start_time timestamp REFERENCES time(start_time), 
user_id int NOT NULL REFERENCES users(user_id) , 
level varchar, song_id varchar REFERENCES songs(song_id), artist_id varchar REFERENCES artists(artist_id),
 session_id varchar, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
(user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
(song_id varchar PRIMARY KEY, title varchar, artist_id varchar REFERENCES artists(artist_id),
 year int, duration numeric )
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
(artist_id varchar PRIMARY KEY, 
name varchar, location varchar, latitude numeric, longitude numeric)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
(start_time timestamp PRIMARY KEY, 
hour int, day varchar, week varchar, month varchar, year int, weekday varchar)
""")

#Insert data into the tables

songplay_table_insert = ("""INSERT INTO songplays 
    (start_time, user_id, level , song_id, artist_id, session_id, location, user_agent)
    values(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE 
        SET
        first_name = excluded.first_name,
        last_name = excluded.last_name,
        gender = excluded.gender,
        level = excluded.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO public.artists (artist_id, name, location, latitude, longitude)
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO UPDATE
        SET
        name = excluded.name,
        location = excluded.location,
        latitude = excluded.latitude,
        longitude = excluded.longitude
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    values (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# Sample Query to find songs
song_select = (""" SELECT songs.song_id, artists.artist_id
                   FROM songs JOIN artists 
                   ON songs.artist_id = artists.artist_id
                   WHERE songs.title = %s
                   AND artists.name = %s
                   AND songs.duration = %s
""")



# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create,  time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

