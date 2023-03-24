import tkinter as tk
from tkinter import messagebox
from tkinter import *

win = tk.Tk(className='Python Examples - Window')
win.geometry("300x200")
win.title("Sum and Average Calculator")
win.configure(bg='blue')

#add labels
lblnumber1 = tk.Label(win, text="Enter number 1").grid(column = 0, row = 0)
lblnumber2 = tk.Label(win, text="Enter number 2").grid(column = 0, row = 1)
lblnumber3 = tk.Label(win, text="Enter number 3").grid(column = 0, row = 2)

#add fields
num1 = tk.IntVar()
fieldnumber1 = tk.Entry(win, width= 12, textvariable= num1).grid(column = 1, row = 0)
num2 = tk.IntVar()
fieldnumber2 = tk.Entry(win, width= 12, textvariable= num2).grid(column = 1, row = 1)
num3 = tk.IntVar()
fieldnumber3 = tk.Entry(win, width= 12, textvariable= num3).grid(column = 1, row = 2)

def submit():
    text_file = open("Week6/ClassExercises/GUImath.txt", "w")
    #write to output file the numbers the user inputted
    text_file.write(f"Number 1:{num1.get()}\nNumber 2:{num2.get()}\nNumber 3:{num3.get()}\n")
    sum = num1.get() + num2.get() + num3.get()
    avg = sum /3
    text_file.write(f"Sum:{sum}\nAverage:{avg}")
    messagebox.showinfo("information", f"Sum: {sum}\n Average: {avg}")

#button submit and create output file
btnSubmit = tk.Button(win, text="Submit", command = submit).grid(column = 0, row = 4)

win.mainloop()
