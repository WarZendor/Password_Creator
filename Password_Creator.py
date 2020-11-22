#imports

import random, tkinter
from tkinter import simpledialog,messagebox

asci = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"

#window using tkinter

window = tkinter.Tk()
window.title("Password Creator")
window.geometry("500x500")
window.withdraw()

a = simpledialog.askinteger("Password Creator",window)

counter = 0
password = ""

while counter<a:
    c = random.randint(0,62)
    password+=asci[c]
    counter+=1
messagebox.showinfo("Password Creator",password)