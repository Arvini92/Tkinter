from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello, Tkinter")
label.pack()
label.config(text = 'Push me')
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = "Howdy, TKinter!")
logo = PhotoImage(file= 'python_logo.gif')
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')
label.img = logo
label.config(image = label.img)




root.mainloop()