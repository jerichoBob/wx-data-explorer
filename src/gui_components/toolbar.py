import wx

class ToolBar:
    def __init__(self, toolbar):
        open_tool = toolbar.AddTool(wx.ID_OPEN, 'Open', wx.Bitmap('resources/icons/icons8-file-50.png'))
        save_tool = toolbar.AddTool(wx.ID_SAVE, 'Save', wx.Bitmap('resources/icons/icons8-save-50.png'))

        toolbar.Realize()

        toolbar.GetParent().Bind(wx.EVT_TOOL, toolbar.GetParent().OnOpen, id=wx.ID_OPEN)
        toolbar.GetParent().Bind(wx.EVT_TOOL, toolbar.GetParent().OnSave, id=wx.ID_SAVE)
