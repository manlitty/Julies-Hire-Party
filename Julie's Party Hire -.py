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
root.minsize(height=450,width=650)

image_references = []



# Window 1 - Opening Window

def window_1():
    
    #Window 2
    
    def window_2():
        label1.destroy() #destroys Label1
        button1.destroy() #destroy button from window 1
        imagelabel.destroy() #destroy image label from window 1
        frame.destroy() # destroys framing from window 1
        
        #Delete Startup Image
        for image_ref in image_references:
            image_ref.__del__()
            
        #Entry Widgets
        L1 = Label(text="What's Your Name?:", font=40)
        L1.grid(row=0, column=0) 
        
        E1=Entry(root,bg="#f4f3f8")
        E1.grid(row=1, column=0, padx=(0,45))
        
        L2 = Label(text="Your Reciept Number:", font=10)
        L2.grid(row=2, column=0, padx=(0,30))
        
        E2=Entry(root,bg="#f4f3f8")
        E2.grid(row=3, column=0, padx=(0,45))
        
        L3 = Label(text="Name of Items Hired:", font=40)
        L3.grid(row=4, column=0, padx=(0,50))
        
        E3=Entry(root,bg="#f4f3f8")
        E3.grid(row=5, column=0, padx=(0,45))
        
        L4 = Label(text="Number of Items Hired:", font=20)
        L4.grid(row=6, column=0, padx=(0,50))
        
        E4=Entry(root,bg="#f4f3f8")
        E4.grid(row=7, column=0, padx=(0,45))
        

        #Using Treeview Widget
        #my_tree = ttk.Treeview(root, columns=("Row_#", "Your_Name", "Reciept_Number", "Item_Number_Hired", "Item_Hired")
                               #,show="headings")
        #my_tree.heading("Row_#", text="Row No.")
        #my_tree.heading("Your_Name", text="Customer Name")
        #my_tree.heading("Reciept_Number", text="Reciept no.")
        #my_tree.heading("Item_Number_Hired", text="No. of items hired")
        #my_tree.heading("Item_Hired", text="Item Name")
        #my_tree.grid(row=2, column=0, columnspan=100, padx=0, pady=100)
        
        
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