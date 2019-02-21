from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text = 'Click Me')
button.pack()
def callback():
    print("Clicked!")

button.config(command = callback)
button.invoke()
button.state(['disabled'])
button.instate(['disabled'])
button.state(['!disabled'])
logo = PhotoImage(file= 'python_logo.gif')
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

root.mainloop()