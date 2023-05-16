#Julie's Party Hire

import tkinter as tk
from tkinter import *
from tkinter import font

#from PIL import Image, #still comes out yellow

win = tk.Tk()
win.title("Julie's Hire Party")
win.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
win.minsize(height=450,width=500)

style1 = font.Font(size=25)
style2 = font.Font(size=20)
style3 = font.Font(size=15)


# Window 1 - Opening Window

def window_1():
    label1=Label(window_1, text="Welcome to...", font=("Century Gothic",35))
    label1.pack(relx= 0.0, rely = 0.0,  anchor = 'nw')
    button1=Button(window_1,text='Proceed',command=lambda: window_2.tkraise(), font=style2)
    button1.pack(side=BOTTOM)
    
    #Images - 21-25
    party_Rentals = tk.PhotoImage(file = "julies_party_rentals.png")
   
    label2 = Label(win, image = party_Rentals)
    
    label2 = Label(win, image= party_Rentals, bd=3, relief="sunken")
    
    label2.pack(padx=20, pady=75 )
    
    
    def window_2():#page 2
        
        label1.destroy()
        button1.destroy()
        label3= Label(window_2,text="Julie's Party Hire", font=('Century Gothic',15))
        button3 = Button(window_2, text='Exit', font=('Century Gothic',15),command=back)
        label3.pack()
        button3.pack(side=RIGHT)
        def back():
            label3.destroy()
            button3.destroy()
window_1()
root.mainloop()