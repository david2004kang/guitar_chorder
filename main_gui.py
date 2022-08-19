import wx

_title = "Hello World"

if __name__ == '__main__':
    app = wx.App()
    wx.Frame(None, title=_title).Show()
    app.MainLoop()