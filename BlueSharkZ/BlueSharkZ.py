import tkinter as tk
from tkinter import *

class Seite1():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='')
        label.pack(side='top', fill='both', expand='True')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        feld = tk.Canvas(self.s1_rahmen, width=1000, height=1000)

        feld.pack(fill="both", expand=True)

        purple_dreieck = feld.create_polygon(0,0,0,1000,1000,1000, fill='darkorchid1')
        royal_dreieck = feld.create_polygon(1000,1000,1000,0,0,0, fill='royalblue1')
    def show(self):
        self.s1_rahmen.lift()

class Seite2():
    def __init__(self, fenster, container):
        self.s1_rahmen = tk.Frame(fenster)
        label = tk.Label(self.s1_rahmen, text='')
        label.pack(side='top', fill='both', expand='True')
        self.s1_rahmen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    def show(self):
        self.s1_rahmen.lift()

def haupt_ansicht(fenster):
    buttonframe = tk.Frame(fenster)
    container = tk.Frame(fenster)
    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)

    s1 = Seite1(fenster, container)
    s2 = Seite2(fenster, container)

    b1 = tk.Button(buttonframe, text="BlueSharkZ Encyption", command=s1.show)
    b2 = tk.Button(buttonframe, text="BluesharkZ Decryption 2", command=s2.show)

    b1.pack(side="left")
    b2.pack(side="left")

    s1.show()

fenster = tk.Tk()

fenster.geometry("1000x1000")

fenster.title('BlueSharkZ')
bild = tk.PhotoImage(file='')
e = Entry(fenster, width=50)
e.pack()
e.insert(0, '')

def Klick():
    hallo = 'Your Encrypted Code is: ' + e.get()
    meinlabel = Label(fenster, text=hallo)
    meinlabel.pack()

myButton = Button(fenster, text='Gib hier was ein', command=Klick)
myButton.pack()

haupt_ansicht(fenster)


fenster.mainloop()