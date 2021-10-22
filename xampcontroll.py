class XammpControler:
    def start_xampp(self):
        import os
        os.startfile(os.path.normpath('xampp/xampp_start.exe'))

    def end_xampp(self):
        import os
        os.startfile(os.path.normpath('xampp/xampp_stop.exe'))

    def connect_to_database(self):
        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE hallo123")