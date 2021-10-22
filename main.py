import csvmanager
import dbmanager
import dbrequests
import wxpmain
import wx
p = dbmanager.DbManagerold()
p.create_platform_table()
p.create_genres_table()
p.create_publischer_table()
p.create_games_table()
#p.create_sales_table()
#import_csv_in_database()
#import_xbox_csv_in_database()
#import_videogames_csv_in_database()
#readfromdatabase()
#showcolumns()
#create_and_fill_ps4Publishertable()
#create_and_fill_ps4Genretable()

app = wx.App()
frame = wxpmain.MyFrame()
app.MainLoop()
