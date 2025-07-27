from tkinter import *
def check_strenght():
    password = entry.get()
    if len(password) < 6:
        result_label.config(text="Weak")
    elif len(password) <= 10:
        result_label.config(text="Medium")
    else:
        result_label.config(text= "Strong")

root = Tk()
root.title("Password Checker")

Label(root, text="Enter Password:").pack()
entry = Entry(root, show="*")
entry.pack()
Button(root, text="Check Strength", command=check_strenght).pack()
result_label = Label(root, text="")
result_label.pack()
root.mainloop()
    