# Julie's Party Hire

from tkinter import *
import tkinter as tk

root=Tk()
root.title("Julie's Hire Party")
root.minsize(height=500,width=750)

def window_1():
    label1=Label(root, text="Welcome to...", font=("Century Gothic", 35))
    button1=Button(root,text='Proceed',font=('Catamaran',15))
    button1.pack(side='bottom')
    def window_2():#page 2
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))
        button2 = Button(root, text='Exit', font=('Century Gothic',15))
        label2.pack()
        button2.pack(side='right')
window_1()
root.mainloop()