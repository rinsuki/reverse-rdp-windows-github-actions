import wx

app = wx.App()

frame = wx.Frame(None)
sizer = wx.BoxSizer(wx.VERTICAL)

slider = wx.Slider(frame, style=wx.SL_AUTOTICKS)
sizer.Add(slider, flag=wx.GROW)
slider = wx.Slider(frame, style=wx.SL_AUTOTICKS)
slider.SetTickFreq(1)
sizer.Add(slider, flag=wx.GROW)
slider = wx.Slider(frame, style=wx.SL_AUTOTICKS)
slider.SetTickFreq(50)
sizer.Add(slider, flag=wx.GROW)

frame.SetSizer(sizer)
frame.Show()

app.MainLoop()