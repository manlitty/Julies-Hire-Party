# Julie's Party Hire

from tkinter import *
import tkinter as tk
from tkinter import ttk

root=Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=500,width=750)

def window_1():
    label1=Label(root, text="Welcome to...", font=("Century Gothic", 35))
    label1.place(relx= 0.0, 
                 rely = 0.0,    
                 anchor = 'nw')
    button1=Button(root,text='Proceed',font=('Catamaran',15))
    button1.pack(side='bottom')
    welcome=PhotoImage(file = 'C:\\Users\\super\\Downloads\\welcomeparty.png')
    label = ttk.Label(root, image = welcome)
    PhotoImage(file = 'C:\\Users\\super\\Downloads\\welcomeparty.png')
    label = Label(root, image=welcome, bd=5, relief="sunken")
    label.place()
    label.pack(padx=20, pady=75 )
    print(label)
    def window_2():#page 2
        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))
        button2 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label2.pack()
        button2.pack(side='right')
        def back():
            label2.destroy()
            button2.destroy()
window_1()
root.mainloop()