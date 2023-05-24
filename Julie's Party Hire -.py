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
    #Window 2
    
    def window_2():
        label1.destroy()
        button1.destroy()
        imagelabel.destroy()
        frame.destroy()
        #Delete Startup Image
        for image_ref in image_references:
            image_ref.__del__()
        
        
        my_tree = ttk.Treeview(root, columns=("Row_#", "Your_Name", "Reciept_Number", "Item_Number_Hired", "Item_Hired")
                               ,show="headings")
        my_tree.heading("Row_#", text="Row No.")
        my_tree.heading("Your_Name", text="Customer Name")
        my_tree.heading("Reciept_Number", text="Reciept no.")
        my_tree.heading("Item_Number_Hired", text="No. of items hired")
        my_tree.heading("Item_Hired", text="Item Name")
        my_tree.grid(row=2, column=0, columnspan=100, padx=0, pady=100)
        
        

        
        
        #Define Columns
        
        
        #Columns
        
        #my_tree.column("Row #", width=120, minwidth=25)
        #my_tree.column("Your Name", anchor=E, width=120)
        #my_tree.column("Reciept Number", anchor=CENTER, width=100)
        #my_tree.column("Item Hired", anchor=W, width=120)
        #my_tree.column("How many Items have you hired?", anchor=CENTER, width=80)
        
        #Headings
        #my_tree.heading("Row #", text="Row", anchor=W)
        #my_tree.heading("Your Name", text="Name", anchor=W)
        #my_tree.heading("Reciept Number", text="Reciept no.", anchor=W)
        #my_tree.heading("Item Hired", text="Item name", anchor=CENTER)
        #my_tree.heading("How many Items have you hired?", text="Item No.", anchor=W)
        #Data
        
        
        #Labels and buttons for 2nd Window
        label2=Label(root, text="Fill in the required fields", font=("Century Gothic",20), fg="red")
        label2.place(relx=.0, rely=0.0, anchor='nw')
        
        #Destroy Program Function
        def close():
            root.destroy()
        button2=Button(root,text='Exit', font=('Catamaran',15),command=close)
        button2.place(relx=1.0, rely=1.0, anchor='se')
            
        
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