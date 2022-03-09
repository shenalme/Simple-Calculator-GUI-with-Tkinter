from tkinter import *
root = Tk()
root.title("Calculator")
root.configure(bg="Black")

e = Entry(root)
e.configure(bg="#f2f5fc")
e.grid(row=0, column=0, columnspan=4, ipadx=50, ipady=20, padx=10, pady=10)


def click_me(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def addition():
    global first_number
    global math
    math = "Addition"
    first_number = e.get()
    e.delete(0, END)


def subtraction():
    global first_number
    global math
    math = "Subtraction"
    first_number = e.get()
    e.delete(0, END)


def multiplication():
    global first_number
    global math
    math = "Multiplication"
    first_number = e.get()
    e.delete(0, END)


def division():
    global first_number
    global math
    math = "Division"
    first_number = e.get()
    e.delete(0, END)


def equal():
    sec_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, int(first_number) + int(sec_number))

    elif math == "Subtraction":
        e.insert(0, int(first_number) - int(sec_number))

    elif math == "Multiplication":
        e.insert(0, int(first_number) * int(sec_number))

    elif math == "Division":
        e.insert(0, int(first_number) / int(sec_number))


# creating Buttons
b9 = Button(root, text="9", bg="#18191c", fg="White", command=lambda: click_me(9))
b8 = Button(root, text="8", bg="#18191c", fg="White", command=lambda: click_me(8))
b7 = Button(root, text="7", bg="#18191c", fg="White", command=lambda: click_me(7))
b6 = Button(root, text="6", bg="#18191c", fg="White", command=lambda: click_me(6))

b5 = Button(root, text="5", bg="#18191c", fg="White", command=lambda: click_me(5))
b4 = Button(root, text="4", bg="#18191c", fg="White", command=lambda: click_me(4))
b3 = Button(root, text="3", bg="#18191c", fg="White", command=lambda: click_me(3))
b2 = Button(root, text="2", bg="#18191c", fg="White", command=lambda: click_me(2))
b1 = Button(root, text="1", bg="#18191c", fg="White", command=lambda: click_me(1))
b0 = Button(root, text="0", bg="#18191c", fg="White", command=lambda: click_me(0))

bAdd = Button(root, text="+", bg="#18191c", fg="White", command=addition)
bSub = Button(root, text="-", bg="#18191c", fg="White", command=subtraction)
bMul = Button(root, text="*", bg="#18191c", fg="White", command=multiplication)
bdiv = Button(root, text="/", bg="#18191c", fg="White", command=division)
bequal = Button(root, text="=", bg="#18191c", fg="White", command=equal)
bclear = Button(root, text="Clear", bg="#18191c", fg="White", command=clear)

# putting the Widgets on the Window
b9.grid(row=1, column=0, ipadx=20, ipady=20)
b8.grid(row=1, column=1, ipadx=20, ipady=20)
b7.grid(row=1, column=2, ipadx=20, ipady=20)
b6.grid(row=1, column=3, ipadx=20, ipady=20)

b5.grid(row=2, column=0, ipadx=20, ipady=20)
b4.grid(row=2, column=1, ipadx=20, ipady=20)
b3.grid(row=2, column=2, ipadx=20, ipady=20)
b2.grid(row=2, column=3, ipadx=20, ipady=20)

b1.grid(row=3, column=0, ipadx=20, ipady=20)
bAdd.grid(row=3, column=1, ipadx=20, ipady=20)
bSub.grid(row=3, column=2, ipadx=20, ipady=20)
bMul.grid(row=3, column=3, ipadx=20, ipady=20)

bdiv.grid(row=4, column=0, ipadx=20, ipady=20)
bequal.grid(row=4, column=1, ipadx=20, ipady=20)
bclear.grid(row=4, column=2, ipadx=10, ipady=20)
b0.grid(row=4, column=3, ipadx=20, ipady=20)

root.mainloop()
