import tkinter
import tkinter.messagebox

class MyGUI: 
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('My GUI')   
        self.win.geometry("300x200")

        #add button
        self.button1 = tkinter.Button(self.win, text='Click Me', command=self.do_something)
        self.button1.pack()

        #add button
        self.button2 = tkinter.Button(self.win, text='Quit', command=self.win.destroy)
        self.button2.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')


        

if __name__ == '__main__':
    myGUI = MyGUI()

