-- script that lists all the cities of California that can be found in the
-- database hbtn_0d_usa
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.name FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa.state_id = 1 ORDER BY hbtn_0d_usa.cities.id ASC;
