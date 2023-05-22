import wx
from gui_components.mainframe import MainFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title="wx-data-explorer")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        wx.InitAllImageHandlers()   
        return True

if __name__ == "__main__":
    app = MyApp() 
    app.MainLoop()


