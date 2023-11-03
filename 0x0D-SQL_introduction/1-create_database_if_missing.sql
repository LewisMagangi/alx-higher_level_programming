-- a script that creates the database hbtn_0c_0 in your MySQ
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'YourDatabaseName')
BEGIN
    -- Database exists
    CREATE DATABASE hbtn_0c_0;
END;
ELSE
BEGIN
    -- Database does not exist
    CREATE DATABASE hbtn_0c_0;
END;
