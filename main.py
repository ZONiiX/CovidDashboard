import sqlite3

connection = sqlite3.connect('coviddashboard.db')

cursor = connection.cursor()


def addState(name, totalcases, totaldeaths, dailycases):
    try:
        cursor.execute(""" INSERT INTO state(name, totalcases, totaldeaths, dailycases) VALUES (%s, %s, %s, %s)""",
                       name, totalcases, totaldeaths, dailycases)
        print('%s has been added to the database successfully', name)
    except:
        print('An error has occured')


def fetchData(name):
    try:
