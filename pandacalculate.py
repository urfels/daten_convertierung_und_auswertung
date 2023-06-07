import wx
import sqlite3
import matplotlib.pyplot as pyplot
import pandas as pandas


class PandaCalculate(wx.Panel):

    def sales_genre(self, event):


        connect = sqlite3.connect("gamesales.db")
        sql_query = pandas.read_sql_query( "SELECT GENRES.Name, GAMES.Global from GAMES, GENRES WHERE GENRES.ID = GAMES.GENREID GROUP BY GENREID;", connect)

        var = sql_query.groupby(['Name']).sum().stack()
        temp = var.unstack()
        type(temp)
        x_list = temp['Global']
        label_list = temp.index
        pyplot.axis("equal")
        pyplot.pie(x_list, labels=label_list, autopct='%1.0f%%', radius=1.3, labeldistance=1.1, pctdistance=0.8)
        pyplot.title('Absatz nach Genre in Mio', pad=30)
        pyplot.show()


    def sales_platform(self, event):

        connect = sqlite3.connect("gamesales.db")
        sql_query = pandas.read_sql_query(
            "SELECT PLATFORMS.Name, GAMES.Global from GAMES, PLATFORMS WHERE PLATFORMS.ID = GAMES.PLATFORMID GROUP BY PLATFORMS.Name;",
            connect)
        var = sql_query.groupby(['Name']).sum().stack()
        temp = var.unstack()
        type(temp)
        x_list = temp['Global']
        label_list = temp.index
        pyplot.axis("equal")
        pyplot.pie(x_list, labels=label_list, autopct='%1.0f%%', radius=1.3, labeldistance=1.1, pctdistance=0.8)
        pyplot.title('Absatz nach Platform in %', pad=30)
        pyplot.show()

    def top_5_sold_Games(self, event):

        connect = sqlite3.connect("gamesales.db")
        sql_query = pandas.read_sql_query(
            "SELECT DISTINCT Name, sum(Global) as 'Verkäufe' from GAMES GROUP BY Name  ORDER BY sum(GLOBAL) DESC LIMIT 5;",
            connect)
        x_list = sql_query['Name']
        ax = sql_query[['Verkäufe', 'Name']].plot(kind= 'barh', width=0.2)
        ax.set_yticklabels(x_list)
        pyplot.title('Top 5 der Verkauften Spiele in Mio', pad=30)
        pyplot.show()

    def top_5_publisher(self, event):

        connect = sqlite3.connect("gamesales.db")
        sql_query = pandas.read_sql_query(
            "SELECT DISTINCT PUBLISHERS.Name, sum(GAMES.Global) as 'Verkäufe' from PUBLISHERS, GAMES WHERE PUBLISHERS.ID = GAMES.PubID  GROUP BY PUBLISHERS.Name  ORDER BY sum(GLOBAL) DESC LIMIT 5;",
            connect)
        x_list = sql_query['Name']

        ax = sql_query[['Verkäufe', 'Name']].plot(kind='barh', width=0.2)
        ax.set_yticklabels(x_list)
        pyplot.title('Top 5 der Publisher nach Verkauf in Mio', pad=30)
        pyplot.show()

    def sales_region_top5(self, event):

        connect = sqlite3.connect("gamesales.db")
        sql_query = pandas.read_sql_query(
            "SELECT DISTINCT Name, sum(NorthAmerica) as 'Nord Amerika', sum(Europe) as 'Europa', sum(Japan) as 'Japan', sum(Rest) as 'Rest der Welt' from Games GROUP BY name ORDER BY SUM(GLOBAL) DESC LIMIT 5" ,
            connect)
        x_list = sql_query['Name']

        ax = sql_query.plot(kind='barh', width=0.6)
        ax.set_yticklabels(x_list)
        pyplot.title('Verkäufe nach Region der Top 5 Spiele', pad=30)
        pyplot.show()

    def sales_region(self, event):

            connect = sqlite3.connect("gamesales.db")
            sql_query = pandas.read_sql_query(
                "SELECT sum(NorthAmerica) as 'Nord Amerika', sum(Europe) as 'Europa', sum(Japan) as 'Japan', sum(Rest) as 'Rest der Welt' from Games;",
                connect)
            ax = sql_query.plot(kind='barh', width=0.6)
            pyplot.title('Verkäufe nach Region von allen Spielen', pad=30)
            pyplot.show()

