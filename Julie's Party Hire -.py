#Julie's Party Hire

from tkinter import *
import tkinter as tk
from tkinter import ttk

root=Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=450,width=500)

# Window 1 - Opening Window
def window_1():
    label1=Label(root, text="Welcome to...", font=("Century Gothic", 35))
    label1.place(relx= 0.0, 
                 rely = 0.0,    
                 anchor = 'nw')
    button1=Button(root,text='Proceed',font=('Catamaran',15), command=window_2)
    button1.pack(side='bottom')
    #Images - 21-25
    party_Rentals = tk.PhotoImage(file = 'C:\\Users\\super\\Downloads\\JULIES_HIRE_PARTY\\PROGRAM\\julies_party_rentals.png')
   
    label = Label(root, image = party_Rentals)
    
    label = Label(root, image= party_Rentals, bd=3, relief="sunken")
    
    label.pack(padx=20, pady=75 )
    
    
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