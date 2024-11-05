# Name: Alexis Tipkemper-Sparks / Kayla Wilson / Jared Rababy 
# email:  tipkemam@mail.uc.edu / wilso5ky@mail.uc.edu /rababyjd@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/07/2024
# Course #/Section:  IS 4010
# Semester/Year: Fall 2024
# Brief Description of the assignment:  Connection to sql server db to pull info 

# Brief Description of what this module does: Practice connection to sql server, extract data, produces output
# Citations: GeeksforGeeks / W3Schools / InClass from last week
# Anything else that's relevant: N/A Github makes us sad

#utils

import pyodbc
# Connect to sql server - grocerystoresimulator
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
