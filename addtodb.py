import wx


class DbManager:
    def addSalestoDb(self, path):

        import sqlite3
        import csv
        connection = sqlite3.connect("gamesales.db")
        cursor = connection.cursor()
        wx.BeginBusyCursor()
        with open(path) as csvdata:
            reader = csv.reader(csvdata, delimiter=",")
            is_first = True
            for i, line in enumerate(reader):
                if is_first == False:

                    token = line
                    tokenlen = len(token)

                    sqltext = """
                            INSERT OR IGNORE INTO PUBLISHERS (Name)
                            VALUES (?)
                            """

                    cursor = connection.cursor()
                    publischer = token[3] if tokenlen == 9 else token[4]

                    cursor.execute(sqltext,(publischer,))
                   # connection.commit()

                    sqltext = """
                            INSERT OR IGNORE INTO GENRES (Name)
                            VALUES (?)
                            """
                    cursor = connection.cursor()
                    genre = token[2] if tokenlen == 9 else token[3]
                    cursor.execute(sqltext, (genre,))
                   # connection.commit()

                    sqltext = """
                            INSERT OR IGNORE INTO PLATFORMS (Name)
                            VALUES (?)
                            """
                    cursor = connection.cursor()
                    platformname = "PS4" if tokenlen == 9 else "XOne" if tokenlen == 10 else token[1]
                    cursor.execute(sqltext, (platformname,))
                    connection.commit()
                    sqltext="SELECT ID FROM GENRES WHERE Name = ?"

                    cursor.execute(sqltext, (genre,))
                    genre_id = cursor.fetchone()

                    sqltext="SELECT ID FROM PUBLISHERS WHERE Name = ?"
                    cursor.execute(sqltext, (publischer,))
                    publisher_id = cursor.fetchone()

                    sqltext = "SELECT ID FROM PLATFORMS WHERE Name = ?"
                    cursor.execute(sqltext, (platformname,))
                    platform_id = cursor.fetchone()

                    sqltext = """
                            INSERT INTO GAMES (Name, Year, GenreID, PubID, PlatformID, NorthAmerica, Europe, Japan, Rest, Global)
                            VALUES (?,?,?,?,?,?,?,?,?,?)
                            """

                    cursor = connection.cursor()

                    name = token[0] if tokenlen == 9 else token[1] if tokenlen == 10 else token[0]
                    year = token[1] if tokenlen == 9 else token[2]
                    northamerica = token[4] if tokenlen == 9 else  token[5]
                    europe = token[5] if tokenlen == 9 else token[6]
                    japan = token[6] if tokenlen == 9 else token [7]
                    rest = token[7] if tokenlen == 9 else token[8]
                    glo = token[8] if tokenlen == 9 else token[9]

                    cursor.execute(sqltext, (name, year,genre_id[0],publisher_id[0],platform_id[0],northamerica,europe,japan,rest,glo))
                    connection.commit()

                else:
                    is_first = False

            connection.close()
            wx.EndBusyCursor()
