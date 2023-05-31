from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re


root = Tk()
root.title("Julie's Hire Party") # Title
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico') # Icon top left of the program
root.minsize(height=450, width=380) # Size of Program

image_references = [] # frame and images
count = 0 # used to add rows

# Window 1 - Opening Window

def window_1():

    def window_2(): # Window 2
        label1.destroy()  # destroys Label1
        button1.destroy()  # destroy button from window 1
        imagelabel.destroy()  # destroy image label from window 1
        frame.destroy()  # destroys framing from window 1
        text.destroy() # destroys text credit

        # Delete Startup Image
        for image_ref in image_references:
            image_ref.__del__()
            
        #Restricts user to type decimal numbers (Entry 4 only)
        def validate_entry(text):
            if text.isdigit() or text == "":
                return True
            return False
        
        def validate_entry_no_decimal(P):
            if P.isdigit() or P == "":
                return True
            elif "." in P:
                return False
            return True
        
        #Restricts user to type numbers from Entry 1-3
        def validate_input(text):
            return not any(char.isdigit() or char == '.' for char in text)

        # Entry Widgets + Buttons
        L1 = Label(text="What's Your Name?:", font=40)
        L1.grid(row=0, column=0, sticky="w", pady=(10, 0))  
        E1 = Entry(root, bg="#f4f3f8", validate="key")
        E1.configure(validatecommand=(root.register(validate_input), '%P'))
        E1.grid(row=1, column=0, padx=(0, 45), sticky="w")

        L2 = Label(text="Your Receipt Number:", font=10)
        L2.grid(row=2, column=0, padx=(0, 30), sticky="w", pady=(10, 0))  

        E2 = Entry(root, bg="#f4f3f8")
        E2.grid(row=3, column=0, padx=(0, 45), sticky="w")
        E2['validatecommand'] = (root.register(validate_entry), '%P')
        E2['validate'] = 'key'

        L3 = Label(text="Name of Items Hired:", font=40)
        L3.grid(row=4, column=0, padx=(0, 50), sticky="w", pady=(10, 0))  

        E3 = Entry(root, bg="#f4f3f8", validate="key")
        E3.configure(validatecommand=(root.register(validate_input), '%P'))
        E3.grid(row=5, column=0, padx=(0, 45), sticky="w")

        L4 = Label(text="Number of Items Hired:", font=20)
        L4.grid(row=6, column=0, padx=(0, 50), sticky="w", pady=(10, 0))

        E4 = Entry(root, bg="#f4f3f8")
        E4.grid(row=7, column=0, padx=(0, 45), sticky="w")
        E4['validatecommand'] = (root.register(validate_entry), '%P')
        E4['validate'] = 'key'

        

        # Save Changes
        def save_changes():
            global count
            name = E1.get()
            receipt_number = E2.get()
            item_name = E3.get()
            item_quantity = E4.get()
            
            if name and receipt_number and item_name and item_quantity:
                item_id = count + 1
                values = (item_id, name, receipt_number, item_quantity, item_name)
                my_tree.insert(parent='', index='end', iid=item_id, text=item_id, values=values)
                count += 1

            # Clear Logs
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)

        # Save button
        save = Button(root, text="Save Changes", command=save_changes)
        save.grid(row=8, column=0, pady=(20,0), sticky="w") 

        # Return all function
        def return_all():
            for changes in my_tree.get_children():
                my_tree.delete(changes)
            
        #Return All button
        
        return_all = Button(root, text="Return all", command=return_all)
        return_all.grid(row=8, column=0, pady=(20,0), padx=(85,0), sticky="w" )
                
        # Using Treeview Widget 
        my_tree = ttk.Treeview(root)
        my_tree['columns'] = ("Row_#", "Your_Name", "Reciept_Number", "Item_Number_Hired", "Item_Hired")
        
        # Treeview Column
        my_tree.column("#0", width=0, stretch=NO)  # Hide the default first column
        my_tree.column("Row_#", anchor=CENTER, width=80)
        my_tree.column("Your_Name", anchor=W, width=140)
        my_tree.column("Reciept_Number", anchor=CENTER, width=120)
        my_tree.column("Item_Number_Hired", anchor=CENTER, width=150)
        my_tree.column("Item_Hired", anchor=W, width=200)

        #Treeview Headers
        my_tree.heading("#0", text="", anchor=CENTER)  # Hide the default first column
        my_tree.heading("Row_#", text="Row No.", anchor=CENTER)
        my_tree.heading("Your_Name", text="Customer Name", anchor=CENTER)
        my_tree.heading("Reciept_Number", text="Receipt No.", anchor=CENTER)
        my_tree.heading("Item_Number_Hired", text="No. of Items Hired", anchor=CENTER)
        my_tree.heading("Item_Hired", text="Item Name", anchor=CENTER)
        my_tree.grid(row=9, column=0, columnspan=100)
        
        
        #User delete individual row
        def delete_row(event):
            selected_item = my_tree.selection()
            if selected_item:
                 my_tree.delete(selected_item)
                 
        
        # Bind double-click event to remove a treeview row
        my_tree.bind("<Double-1>", delete_row)   
        
        #LOGO IMAGE TOP RIGHT
        img4 = Image.open("C:\\Users\\super\\Downloads\\JULIES_HIRE_PARTY\\PROGRAM\\imagesss.png")
        img4 = img4.resize((330, 250), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(img4)
        imagelabel2 = Label(root, image=photo2)
        image_references.append(photo2)
        imagelabel2.place(x=350, y=0)  # Position the photo in the top-right corner
        

        # Destroy Program Function
        def close():
            root.destroy()

        button2 = Button(root, text='Exit', font=('Catamaran', 15), command=close)
        button2.grid(row=10, column=0, sticky="sw")

    # Window_1 Labels, Buttons etc.
    label1 = Label(root, text="Welcome to...", font=("Century Gothic", 25))
    label1.grid(row=0, column=0)

    button1 = Button(root, text='Proceed', font=('Catamaran', 15), command=window_2, activebackground='blue')
    button1.grid(row=5, column=0, pady=20, sticky="e")

    # Images - Window 1
    img = Image.open("C:\\Users\\super\\Downloads\\JULIES_HIRE_PARTY\\PROGRAM\\imagesss.png")
    img2 = img.resize((350, 350), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    imagelabel = Label(root, image=photo)
    image_references.append(photo)


    # Framing for Image - Window 1
    frame = Frame(root, highlightbackground='black', highlightthickness=2)
    frame.grid(row=2, column=0, pady=10)
    imagelabel2 = Label(frame, image=photo)
    imagelabel2.pack()
    
    #Text Credits
    text = Label(root, text='Credits to: https://www.facebook.com/juliespartyrentals/', font=('Catamaran', 10, 'italic'))
    text.grid(row=2, column=0, sticky='sw', padx=10, pady=20)


window_1()
root.mainloop()