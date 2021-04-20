select  marinaname, pid, geom, ST_Distance(marinas.geom, (select geom from volusia.parcel where parid = 3857607))/5280 from volusia.marinas
order by marinas.geom <-> (select geom from volusia.parcel where parid = 3857607) 
limit 1

