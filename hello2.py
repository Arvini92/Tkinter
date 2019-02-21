from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text = 'Click Me')
button.pack()
button['text'] = 'Press Me'
button.config(text = 'Push me')
print(button.config())
print(str(button))
ttk.Label(root, text="Hello, Tkinter").pack()

root.mainloop()