import wx

class StatusBar(wx.StatusBar):
    def __init__(self, parent):
        super(StatusBar, self).__init__(parent)

        self.SetFieldsCount(1)
        self.SetStatusText('Ready', 0)
