import wx
class MenuBar(wx.MenuBar):
    def __init__(self, frame):
        super(MenuBar, self).__init__()

        filemenu = wx.Menu()
        filemenu.Append(wx.ID_OPEN, '&Open', 'Open a file')
        filemenu.Append(wx.ID_SAVE, '&Save', 'Save a file')
        filemenu.Append(wx.ID_CLOSE, '&Quit', 'Quit app')

        self.Append(filemenu, '&File')

        frame.Bind(wx.EVT_MENU, frame.OnOpen, id=wx.ID_OPEN)
        frame.Bind(wx.EVT_MENU, frame.OnSave, id=wx.ID_SAVE)
        frame.Bind(wx.EVT_MENU, frame.OnQuit, id=wx.ID_CLOSE)
