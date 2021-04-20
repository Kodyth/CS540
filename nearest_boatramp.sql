select  rampname, geom, ST_Distance(boatramps.geom, (select geom from volusia.parcel where parid = 3774906))/5280 from volusia.boatramps
order by boatramps.geom <-> (select geom from volusia.parcel where parid = 3774906) 
limit 1
