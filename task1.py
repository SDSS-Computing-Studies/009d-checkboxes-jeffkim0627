#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *




def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal

    
    if binary[0] == 0:
        stan1 = 0 
    else :
        stan1 = 128
    if binary[1] == 0:
        stan2 = 0
    else:
        stan2 = 64
    if binary[2] == 0:
        stan3 = 0
    else:
        stan3 = 32
    if binary[3] == 0:
        stan4 = 0
    else:
        stan4 = 16
    if binary[4] == 0:
        stan5 = 0
    else:
        stan5 = 8
    if binary[5] == 0:
        stan6 = 0
    else:
        stan6 = 4
    if binary[6] == 0:
        stan7 = 0
    else:
        stan7 = 2
    if binary[7] == 0:
        stan8 = 0
    else:
        stan8 = 1    

    ans = stan1+stan2+stan3+stan4+stan5+stan6+stan7+stan8

    Entry1.delete(0,tk.END)
    Entry1.insert(0, ans)


def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    import math


    declist = list(str(format(decimal, '08b')))
    
    declist[0] = int(declist[0])
    declist[1] = int(declist[1])
    declist[2] = int(declist[2])
    declist[3] = int(declist[3])
    declist[4] = int(declist[4])
    declist[5] = int(declist[5])
    declist[6] = int(declist[6])
    declist[7] = int(declist[7])
    
    state1.set(declist[0])
    state2.set(declist[1])
    state3.set(declist[2])
    state4.set(declist[3])
    state5.set(declist[4])
    state6.set(declist[5])
    state7.set(declist[6])
    state8.set(declist[7])


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    decimal = int(Entry1.get())
    binary = decimal_to_binary(decimal)


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box

    st1=state1.get()
    st2=state2.get()
    st3=state3.get()
    st4=state4.get()
    st5=state5.get()
    st6=state6.get()
    st7=state7.get()
    st8=state8.get()

    binary = [st1, st2, st3, st4, st5, st6, st7, st8]
    decimal = binary_to_decimal(binary)



win = tk.Tk()

state1 = IntVar()
state1.set(1)
state2 = IntVar()
state2.set(1)
state3 = IntVar()
state3.set(1)
state4 = IntVar()
state4.set(1)
state5 = IntVar()
state5.set(1)
state6 = IntVar()
state6.set(1)
state7 = IntVar()
state7.set(1)
state8 = IntVar()
state8.set(1)

label1 = Label(win, text="Binary / Decimal Converter!")

b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)

cb1 = Checkbutton(win, text="", variable = state1)
cb2 = Checkbutton(win, text="", variable = state2)
cb3 = Checkbutton(win, text="", variable = state3)
cb4 = Checkbutton(win, text="", variable = state4)
cb5 = Checkbutton(win, text="", variable = state5)
cb6 = Checkbutton(win, text="", variable = state6)
cb7 = Checkbutton(win, text="", variable = state7)
cb8 = Checkbutton(win, text="", variable = state8)

Entry1 = Entry(win)


label1.grid(row=1, column=1, columnspan=8)

b1.grid(row=3, column=1, columnspan=4)
b2.grid(row=3, column=5, columnspan=8)

cb1.grid(row=2, column=1)
cb2.grid(row=2, column=2)
cb3.grid(row=2, column=3)
cb4.grid(row=2, column=4)
cb5.grid(row=2, column=5)
cb6.grid(row=2, column=6)
cb7.grid(row=2, column=7)
cb8.grid(row=2, column=8)

Entry1.grid(row=4, column=1, columnspan=8)



win.mainloop()