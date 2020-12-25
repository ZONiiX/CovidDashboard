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


def getStateData(name):
    try:
        cursor.execute(
            """SELECT * FROM state WHERE name='%s'""", name)
        print(cursor.fetchall())
    except:
        print("Could not gather state data, the input could be spelled wrong.")


def getCountyData(name):
    try:
        cursor.execute(
            """SELECT * FROM county WHERE name='%s'""", name)
        print(cursor.fetchall())
    except:
        print("Could not gather county data, the input could be spelled wrong.")


addState('fakestate', 13000, 1300, 12)
