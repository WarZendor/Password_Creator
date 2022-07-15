from random import randint
from tkinter import Tk,Entry, mainloop
asci = """!#()*+,-./0123456789<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]_abcdefghijkmnopqrstuvwxyz{}"""
root= Tk()
root.geometry('50x50')
password = ""
for i in range(12):
    c = randint(0,77)
    password+=asci[c]
e = Entry(root)
e.insert(0,password)
e.pack()
mainloop()
