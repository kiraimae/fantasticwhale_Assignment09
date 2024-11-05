
#main.py

from utilsPackage.utils import get_db_connection  # Importing the connection function from utils
import pyodbc #For Question 2
import random


try:
    conn= get_db_connection()
#Submits sql to database and stores in cursor
    cursor = conn.cursor() #Temporary table
    cursor.execute('SELECT * FROM tProduct')
except Exception as e:
    print("Error accessing database")
    print(e)
    exit() #Give up