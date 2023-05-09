import tkinter

class MyGUI: 
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('My GUI')   
        self.win.geometry("300x200")
        tkinter.mainloop()

if __name__ == '__main__':
    myGUI = MyGUI()


