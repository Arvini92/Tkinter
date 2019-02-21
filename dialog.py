from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser


messagebox.showinfo(title = 'A Friendly Message', message = 'Hello, Tkinter!')

messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?')

filename = filedialog.askopenfile()
print(filename.name)

colorchooser.askcolor(initialcolor = '#FFFFFF')