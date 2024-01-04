from tkinter import *

window = Tk()
window.title('Calculator')
window.resizable(False, False)
display_frame = LabelFrame(window, text='Selman Calculator', relief=SUNKEN, padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=4, padx=2, pady=4)
input_text = StringVar()
display = Entry(display_frame, textvariable=input_text, width=22, font=('arial', 18, 'normal'), bd=0, justify=RIGHT)
display.pack(ipady=12)


def button_press(num):
    global exp
    exp = input_text.get()
    exp = str(exp) + str(num)
    print(exp)
    input_text.set(exp)


def button_oper(oper):
    global exp
    exp = input_text.get()
    exp = str(exp) + str(oper)
    input_text.set(exp)


def clr_scr():
    global exp
    input_text.set("")
    exp = ""


def equal(event):
    global display
    global exp
    global oper
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)

button_7 = Button(window, text=7, padx=33, pady=33, bg="red", command=lambda: button_press(7))
button_8 = Button(window, text=8, padx=33, pady=33, bg="red", command=lambda: button_press(8))
button_9 = Button(window, text=9, padx=33, pady=33, bg="red", command=lambda: button_press(9))
button_plus = Button(window, text='+', padx=33, pady=33, bg="red", command=lambda: button_oper('+'))
button_4 = Button(window, text=4, padx=33, pady=33, bg="red", command=lambda: button_press(4))
button_5 = Button(window, text=5, padx=33, pady=33, bg="red", command=lambda: button_press(5))
button_6 = Button(window, text=6, padx=33, pady=33, bg="red", command=lambda: button_press(6))
button_minus = Button(window, text='-', padx=33, pady=33, bg="red", command=lambda: button_oper('-'))
button_1 = Button(window, text=1, padx=33, pady=33, bg="red", command=lambda: button_press(1))
button_2 = Button(window, text=2, padx=33, pady=33, bg="red", command=lambda: button_press(2))
button_3 = Button(window, text=3, padx=33, pady=33, bg="red", command=lambda: button_press(3))
button_div = Button(window, text='/', padx=33, pady=33, bg="red", command=lambda: button_oper('/'))
button_equals = Button(window, text='=', padx=33, pady=33, bg="red", command=lambda: equal(""))
button_clear = Button(window, text='C', padx=33, pady=33, bg="red", command= clr_scr)
button_dot = Button(window, text='.', padx=33, pady=33, bg="red", command=lambda: button_press('.'))
button_multi = Button(window, text='*', padx=33, pady=33, bg="red", command=lambda: button_oper('*'))

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)
button_equals.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_dot.grid(row=4, column=2)
button_multi.grid(row=4, column=3)
window.mainloop()
