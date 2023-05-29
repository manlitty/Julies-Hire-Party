from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=450, width=440)

image_references = []
count = 0

# Window 1 - Opening Window

def window_1():
    # Window 2

    def window_2():
        label1.destroy()  # destroys Label1
        button1.destroy()  # destroy button from window 1
        imagelabel.destroy()  # destroy image label from window 1
        frame.destroy()  # destroys framing from window 1

        # Delete Startup Image
        for image_ref in image_references:
            image_ref.__del__()

        # Entry Widgets + Buttons
        L1 = Label(text="What's Your Name?:", font=40)
        L1.grid(row=0, column=0, sticky="w")

        E1 = Entry(root, bg="#f4f3f8")
        E1.grid(row=1, column=0, padx=(0, 45), sticky="w")

        L2 = Label(text="Your Receipt Number:", font=10)
        L2.grid(row=2, column=0, padx=(0, 30), sticky="w")

        E2 = Entry(root, bg="#f4f3f8")
        E2.grid(row=3, column=0, padx=(0, 45), sticky="w")

        L3 = Label(text="Name of Items Hired:", font=40)
        L3.grid(row=4, column=0, padx=(0, 50), sticky="w")

        E3 = Entry(root, bg="#f4f3f8")
        E3.grid(row=5, column=0, padx=(0, 45), sticky="w")

        L4 = Label(text="Number of Items Hired:", font=20)
        L4.grid(row=6, column=0, padx=(0, 50), sticky="w")

        E4 = Entry(root, bg="#f4f3f8")
        E4.grid(row=7, column=0, padx=(0, 45), sticky="w")

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
        save.grid(row=8, column=0, pady=20)
        

        #Def remove
        def remove_all():
            for changes in my_tree.get_children():
                my_tree.delete(changes)
            
    
        #Remove all
        
        remove_all = Button(root, text="Remove all", command=remove_all)
        remove_all.grid(row=8, column=2 )
                
        # Using Treeview Widget
        my_tree = ttk.Treeview(root)
        my_tree['columns'] = ("Row_#", "Your_Name", "Reciept_Number", "Item_Number_Hired", "Item_Hired")
        
        my_tree.column("#0", width=0, stretch=NO)  # Hide the default first column
        my_tree.column("Row_#", anchor=CENTER, width=80)
        my_tree.column("Your_Name", anchor=W, width=140)
        my_tree.column("Reciept_Number", anchor=CENTER, width=120)
        my_tree.column("Item_Number_Hired", anchor=CENTER, width=150)
        my_tree.column("Item_Hired", anchor=W, width=200)

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
                 
        
        # Bind double-click event to treeview
        my_tree.bind("<Double-1>", delete_row)   
        
        

        # Destroy Program Function
        def close():
            root.destroy()

        button2 = Button(root, text='Exit', font=('Catamaran', 15), command=close)
        button2.grid(row=10, column=0, sticky="se")

    # Window_1 Labels, Buttons etc.
    label1 = Label(root, text="Welcome to...", font=("Century Gothic", 25))
    label1.grid(row=0, column=0)

    button1 = Button(root, text='Proceed', font=('Catamaran', 15), command=window_2, activebackground='blue')
    button1.grid(row=1, column=0, pady=20)

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


window_1()
root.mainloop()
