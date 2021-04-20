"""
@author: Kody Miller

This code can be used to obtain the distances a parcel is from a marina/boatramp.
To execute quickly this code requires indexing of the volusia.parcel table
You must also add the columns to the database ahead of time:
    alter volusia.parcel add column mar_distance double precision;
    alter volusia.parcel add column br_distance double precision
Note: The password has been removed from the conn section, to run this code simply
insert the password for the postgres user in the space provided ('_______')

"""

import psycopg2
import re
import matplotlib.pyplot as plt
import os
import pandas as pd

# connection to database:
try:
    conn = psycopg2.connect("dbname='spatial' user='postgres' host='localhost' password='________'")
except:
    print("cant connect to the database")

# Set up cursors for each operation
cur = conn.cursor()
marina_cur = conn.cursor()
boatramp_cur = conn.cursor()
mar_update_cur = conn.cursor()
br_update_cur = conn.cursor()

# Obtain parids for all rows that have valide geometry
sql = "select parid::integer from volusia.parcel p where geom is not null" # limit 10"
print('SQL: ', sql)
cur.execute(sql)

# Loop through the non null rows computing distances between parid location and marina/boatramp location
# Add distance values to database columns
print(cur)
i=0
row = cur.fetchone()
while row is not None:
    i = i + 1
    parid = str(row[0])  
    # Computes distance to nearest marina in miles
    marina_sql = "select marinaname, pid, geom, ST_Distance(marinas.geom, (select geom from volusia.parcel where parid=" + parid + "))/5280 from volusia.marinas order by marinas.geom <-> (select geom from volusia.parcel where parid=" + parid + ") limit 1;"
    marina_cur.execute(marina_sql)
    marina_row = marina_cur.fetchone()
    marinaname = str(marina_row[0])
    marina_distance = marina_row[3]
    
    # Computes distance to nearest boatramp in miles
    boatramp_sql = "select  rampname, geom, ST_Distance(boatramps.geom, (select geom from volusia.parcel where parid="+ parid +"))/5280 from volusia.boatramps order by boatramps.geom <-> (select geom from volusia.parcel where parid="+ parid +") limit 1;"
    boatramp_cur.execute(boatramp_sql)
    boatramp_row = boatramp_cur.fetchone()
    boatrampname = str(boatramp_row[0])
    boatramp_distance = boatramp_row[2]
  
    update_sql_m = "update volusia.parcel set mar_distance = " + str(marina_distance) + " where parcel.parid=" + parid + ";"
    update_sql_br = "update volusia.parcel set br_distance = " + str(boatramp_distance) + " where parcel.parid=" + parid + ";"
    mar_update_cur.execute(update_sql_m)  
    br_update_cur.execute(update_sql_br)
    print(i)
    if i%100 == 0:
          print('Committing to database') 
          conn.commit()
    row = cur.fetchone()

conn.commit()
conn.close()


