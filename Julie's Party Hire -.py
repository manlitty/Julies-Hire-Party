#Julie's Party Hire
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox

root=Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=450,width=500)

image_references = []



# Window 1 - Opening Window

def window_1():
    def window_2():
        label1.destroy()
        button1.destroy()
        imagelabel.destroy()
        frame.destroy()
        for image_ref in image_references:
            image_ref.__del__()
        
        #Labels and buttons for 2nd Window
        label2=Label(root, text="WORK PLEASe", font=("Century Gothic", 25))
        label2.place(relx=.0, rely=0.0, anchor='nw')
        def back():
            label2.destroy()
            button2.destroy()
            window_1()
        button2=Button(root,text='Proceed', font=('Catamaran',15),command=back)
        button2.place(relx=1.0, rely=1.0, anchor='se')
    button1=Button(root,text='Proceed', font=('Catamaran',15))
    button1.place(relx=1.0, rely=1.0, anchor='se')
    #Window_1 Labels, Buttons etc.    
    label1=Label(root, text="Welcome to...", font=("Century Gothic", 25))
    label1.place(relx= 0.0, rely = 0.0)
    button1=Button(root,text='Proceed', font=('Catamaran',15),command=window_2,activebackground='blue')
    button1.place(relx=1.0, rely=1.0, anchor='se')


    #Images
    img = Image.open("C:\\Users\\super\\Downloads\\JULIES_HIRE_PARTY\\PROGRAM\\imagesss.png")
    img2 = img.resize((350,350), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    imagelabel = Label(root, image=photo)
    image_references.append(photo)
    imagelabel.place(x=100, y=100)
    #Framing for Image
    frame = Frame(root, highlightbackground='black', highlightthickness=2)
    frame.pack(pady=50)
    imagelabel2 = Label(frame, image=photo)
    imagelabel2.pack()
    
window_1()
root.mainloop()