#utils

import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'driver={SQL Server};'
            'server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'database=grocerystoresimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
    except:
        conn = None

    return conn
