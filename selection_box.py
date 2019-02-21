from tkinter import *
from tkinter import ttk

root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar'))
month.get()
month.set('Dec')
month.set('Not a month')
print(month.get())
year = StringVar()

Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

root.mainloop()