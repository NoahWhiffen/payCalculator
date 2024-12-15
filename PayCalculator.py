from tkinter import *
import os

root = Tk()
root.geometry("500x500")
root.title("Pay Calculator")

e1_label = Label(root, text= "Enter Hours Worked:", font=("Times New Roman", 12), width=15, borderwidth=5)
e1_label.grid(row=0, column=1, columnspan=1, padx=10,pady=10)
e1 = Entry(root, width=15, borderwidth =5)
e1.grid(row=0, column=2, columnspan=1, sticky="W", padx=10, pady=10)

e2_label = Label(root, text= "Enter Rate of Pay:", font=("Times New Roman", 12), width=15, borderwidth =5)
e2_label.grid(row=1, column=1, columnspan= 1, padx=10, pady=10)
e2 = Entry(root, width=15, borderwidth=5)
e2.grid(row=1, column=2, columnspan=1, sticky="W", padx=10, pady=10)

e3_label = Label(root, text="Pay =", font= ("Times New Roman", 12), width=10, borderwidth =5)
e3_label.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

Output = 0.0
    
def calc():    
    global Output
    h = float(e1.get())
    r = float(e2.get())
    if h <= 40.0:
        Output = ((h * r) * 0.85)
    elif h > 40.0:
        Output = ((h - 40.0) * (r * 1.5) + (40.0 * r) * 0.85)
    ans_label.configure(text= "$" + str(Output) + " Net Pay")
    



calculate = Button(root, text = "Press Me", font=("Times New Roman", 10), width=10, borderwidth=2, command=calc)
calculate.grid(row=3, column=2, columnspan=1, padx=10, pady=10)

ans_label = Label(root, text=("$" + str(Output) + " Net Pay"), font=("Times New Roman", 14), width=10, borderwidth=5)
ans_label.grid(row=2, column=2, columnspan=1, sticky="W", padx=15, pady=15)


root.mainloop()