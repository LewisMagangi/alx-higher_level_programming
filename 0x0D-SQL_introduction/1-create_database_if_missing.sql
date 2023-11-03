-- a script that creates the database hbtn_0c_0 in your MySQL server.
-- Check if the database hbtn_0c_0 exists
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'hbtn_0c_0')
BEGIN
    -- Create the database if it doesn't exist
        CREATE DATABASE hbtn_0c_0;
	END;   
ELSE
BEGIN
    -- Database exists
    CREATE DATABASE hbtn_0c_0;
    END;
