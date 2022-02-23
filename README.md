# csv-to-sql-using-python
This python code will read the csv file and send it to a selected server in sql


First create a table using sql with th given code:


USE JJ 
GO

IF OBJECT_ID('New_database_table') IS NOT NULL
  DROP TABLE New_database_table;
GO

CREATE TABLE New_database_table(
 Date_Time DATETIME NOT NULL,
 Main_Type NVARCHAR(100) NOT NULL,
 Sub_Type NVARCHAR(100) NOT NULL,
 Param_ NVARCHAR(100) NOT NULL,
 User_ NVARCHAR(100) NOT NULL,
 IP_ NVARCHAR(100) NOT NULL,
 Detail NVARCHAR(100) NOT NULL,
 );
 GO

 SELECT *
 FROM New_database_table 

 
