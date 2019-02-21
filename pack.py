from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello, Tkinter", background = 'yellow')
label.pack(side = LEFT, anchor = 'nw')
print(label)
ttk.Label(root, text="Hello, Tkinter", background = 'blue').pack(fill =  BOTH, padx = 10, pady = 10)
ttk.Label(root, text="Hello, Tkinter", background = 'green').pack(fill =  BOTH, expand = True, ipadx = 10, ipady = 10)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()