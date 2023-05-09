import tkinter

class MyGUI: 
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('My GUI')   
        self.win.geometry("300x200")
        #add labels
        self.lblnumber1 = tkinter.Label(self.win, text="First Name")
        self.lblnumber1.pack()
        self.lblnumber2 = tkinter.Label(self.win, text="Last Name")
        self.lblnumber2.pack()
        self.lblnumber3 = tkinter.Label(self.win, text="Age")
        self.lblnumber3.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    myGUI = MyGUI()

