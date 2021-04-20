# CS540 - Project

This file contains instructions on how to utilize the data contained in the "marina_and_boatramps_distance.csv" file. It also contains information related to all files present in this repository.

# Instructions for using the data

To use the distance data first download the file labeled "marina_and_boatramps_distance.csv"
After downloading the file, you will need to perform an update on the volusia.parcel table or any other table that you would like to add the data to. 
There are two new columns that will need to be added to the table: 
      mar_distance
      br_distance
These columns contain the distance a given parcel is from the nearest marina and boatramp respectively in miles.

It is also recommended that you download the marinas.zip and boatramps.zip files so you can use them in QGIS to visually see where each marina/boatramp is located.
Once downloaded you can use QGIS to import the .shp file for each as a new layer. When done correctly you will see new data points for each marina and boatramp in Volusia county, Florida.

# File Descriptions

marina_and_boatramps_distance.csv - A csv file containing three columns: parid, mar_distance, br_distance.
  parid: the parcel identification number contained in the volusia.parcel table (only includes parcels that have valid geometry data)
  mar_distance: the distance a parcel is from the nearest marina in miles
  br_distance: the distance a parcel is from the nearest boatramp in miles

marinas.zip - a zip file containing gis files used to add the marina locations as a vector layer in QGIS

boatramps.zip - a zip file containing gis files used to add the boatramp location as a vector layer in QGIS
  
nearest_marinas.sql - SQL script used to obtain the distance a given parcel is from the nearest marina. Requires the marina data to be added as a table to the volusia schema. The column labeled name in this table must be renamed to marinaname in order for the query to be completed.
  
nearest_boatramps.sql -  SQL script used to obtain the distance a given parcel is from the nearest boatramp. Requires the boatramp data to be added as a table tot he volusia schema.

update_marina_and_boatramp_distances.py - A python script that was used to obtain the distances between each parcel and the nearest marina/boatramp
