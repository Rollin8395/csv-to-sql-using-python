import pypyodbc as odbc
import pandas as pd

"""
Importing dataset from csv
"""

df = pd.read_csv('sparshlog.csv')
columns = ['Time', ' Main Type', ' Sub Type', ' Param', ' User', ' IP', ' Detail']
df_data = df[columns]
records = df_data.values.tolist()


"""Create SQL server connection string"""
DRIVER = 'SQL Server'
SERVER_NAME = 'ROLLIN\SQLEXPRESS'
DATABASE_NAME = 'JJ'

def connection_string(driver,server_name,database_name):
    conn_string = f"""
      DRIVER={{{driver}}};
      SERVER={server_name};
      DATABASE={database_name};
    """
    return conn_string

"""Create database connection instance"""

try:
    conn=odbc.connect(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME))
except odbc.DatabaseError as e:
    print('Database Error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))

"""
Create a cursor connection
"""
sql_insert = '''  
      INSERT INTO New_database_table 
      VALUES(?,?,?,?,?,?,?)
'''
try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert,records)
    cursor.commit();
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    print('DONE')
    cursor.close()
    conn.close()