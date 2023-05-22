import wx
from wx import ID_OPEN, ID_SAVE, ID_EXIT
from .menubar import MenuBar
from .toolbar import ToolBar
from .statusbar import StatusBar

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(800,600))

        # Set the menu bar
        self.SetMenuBar(MenuBar(self))

        # Set the toolbar
        ToolBar(self.CreateToolBar())

        # Set the status bar
        StatusBar(self.CreateStatusBar())

        self.Show()

    def OnOpen(self, event):
        # Open a file dialog to choose a file to open
        with wx.FileDialog(self, "Open file", wildcard="All files (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                # Add your code here to open the file and do something with it
                print(f'Opening file at {pathname}')
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

    def OnSave(self, event):
        # Open a file dialog to choose a file to save
        with wx.FileDialog(self, "Save file", wildcard="All files (*.*)|*.*",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Save the current data to the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                # Add your code here to save your data to the file
                print(f'Saving to file at {pathname}')
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def OnQuit(self, event):
        # Close the application
        self.Close()

