#Julie's Party Hire
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter

root=Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=450,width=500)

# Window 1 - Opening Window

def window_1():
    label1=Label(root, text="Welcome to...", font=("Century Gothic", 35))
    button1=Button(root,text='Proceed',font=('Catamaran',15))
    label1.place(relx= 0.0, rely = 0.0)
    button1=Button(root,text='Proceed',font=('Catamaran',15))
    button1.pack(side=BOTTOM)

    #Images - 21-25
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\super\\Downloads\\JULIES_HIRE_PARTY\\PROGRAM\\imagesss.png"))
    testlabel = Label(image=img)
    img = Image.resize((100,100), Image.ANTIALIAS)
    testlabel.pack()
    
    imagelabel = Label(root, image=img).place(x=100, y=200)


    def window_2():#page 2

        label1.destroy()
        button1.destroy()
        label2= Label(root,text='Night', font=('Century Gothic',15))
        button2 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label2.pack()
        button2.pack(side='right')
        label3= Label(root,text="Julie's Party Hire", font=('Century Gothic',15))
        button3 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label3.pack()
        button3.pack(side=RIGHT)
        def back():
            label2.destroy()
            button2.destroy()
            label3.destroy()
            button3.destroy()
            window_1()
window_1()
root.mainloop()