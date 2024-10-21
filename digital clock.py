import tkinter as tk
from time import strftime

root = tk.Tk()  # Correct capitalization for Tk()

root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p\n%D")  # Fixed format string
    label.config(text=string)
    label.after(1000, time)

# Fix capitalization of 'Label' (tk.label -> tk.Label)
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time() 

root.mainloop()