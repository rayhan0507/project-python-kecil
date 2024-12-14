import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('jam digital sederhana')

def time():
    waktu = strftime('%H:%M:%S %p')
    lbl.config(text=waktu)
    lbl.after(1000, time)

lbl = tk.Label(font=('calibri', 40, 'bold'), fg='white', bg='light blue')
lbl.pack(anchor='center')
time()
root.mainloop()