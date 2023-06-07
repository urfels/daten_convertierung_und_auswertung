import dbmanager
import wxpmain
import wx


p = dbmanager.DbManagerold()
p.create_platform_table()
p.create_genres_table()
p.create_publischer_table()
p.create_games_table()
# starting wx gui
app = wx.App()
frame = wxpmain.MyFrame()
app.MainLoop()


