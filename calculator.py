from tkinter import *
import tkinter.font as font
from tkinter import messagebox

window = Tk()
window.title("Calculator")
window ['background'] = '#333333'
window.iconbitmap("dont_start_without_this.ico")

e = None

def entireprogram():
    global e
    e = Entry(window, width=26, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clearr():
        e.delete(0, END)

    def button_addd():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        e.delete(0, END)

    def button_substractt():
        first_number = e.get()
        global f_num
        global math
        math = "substraction"
        f_num = float(first_number)
        e.delete(0, END)

    def button_multipyy():
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        e.delete(0, END)

    def button_dividee():
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        e.delete(0, END)

    def button_powerr():
        first_number = e.get()
        global f_num
        global math
        math = "power"
        f_num = float(first_number)
        e.delete(0, END)

    def button_equall():
        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + float(second_number))
        elif math == "substraction":
            e.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            e.insert(0, f_num * float(second_number))
        elif math == "division":
            e.insert(0, f_num / float(second_number))
        elif math == "power":
            e.insert(0, f_num ** float(second_number))

    def exit_calculator():
        window.quit()
        messagebox.showinfo('Made by ZeaCeR#5641', 'Thanks for using this Calculator! Make sure to check my other projects!')


    # 10 number buttons
    button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#FF5733", fg="#FFFFFF")
    button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#FF5733", fg="#FFFFFF")
    button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#FF5733", fg="#FFFFFF")
    button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#FF5733", fg="#FFFFFF")
    button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#FF5733", fg="#FFFFFF")
    button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#FF5733", fg="#FFFFFF")
    button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#FF5733", fg="#FFFFFF")
    button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#FF5733", fg="#FFFFFF")
    button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#FF5733", fg="#FFFFFF")
    button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#C539B1", fg="#FFFFFF")
    # other buttons
    button_add = Button(window, text="+", padx=39, pady=20, command=button_addd, bg="#C539B1", fg="#FFFFFF")
    button_equal = Button(window, text="=", padx=94, pady=20, command=button_equall, bg="#00f636", fg="#000000")
    button_clear = Button(window, text="Clear", padx=78, pady=20, command=button_clearr, bg="#A20000", fg="#FFFFFF")
    button_substract = Button(window, text="-", padx=41, pady=20, command=button_substractt, bg="#C539B1", fg="#FFFFFF")
    button_multipy = Button(window, text="*", padx=45, pady=20, command=button_multipyy, bg="#C539B1", fg="#FFFFFF")
    button_divide = Button(window, text="/", padx=41, pady=20, command=button_dividee, bg="#C539B1", fg="#FFFFFF")
    button_power = Button(window, text="^", padx=40, pady=20, command=button_powerr, bg="#C539B1", fg="#FFFFFF")
    button_exit_program = Button(window, text="EXIT", padx=78, pady=20, command=exit_calculator)

    # row 1
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    # row 2
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    # row 3
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    # row 4
    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)

    # row 5
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    # row 6
    button_substract.grid(row=6, column=0)
    button_multipy.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    # row 7
    button_power.grid(row=7,column=0)
    button_exit_program.grid(row=7, column=1, columnspan=2)

    # button properties
    myFont = font.Font(family='Arial', size=14)

    button_1['font'] = myFont
    button_2['font'] = myFont
    button_3['font'] = myFont
    button_4['font'] = myFont
    button_5['font'] = myFont
    button_6['font'] = myFont
    button_7['font'] = myFont
    button_8['font'] = myFont
    button_9['font'] = myFont
    button_0['font'] = myFont

    button_add['font'] = myFont
    button_equal['font'] = myFont
    button_clear['font'] = myFont
    button_substract['font'] = myFont
    button_multipy['font'] = myFont
    button_divide['font'] = myFont
    button_power['font'] = myFont
    button_exit_program['font'] = myFont
    e['font'] = myFont


    window.mainloop()

# i barely hope this works
try:
    entireprogram()
except ValueError:
    e.delete(0, END)
    e.insert(0, "Not Valid")
    print("Not Valid")
except ZeroDivisionError:
    e.delete(0, END)
    e.insert(0, "Cannot Divide by 0")
    print("Cannot Divide by 0")
