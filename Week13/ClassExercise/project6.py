import tkinter
import tkinter.messagebox

class MyGUI: 
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('My GUI')   
        self.win.geometry("300x200")
        self.top_frame = tkinter.Frame(self.win)
        self.mid_frame = tkinter.Frame(self.win)
        self.bottom_frame = tkinter.Frame(self.win)

        self.lblnumber1 = tkinter.Label(self.top_frame, text="Enter a distance in kilometers")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        self.lblnumber1.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to miles:")
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, text=self.value)
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        #add button
        self.button1 = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.button1.pack(side='left')
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.win.destroy)
        self.button2.pack(side='left')

        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #add button
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(miles)


        

if __name__ == '__main__':
    myGUI = MyGUI()

