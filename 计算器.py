import tkinter as tk
from tkinter import *


def num():
    eq.set(eval(eq.get()))


win = tk.Tk()
win.geometry('400x500')
Label(win, text='计算器').pack()
eq = StringVar()
Entry(win, textvariable=eq).pack()
Button(win, text='=', command=num).pack()
win.mainloop()
