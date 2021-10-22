class DbManagerold:
    def import_csv_in_database(self):
        import csv
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
        Create Table IF NOT EXISTS ps4sales (
        Game VARCHAR(30),
        Year INT,
        Genre VARCHAR(30),
        Publisher VARCHAR(30),
        NorthAmerica REAL,
        Europe REAL,
        Japan REAL,
        Rest REAL,
        Global REAL
        );"""
        cursor.execute(sqltext)

        sqltext = """
        INSERT INTO ps4sales (Game, Year, Genre, Publisher, NorthAmerica, Europe, Japan, Rest, Global)
        VALUES (:Game, :Year, :Genre, :Publisher, :NorthAmerica, :Europe, :Japan, :Rest, :Global)
        """
        with open("ps4sales.csv") as csvdata:
            csv_reader_object = csv.reader(csvdata, delimiter=',')
            with sqlite3.connect("gamesales.db") as con:
                cursor = con.cursor()
                cursor.executemany(sqltext, csv_reader_object)

    def import_xbox_csv_in_database(self):
        import csv
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
        Create Table IF NOT EXISTS xboxonesales (
        Position INT,
        Game VARCHAR(30),
        Year INT,
        Genre VARCHAR(30),
        Publisher VARCHAR(30),
        NorthAmerica REAL,
        Europe REAL,
        Japan REAL,
        Rest REAL,
        Global REAL
        );"""
        cursor.execute(sqltext)

        sqltext = """
        INSERT INTO xboxonesales ( Position, Game, Year, Genre, Publisher, NorthAmerica, Europe, Japan, Rest, Global)
        VALUES (:Position, :Game, :Year, :Genre, :Publisher, :NorthAmerica, :Europe, :Japan, :Rest, :Global)
        """
        with open("xboxonesales.csv") as csvdata:
            csv_reader_object = csv.reader(csvdata, delimiter=',')
            with sqlite3.connect("gamesales.db") as con:
                cursor = con.cursor()
                cursor.executemany(sqltext, csv_reader_object)

    def import_videogames_csv_in_database(self):
        import csv
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
        Create Table IF NOT EXISTS videogamesales (
        Game VARCHAR(30),
        Platform VARCHAR(30),
        Year INT,
        Genre VARCHAR(30),
        Publisher VARCHAR(30),
        NorthAmerica REAL,
        Europe REAL,
        Japan REAL,
        Rest REAL,
        Global REAL,
        CriticScore REAL,
        CriticCount REAL,
        UserScore VARCHAR(30),
        UserCount VARCHAR(30),
        Developer VARCHAR(30),
        Rating VARCHAR(30)
        );"""
        cursor.execute(sqltext)

        sqltext = """
        INSERT INTO videogamesales ( Game, Platform, Year, Genre, Publisher, NorthAmerica, Europe, Japan, Rest, Global, CriticScore, CriticCount, UserScore, UserCount, Developer, Rating)
        VALUES (:Game,:Platform,:Year,:Genre,:Publisher,:NorthAmerica,:Europe,:Japan,:Rest,:Global,:CriticScore,:CriticCount,:UserScore,:UserCount,:Developer,:Rating)
        """
        with open("videogamessales.csv") as cdata:
            csv_reader_object = csv.reader(cdata, delimiter=',')
            with sqlite3.connect("gamesales.db") as con:
                cursor = con.cursor()
                cursor.executemany(sqltext, csv_reader_object)

    def create_and_fill_ps4Publishertable(self):
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
            Create Table IF NOT EXISTS ps4Publisher (
            PubID integer primary key autoincrement,
            Publisher
            );"""
        cursor.execute(sqltext)
        sqltext = """
            INSERT INTO ps4Publisher (Publisher) SELECT DISTINCT Publisher FROM ps4sales
            ;"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def create_and_fill_ps4Genretable(self):
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
            Create Table IF NOT EXISTS ps4Genre (
            GenreID integer primary key autoincrement,
            Genre VARCHAR(30),
            );"""
        cursor.execute(sqltext)
        connection.commit()
        sqltext = """
            INSERT INTO ps4Genre (Genre) SELECT DISTINCT Genre FROM ps4sales
            ;"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

    def create_and_fill_ps4Gametable(self):
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
            Create Table IF NOT EXISTS ps4Game (
            GameID integer primary key autoincrement,
            Game VARCHAR(30)
            Year INT,
            GenreID INT,
            FOREIGN KEY (GenreID)
            REFERENCES ps4Genre (GenreID)
            PubID INT,
            FOREIGN KEY (PubID)
            REFERENCES ps4Publisher (PubID)
            NorthAmerica REAL,
            Europe REAL,
            Japan REAL,
            Rest REAL,
            Global REAL
            );"""
        cursor.execute(sqltext)
        connection.commit()
        sqltext = """
               INSERT INTO ps4Game (Game) SELECT Game FROM ps4sales
               ;"""
        cursor.execute(sqltext)
        connection.commit()
        sqltext = """
                   INSERT INTO ps4Game (Year) SELECT Year FROM ps4sales
                   ;"""
        cursor.execute(sqltext)
        sqltext = """
                   INSERT INTO ps4Game (GenreID) SELECT 
                   ;"""
        cursor.execute(sqltext)
        connection.commit()

        connection.close()

    def create_publischer_table(self):
        import sqlite3
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
        import sqlite3
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
        import sqlite3
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
        import sqlite3
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

    def create_sales_table(self):
        import sqlite3
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        sqltext = """
                Create Table IF NOT EXISTS SALES (
                GameID INTEGER primary key,
                NorthAmerica REAL,
                Europe REAL,
                Japan REAL,
                Rest REAL,
                Global REAL
                );"""
        cursor.execute(sqltext)
        connection.commit()
        connection.close()

