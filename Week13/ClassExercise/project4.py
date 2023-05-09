import tkinter

class MyGUI: 
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('My GUI')   
        self.win.geometry("300x200")
        #add labels
        self.lblnumber1 = tkinter.Label(self.win, text="If you do not think about your future, you cannot have one.")
        self.lblnumber1.pack(ipadx=20, ipady=20)
        self.lblnumber2 = tkinter.Label(self.win, text="Real happiness is cheap enough, yet how dearly we pay for its counterfeit.")
        self.lblnumber2.pack(ipadx=20, ipady=20)

        tkinter.mainloop()

if __name__ == '__main__':
    myGUI = MyGUI()

