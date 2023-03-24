import tkinter as tk
from tkinter import messagebox
from tkinter import *

win = tk.Tk(className='Python Examples - Window')
win.geometry("300x200")
win.title("Read Numbers from File")
win.configure(bg='blue')

def read():
    total = 0
    number_file = open("Week6/Homework/number.txt")

    for line in number_file:
        total += int(line)
        messagebox.showinfo("information", f"Adding {line}")
    messagebox.showinfo("information", f"Total: {total}")


#button to read existing file
btnSubmit = tk.Button(win, text="Read File", command = read).grid(column = 0, row = 0)

win.mainloop()
