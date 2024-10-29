from tkinter import *
from tkinter import *

from time import strftime

root = Tk()
root.title("Clock")
root.config(bg='black')

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

def date():
    string1 = strftime('%d/%b/%Y')
    label1.config(text=string1)
    label1.after(86400, date)

def day():
    string2 = strftime('%A')
    label2.config(text=string2)
    label2.after(86400, day)


label = Label(root,font=("ds-digital", 80), background= "black", foreground= "cyan")
label.pack(anchor='center')
time()

label1 = Label(root,font=("ds-digital", 20), background= "black", foreground= "cyan")
label1.pack(anchor='se')
date()

label2 = Label(root,font=("ds-digital", 20), background= "black", foreground= "cyan")
label2.pack(anchor='se')
day()

mainloop()