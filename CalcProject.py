from tkinter import *

#window
root=Tk()
root.geometry('381x265+0+0')
root.title('Calculator by Simple Coding Style')
root.resizable(False, False)
root.iconbitmap('Myneww.ico')

#function section

operator= ''

def Click(figures):
    global operator
    operator= operator+figures
    calcEntryField.delete(0, END) #to delete text from First to LAST
    calcEntryField.insert(END, operator) #to place my operation at the lefthand side and must my entered operator

def Clear():
    global operator #global helps to modify a variale inside a function.
    operator='' #is to absorb the figures or numbers and operator typed in.
    calcEntryField.delete(0, END) #to delete text from First to LAST

def Eval():
    global operator
    solution=str(eval(operator)) #evaluate our operations and give the result in a form of a string
    calcEntryField.delete(0, END) #delete the field after operations
    calcEntryField.insert(0, solution)




#calcEntryfield
calcEntryField=Entry(root,font=('ariel', 14, 'bold'), fg= 'floral white', bd=6, borderwidth=20, bg='black')
calcEntryField.grid(row=0, column=0,columnspan=4)


#buttons
button7=Button(root, text='7', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('7'))
button7.grid(row=1, column=0)

button8=Button(root, text='8', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('8'))
button8.grid(row=1, column=1)

button9=Button(root, text='9', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('9'))
button9.grid(row=1, column=2)

buttonAdd=Button(root, text='+', font=('ariel', 16, 'bold'), fg='black', bg='mediumturquoise', bd=6, width=6,
                 command=lambda:Click('+'))
buttonAdd.grid(row=1, column=3)

button4=Button(root, text='4', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('4'))
button4.grid(row=2, column=0)

button5=Button(root, text='5', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('5'))
button5.grid(row=2, column=1)

button6=Button(root, text='6', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('6'))
button6.grid(row=2, column=2)

buttoMinus=Button(root, text='-', font=('ariel', 16, 'bold'), fg='black', bg='mediumturquoise', bd=6, width=6,
                  command=lambda:Click('-'))
buttoMinus.grid(row=2, column=3)

button1=Button(root, text='1', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('1'))
button1.grid(row=3, column=0)

button2=Button(root, text='2', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('2'))
button2.grid(row=3, column=1)

button3=Button(root, text='3', font=('ariel', 16, 'bold'), fg='black', bg='floral white', bd=6, width=6,
               command=lambda:Click('3'))
button3.grid(row=3, column=2)

buttonMult=Button(root, text='*', font=('ariel', 16, 'bold'), fg='black', bg='mediumturquoise', bd=6, width=6,
                  command=lambda:Click('*'))
buttonMult.grid(row=3, column=3)

buttonClear=Button(root, text='C', font=('ariel', 16, 'bold'), fg='brown1', bg='floral white', bd=6, width=6,
                   command=Clear)
buttonClear.grid(row=4, column=0)

buttonEqual=Button(root, text='=', font=('ariel', 16, 'bold'), fg='black', bg='springgreen1', bd=6, width=6,
                   command=Eval)
buttonEqual.grid(row=4, column=1)

buttonZero=Button(root, text='0', font=('ariel', 16, 'bold'), fg='black', bg='mediumturquoise', bd=6, width=6,
                  command=lambda:Click('0'))
buttonZero.grid(row=4, column=2)

buttonDiv=Button(root, text='/', font=('ariel', 16, 'bold'), fg='black', bg='mediumturquoise', bd=6, width=6,
                 command=lambda:Click('/'))
buttonDiv.grid(row=4, column=3)


root.mainloop()
