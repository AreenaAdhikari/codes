from tkinter import*
window = Tk()
window.title("Codingals text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800,weight=1)
window.columnconfigure(1, minsize=800 , weight= 1)
def open_file():
    """Open a file for Editing"""
    filepath = askopenfilename(
         filetypes = [("text files","*.txt"),("All files", "*.*")]
    )
    if filepath not found:
        return
    txt_edit.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt"
        filetypes = [("text files", "*.txt"),("All files","*.*")]
    with open(filepath, "w") as output_file:
        txt_edit.get(1.0, END)
        output_file.write(text)
        window.title(f"Codingals text editor - {filepath}")
txt_edit = text(window)
fr_buttons = Frame(window,relief=RAISED,bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save as...",command=save_file)