from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

style = ttk.Style()
style.theme_use('classic')

frame1 = ttk.Frame(root, padding=5)
frame1.grid()

button1 = ttk.Button(frame1, text='A')
button1.grid(row=0, column=0)

button2 = ttk.Button(frame1, text='B')
button2.state(['disabled'])
button2.grid(row=0, column=1)

root.mainloop()