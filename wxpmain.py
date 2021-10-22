import wx

import addtodb
import pandacalculate

class MyFrame(wx.Frame):
    path = ""
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title='Projekt LF 8')
        self.sp = wx.SplitterWindow(self)
        self.panel1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.panel2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.sp.SplitVertically(self.panel1, self.panel2, 300)
        pdc = pandacalculate.PandaCalculate()
        wx.StaticText(self.panel1, label="Wähelen Sie eine CSV Datei aus", pos=(5,10), style=0, name="Header")
        wx.StaticText(self.panel1,label="Die Einbindung kann einige Minuten dauern.",pos=(5, 40), style=0, name="Header2")
        wx.StaticText(self.panel1, label="Bitte haben Sie etwas Geduld.",pos=(5, 70), style=0, name="Header3")
        wx.StaticText(self.panel1, label="Bitte Benutzen Sie nur die CSV Dateien die ihnen",pos=(5, 100), style=0, name="Header4")
        wx.StaticText(self.panel1,label="Mitgeliefert wurden oder gleich aufgebaute Dateien",pos=(5, 130), style=0, name="Header5")
        buttondd = wx.Button(self.panel1, label="CSV Datei in die Datebank einfügen", pos=(20,160))
        buttondd.Bind(wx.EVT_BUTTON, self.showfiledialog)
        buttondd.SetSize((230,25))
        wx.StaticText(self.panel1, label="Bitte wählen Sie eine Analyse aus", pos=(5, 200), style=0, name="Header4")
        button_top10_sales = wx.Button(self.panel1, label="Top 5 verkaufte Spiele", pos=(20, 240))
        button_top10_sales.Bind(wx.EVT_BUTTON, pdc.top_5_sold_Games)
        button_top10_sales.SetSize((230,25))
        button_sales_genre = wx.Button(self.panel1, label="Verkäufe nach Genre in %", pos=(20, 280))
        button_sales_genre.Bind(wx.EVT_BUTTON, pdc.sales_genre)
        button_sales_genre.SetSize((230,25))
        button_sales_platform = wx.Button(self.panel1, label="Verkäufe nach Platform in %", pos=(20, 320))
        button_sales_platform.Bind(wx.EVT_BUTTON, pdc.sales_platform)
        button_sales_platform.SetSize((230,25))
        button_sales_top10_pub = wx.Button(self.panel1, label="Top 5 Publischer", pos=(20, 360))
        button_sales_top10_pub.Bind(wx.EVT_BUTTON, pdc.top_5_publisher)
        button_sales_top10_pub.SetSize((230,25))
        button_sales_top5_region = wx.Button(self.panel1, label="Verkäufe nach Region der Top 5 Spiele", pos=(20, 400))
        button_sales_top5_region.Bind(wx.EVT_BUTTON, pdc.sales_region_top5)
        button_sales_top5_region.SetSize((230,25))
        button_sales_region = wx.Button(self.panel1, label="Verkäufe nach Region", pos=(20,440))
        button_sales_region.Bind(wx.EVT_BUTTON,pdc.sales_region)
        button_sales_region.SetSize((230,25))
        buttonQuit = wx.Button(self.panel1, label="Beenden", pos=(20, 600))
        buttonQuit.Bind(wx.EVT_BUTTON, self.onQuit)
        buttonQuit.SetSize((230,25))
        self.Show()
        self.Maximize(True)

    def onQuit(self, event):

        self.Close()

    def changeCursor(self, event):
        myCursor = wx.Cursor(wx.CURSOR_WAIT)
        self.SetCursor(myCursor)

    def showfiledialog(self, event):
        dlg = wx.FileDialog(parent=None,message= "", defaultDir= "",style= wx.FD_DEFAULT_STYLE)

        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
            self.addToDb(self.path)

        else:
            self.path = ''

        dlg.Destroy()
        #print(self.path)
        event.Skip()

    def addToDb(self, path):
        ps4= addtodb.DbManager()
        ps4.addSalestoDb(path)