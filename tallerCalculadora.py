from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def btnLimpiarTexto():
    global operator
    operator=""
    text_Input.set("")
def botonIgual():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
cal= Tk()
cal.title("CALCULADORA")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right').grid(columnspan=4)

#================================================================================
btn7=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="7", bg="blue", command=lambda:btnClick(7)).grid(row=1, column=0)

btn8=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="8", bg="blue", command=lambda:btnClick(8)).grid(row=1, column=1)

btn9=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="9", bg="blue", command=lambda:btnClick(9)).grid(row=1, column=2)

Suma=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="+", bg="blue", command=lambda:btnClick("+")).grid(row=1, column=3)
#================================================================================
btn4=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="4", bg="blue", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="5", bg="blue", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="6", bg="blue", command=lambda:btnClick(6)).grid(row=2, column=2)
Resta=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="-", bg="blue", command=lambda:btnClick("+")).grid(row=2, column=3)
#================================================================================
btn1=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="1", bg="blue", command=lambda:btnClick(1)).grid(row=3, column=0)

btn2=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="2", bg="blue", command=lambda:btnClick(2)).grid(row=3, column=1)