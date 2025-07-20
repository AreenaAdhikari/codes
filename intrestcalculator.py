import tkinter as tk
def calculate_interest():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())

        si = (p * r * t) / 100

        ci = p *  ((1  + r/100 ** t))- p
        
        label_result.config(text=f"Simple Interest: {si:.2f}\nCompound interest: {ci:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers. ")

root = tk.Tk()
root.title("Interest Calculator")
tk.Label(root, text="Principal (P):").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()
tk.Label(root, text="Rate of Interest (R):").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()
tk.Label(root, text="Time (T in years):").pack()
entry_time = tk.Entry(root)
entry_time.pack()
tk.Button(root, text="Calculator", command=calculate_interest).pack(pady=10)
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()

