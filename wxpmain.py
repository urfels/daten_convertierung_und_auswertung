
import wx
import wx.lib.intctrl
import sqlite3
import addtodb
import pandacalculate
import matplotlib.pyplot as pyplot
import pandas as pandas
import dbmanager
import webbrowser




class MyFrame(wx.Frame):
    path = ""

    def __init__(self):

        y= 0
        # initialisierung der gui
        self.window = wx.Window.__init__(self, parent=None, title='Projekt LF 8')
        # split window
        self.sp = wx.SplitterWindow(self)
        # window split part 1
        self.panel1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        # window split part 2
        self.panel2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        # split of the window
        self.sp.SplitVertically(self.panel1, self.panel2, 300)
        self.panel2.SetBackgroundColour(wx.Colour(51, 204, 255))
        self.panel1.SetBackgroundColour(wx.Colour(51, 204, 255))
        pdc = pandacalculate.PandaCalculate()
        dbmo = dbmanager.DbManagerold()
        wx.StaticText(self.panel1, label="Wähelen Sie eine CSV Datei aus", pos=(5, 10), style=0, name="Header")
        wx.StaticText(self.panel1, label="Die Einbindung kann einige Minuten dauern.", pos=(5, 40), style=0,
                      name="Header2")
        wx.StaticText(self.panel1, label="Bitte haben Sie etwas Geduld.", pos=(5, 70), style=0, name="Header3")
        wx.StaticText(self.panel1, label="Bitte Benutzen Sie nur die CSV Dateien die ihnen", pos=(5, 100), style=0,
                      name="Header4")
        wx.StaticText(self.panel1, label="Mitgeliefert wurden oder gleich aufgebaute Dateien", pos=(5, 130), style=0,
                      name="Header5")
        buttondd = wx.Button(self.panel1, label="CSV Datei in die Datebank einfügen", pos=(20, 160))
        buttondd.Bind(wx.EVT_BUTTON, self.showfiledialog)
        buttondd.SetSize((230, 25))
        button_del_data = wx.Button(self.panel1, label="Lösche alle Daten aus DB", pos=(20, 200))
        button_del_data.Bind(wx.EVT_BUTTON, dbmo.delete_data_from_Database)
        button_del_data.SetSize(230, 25)
        wx.StaticText(self.panel1, label="Bitte wählen Sie eine Analyse aus", pos=(5, 240), style=0, name="Header4")
        button_top10_sales = wx.Button(self.panel1, label="Top 5 verkaufte Spiele", pos=(20, 280))
        button_top10_sales.Bind(wx.EVT_BUTTON, pdc.top_5_sold_Games)
        button_top10_sales.SetSize((230, 25))
        button_sales_genre = wx.Button(self.panel1, label="Verkäufe nach Genre in %", pos=(20, 320))
        button_sales_genre.Bind(wx.EVT_BUTTON, pdc.sales_genre)
        button_sales_genre.SetSize((230, 25))
        button_sales_platform = wx.Button(self.panel1, label="Verkäufe nach Platform in %", pos=(20, 360))
        button_sales_platform.Bind(wx.EVT_BUTTON, pdc.sales_platform)
        button_sales_platform.SetSize((230, 25))
        button_sales_top10_pub = wx.Button(self.panel1, label="Top 5 Publischer", pos=(20, 400))
        button_sales_top10_pub.Bind(wx.EVT_BUTTON, pdc.top_5_publisher)
        button_sales_top10_pub.SetSize((230, 25))
        button_sales_top5_region = wx.Button(self.panel1, label="Verkäufe nach Region der Top 5 Spiele", pos=(20, 440))
        button_sales_top5_region.Bind(wx.EVT_BUTTON, pdc.sales_region_top5)
        button_sales_top5_region.SetSize((230, 25))
        button_sales_region = wx.Button(self.panel1, label="Verkäufe nach Region", pos=(20, 480))
        button_sales_region.Bind(wx.EVT_BUTTON, pdc.sales_region)
        button_sales_region.SetSize((230, 25))

        read_me = wx.Button(self.panel1,label="Read Me", pos=(20,560))
        read_me.Bind(wx.EVT_BUTTON, self.open_read_me)
        read_me.SetSize((230,25))
        buttonQuit = wx.Button(self.panel1, label="Beenden", pos=(20, 600))
        buttonQuit.Bind(wx.EVT_BUTTON, self.onQuit)
        buttonQuit.SetSize((230, 25))
        self.Show()
        self.Maximize(True)
        # panel 2
        # connect to database
        connect = sqlite3.connect("gamesales.db")
        # get the table names of Databse
        cursor1 = connect.execute('''SELECT name FROM sqlite_sequence''')
        tables = cursor1.fetchall()
        tables2 = list(map(lambda z: z[0], tables))
        tables2 = list(dict.fromkeys(tables2))
        translation = {39: None}
        table2_length = len(tables2)
        self.boxes = {"item": [],
                      "table": [],
                      "name": [],
                      "join": [],
                      "barhname": []}

        self.combobox_list = []
        self.sales_list = ["keine"]
        self.axis_name_list = []
        self.groupby_list = ["keine"]
        self.select_list = {
            "column":[],
            "table":[]
        }
        self.headline = wx.StaticText(self.panel2,-1, label="Analyse Tool für Spiele Verkäufe", pos=(10, 10), name="Headline")
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        self.headline.SetFont(font)
        x = 20
        y = 40
        # get all informations from all tables from the database
        for i in range(table2_length):
            info = connect.execute('PRAGMA table_info(' + tables2[i] + ');').fetchall()

            for j in info:
                for u, item in enumerate(j):
                    # add the information to lists and dictonarys when datatype is Text
                    if item == "TEXT":
                        self.combobox_list.append(j[u - 1])
                        self.groupby_list.append(tables2[i]+"."+j[u-1])
                        self.select_list["column"].append(tables2[i] + "." + j[u - 1])
                        self.select_list["table"].append(tables2[i])

                    # add information to lists when datatype is integer and not ID in name
                    elif item == "INTEGER" and "ID" not in j[u-1]:
                        self.groupby_list.append(tables2[i] + "." + j[u - 1])
                        name= j[u - 1]
                        namename = tables2[i] + "." +j[u - 1]
                        tableint = tables2[i]
                        x,y,self.checkboxcol = self.add_content_to_lists(x=x,y=y,tabl= tableint, namename = namename)
                    # add informations to lists datatype is Real
                    elif item == "REAL":
                        name =  j[u - 1]
                        namename = "sum("+j[u-1]+")"
                        tabl= tables2[i]
                        x,y,self.checkboxcol = self.add_content_to_lists(x=x,y=y, tabl=tabl, namename=namename)
                        namename = j[u - 1]
                        x,y,self.checkboxcol = self.add_content_to_lists(x=x, y=y, tabl=tabl, namename=namename)

          #          # self.globals()["CheckBox"+str(i)+str(l)] = wx.CheckBox(self.panel2, label=str(tables2[i]+ ' : '#          # + l), pos=(x, y))
        x = 20
        y += 30
        # put all attributes from select list .column in a radioBox
        self.select_radiobox = wx.RadioBox(self.panel2, label="", pos=(x, y), majorDimension=6,
                                           choices=self.select_list["column"], size=[800, 50])
        y += 70
        x = 20
        self.distinctcheckbox = wx.CheckBox(self.panel2, label="Doppelnennungen unterdrücken (Distinct)", pos=(x, y))
        y += 30
        x = 20
        self.groupby_radiobox = wx.RadioBox(self.panel2, label= " Gruppiert nach: ", pos=(x,y),majorDimension=6, choices=self.groupby_list, size= [800,50])
        y += 70
        x = 20
        self.order = []
        self.radiobox = wx.RadioBox(self.panel2, label=" Ordnen nach: ", pos=(x, y), majorDimension=6, choices=self.sales_list, size= [800,80])

        y += 100
        x = 20
        self.labeltopinput = wx.StaticText(self.panel2, label=" Grafik nur für die besten folgender Anzahl erstellen(Top X): ", pos=(x, y),
                      style=0, name="Headline")

        x = 340
        y-= 5
        # int text input field
        self.topinput = wx.lib.intctrl.IntCtrl(self.panel2, pos=(x,y), allow_none=True, value=None, min=1)
        y += 65
        x = 20
        wx.StaticText(self.panel2, label="Wählen sie eine Darstellungsform aus:", pos=(x, y), style=0, name="Headline")
        x += 300
        axesname = wx.StaticText(self.panel2, label="Wählen Sie eine Achsen Beschriftung aus:", pos=(x, y), style=0,
                      name="Headline")
        axesname.Hide()
        x += 250
        wx.StaticText(self.panel2, label="Wählen Sie aus wonach der Piechart ausgerechnet werden soll:", pos=(x, y), style=0,
                      name="Headline")
        y += 30
        x = 20
        self.piechartcheckbox = wx.CheckBox(self.panel2, label='Tortendiagramm', pos=(x, y))
        self.piechartcheckbox.Bind(wx.EVT_CHECKBOX, self.set_bccb_false)
        x += 150
        self.barchartcheckbox = wx.CheckBox(self.panel2, label='Balkendiagramm', pos=(x, y))
        self.barchartcheckbox.Bind(wx.EVT_CHECKBOX, self.set_pccb_false)

        x += 150
        self.combobox = wx.ComboBox(self.panel2, choices=self.combobox_list, pos=(x, y))
        self.combobox.Hide()
        x += 250
        # drop down field
        self.combobox_pie = wx.ComboBox(self.panel2, choices=self.sales_list, pos=(x, y))

        y += 30
        x = 20
        # run funktion dynamic calculate when clicket
        self.calculatebutton = wx.Button(self.panel2, label='Berechnen', pos=(x, y))
        self.calculatebutton.Bind(wx.EVT_BUTTON, self.dynamic_calculate)
        self.calculatebutton.SetSize((230, 25))
        examplebutton1 = wx.Button(self.panel2, label='Muster Belegung 1', pos=(20,550))
        examplebutton1.Bind(wx.EVT_BUTTON, self.set_value_1)
        examplebutton1.SetBackgroundColour(wx.Colour(255, 255, 51))
        examplebutton1.SetSize((230, 25))
        examplebutton2 = wx.Button(self.panel2, label='Muster Belegung 2', pos=(20, 590))
        examplebutton2.Bind(wx.EVT_BUTTON, self.set_value_2)
        examplebutton2.SetBackgroundColour(wx.Colour(255, 255, 51))
        examplebutton2.SetSize((230, 25))
    # set checkboxen false when a nother is clicket so just one can be selected
    def set_bccb_false(self, event):
        self.barchartcheckbox.SetValue(False)

    def set_pccb_false(self, event):
        self.piechartcheckbox.SetValue(False)
    # creates a dynamic sql querry(panel2) and starts a window which gives the data back
    def dynamic_calculate(self, event):
        where = []
        column = []
        table = []
        barhname = []

        selectindex = self.select_radiobox.GetSelection()
        nameselect = self.select_list["column"][selectindex]
        tableselect = self.select_list["table"][selectindex]
        column.append(nameselect)
        wherequery = "PUBLISHERS.ID = GAMES.PubID" if nameselect == "PUBLISHERS.Name" else "GENRES.ID = Games.GenreID" if nameselect == "GENRES.Name" else "PLATFORMS.ID = Games.PlatformID" if nameselect == "PLATFORMS.Name" else None
        where_len = len(where)
        # creates where statement
        if wherequery != None:
            if where_len == 0:
                where.append("WHERE " + wherequery)
            else:
                where.append(wherequery)
        # creates table names for querry
        if tableselect not in table:
            table.append(tableselect)
        # read out checkboxes from list item
        for index, i in enumerate(self.boxes["item"]):
            # if checkbox is checked and adds values to lists
            if i.IsChecked():

                name = self.boxes["name"][index]
                tablename = self.boxes["table"][index]
                column.append(name)
                barname = self.boxes["barhname"][index]
                barhname.append(barname)
                if tablename not in table:
                    table.append(tablename)


        orderby = []
        orderindex = self.radiobox.GetSelection()
        nameorderby = self.sales_list[orderindex]
        if nameorderby != " ":
            orderby.append(" ORDER BY " + nameorderby)

        if self.distinctcheckbox.GetValue():
            distinct = " DISTINCT "
        else:
            distinct = " "

        groupbyindex = self.groupby_radiobox.GetSelection()
        namegrouby = self.groupby_list[groupbyindex]

        if namegrouby != " ":
            groupby = " GROUP BY "+ namegrouby+ " "

        else:
            groupby = " "
        # gets input of an integer to limit the rows of query output
        topnumber = self.topinput.GetValue()
        if topnumber == None or topnumber < 1:
            limit = " "
        else:
            limit = " DESC LIMIT " + str(topnumber) + " "

        connect = sqlite3.connect("gamesales.db")
        query = "SELECT " + distinct + " , ".join(column) + " from " + " , ".join(table) + " " + " and ".join(
            where) + " " + groupby + "".join(orderby) + limit + ";"
        # create the query with the variables
        sql_query = pandas.read_sql_query(
            "SELECT " + distinct + " , ".join(column) + " from " + " , ".join(table) + " " + " and ".join(
                where) + " " + groupby + "".join(orderby) + limit + ";", connect)
        combobox_selected = "Name"  #self.combobox.GetValue()
        combobox_pie_selected = self.combobox_pie.GetValue()
        # chose piechart or barchart depends wich is selected
        if self.barchartcheckbox.GetValue():
            x_list = sql_query[combobox_selected]
            ax = sql_query[[z for z in barhname]].plot(kind='barh', width=0.6)
            ax.set_yticklabels(x_list)
        if self.piechartcheckbox.GetValue():
            var = sql_query.groupby([combobox_selected]).sum().stack()
            temp = var.unstack()
            label_list = temp.index
            x_list = temp[combobox_pie_selected]
            type(temp)
            pyplot.axis("equal")
            pyplot.pie(x_list, labels=label_list, autopct='%1.0f%%', radius=1.3, labeldistance=1.1, pctdistance=0.8)

        pyplot.title('Benutzer Generierte Analyse', pad=30)
        pyplot.show()
    # close application
    def onQuit(self, event):

        self.Close()

    def add_content_to_lists(self,x,y, tabl, namename):
        name = namename
        # set checkbox and add values to dictionarie to get acces to variables later
        self.checkboxcol = wx.CheckBox(self.panel2, label=name, pos=(x, y))
        self.sales_list.append(name)
        self.boxes["item"].append(self.checkboxcol)
        self.boxes["table"].append(tabl)
        self.boxes["name"].append(name)
        self.boxes["barhname"].append(name)
        x += 160
        if x > 800:
            y += 30
            x = 20
        return x,y,self.checkboxcol
    # make cursor to a witing cursor
    def changeCursor(self, event):
        myCursor = wx.Cursor(wx.CURSOR_WAIT)
        self.SetCursor(myCursor)
    # opends a filedialog to add csv datas to the database
    def showfiledialog(self, event):
        dlg = wx.FileDialog(parent=None, message="", defaultDir="", style=wx.FD_DEFAULT_STYLE)

        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
            self.addToDb(self.path)

        else:
            self.path = ''

        dlg.Destroy()
        event.Skip()

    def addToDb(self, path):
        dbm = addtodb.DbManager()
        dbm.addSalestoDb(path)
    # opens the readme text
    def open_read_me(self, event):
        webbrowser.open("readme.txt")
    # not in use
    def on_error(self):
        msg = "Ein fehler ist aufgetreten"
        dlg = wx.MessageDialog(None, msg, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    # first pre selected query
    def set_value_1(self, event):
        self.checkboxcol.SetValue(True)
        self.select_radiobox.SetSelection(0)
        self.groupby_radiobox.SetSelection(1)
        self.radiobox.SetSelection(11)
        self.topinput.SetValue(5)
        self.barchartcheckbox.SetValue(True)
        self.piechartcheckbox.SetValue(False)
    # second pre selected query
    def set_value_2(self, event):
        self.checkboxcol.SetValue(True)
        self.select_radiobox.SetSelection(0)
        self.groupby_radiobox.SetSelection(1)
        self.radiobox.SetSelection(11)
        self.topinput.SetValue(5)
        self.combobox_pie.SetSelection(11)
        self.piechartcheckbox.SetValue(True)
        self.barchartcheckbox.SetValue(False)


