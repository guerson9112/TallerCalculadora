from tkinter import *


def Suma():
    total = int(a.get()) + int(b.get())
    print(total)


    
    

tk=Tk()
valor1 = IntVar()
valor2 = IntVar()
a = Entry(tk, textvariable = valor1)
b = Entry(tk, textvariable = valor2)
a.pack()
b.pack()

suma= Button(tk, text="SUMA", command = Suma)
suma.pack()
