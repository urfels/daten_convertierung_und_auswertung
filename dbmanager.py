import sqlite3


class DbManagerold:
    def create_publischer_table(self):

        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
                Create Table IF NOT EXISTS PUBLISHERS (
                ID INTEGER primary key autoincrement,
                Name TEXT UNIQUE
                );"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def create_genres_table(self):

        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
                Create Table IF NOT EXISTS GENRES (
                ID INTEGER primary key autoincrement,
                Name TEXT UNIQUE
                );"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def create_platform_table(self):

        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
                Create Table IF NOT EXISTS PLATFORMS (
                ID INTEGER primary key autoincrement,
                Name TEXT UNIQUE
                );"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def create_games_table(self):

        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
                Create Table IF NOT EXISTS GAMES (
                ID integer primary key autoincrement,
                Name TEXT,
                Year INTEGER,
                GenreID INTEGER,
                PubID INTEGER,
                PlatformID INTEGER,
                NorthAmerica REAL,
                Europe REAL,
                Japan REAL,
                Rest REAL,
                Global REAL 
                );"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def delete_data_from_Database(self, event):
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """ SELECT Name from sqlite_sequence ;"""
        cursor.execute(sqltext)
        table = cursor.fetchall()
        table2 = list(map(lambda z: z[0], table))
        table2 = list(dict.fromkeys(table2))
        translation = {39: None}
        table2_length = len(table2)
        for i in range(table2_length):
            cursor = connection.cursor()
            sqltext = " DELETE FROM " + str(table2[i].translate(translation)) + " ; "
            cursor.execute(sqltext)
            connection.commit()
        connection.close()
