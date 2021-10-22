class DbRequests:
    def readfromdatabase(self):
        import sqlite3
        verbindung = sqlite3.connect("gamesales.db")
        zeiger = verbindung.cursor()
        zeiger.execute("SELECT * FROM ps4Genre")
        inhalt = zeiger.fetchall()
        print(inhalt)
        verbindung.close()

    def showcolumns(self):
        import sqlite3
        verbindung = sqlite3.connect("gamesales.db")
        zeiger = verbindung.cursor()
        zeiger.execute("PRAGMA table_info(ps4Genre);")
        inhalt = zeiger.fetchall()
        print(inhalt)
        verbindung.close()