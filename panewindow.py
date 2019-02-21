from tkinter import *
from tkinter import ttk

root = Tk()
panewindow = ttk.PanedWindow(root, orient = HORIZONTAL)
panewindow.pack(fill = BOTH, expand = True)
frame1 = ttk.Frame(panewindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panewindow, width = 400, height = 400, relief = SUNKEN)
panewindow.add(frame1, weight = 1)
panewindow.add(frame2, weight = 4)
frame3 = ttk.Frame(panewindow, width = 50, height = 400, relief = SUNKEN)
panewindow.insert(1, frame3)
panewindow.forget(1)

root.mainloop()