import tkinter as tk

root = tk.Tk()
root.title("Restaurant Bill")
root.geometry("300x400")


menu = {"Burger": 100, "Pizza": 250, "Pasta": 150}

vars = {}
qtys = {}

tk.Label(root, text="Menu", font=("Arial", 16)).pack()

# Menu items with checkboxes and quantity
for item, price in menu.items():
    var = tk.IntVar()
    qty = tk.StringVar(value="0")
    vars[item] = var
    qtys[item] = qty
    tk.Checkbutton(root, text=f"{item} - ₹{price}", variable=var).pack(anchor='w')
    tk.Entry(root, textvariable=qty, width=5).pack(anchor='w')

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

def calculate():
    total = 0
    for item in menu:
        if vars[item].get():
            qty = int(qtys[item].get())
            total += qty * menu[item]
    result.config(text=f"Total: ₹{total}")

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
