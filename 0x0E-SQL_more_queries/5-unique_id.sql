-- script that creates the table unique_id on a MySQL server
CREATE TABLE IF NOT EXISTS unique_id(id UNIQUE DEFAULT 1,
name VARCHAR(256));
