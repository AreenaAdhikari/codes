import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        dob = datetime.strptime(entry.get(), "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result.config(text=f"Age: {age} years")
    except :
        result.config(text="Enter date as DD/MM/YYYY")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter DOB (DD/MM/YYYY):").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=5)
result = tk.Label(root, text="")
result.pack()

root.mainloop()