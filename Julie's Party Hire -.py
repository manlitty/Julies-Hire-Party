#Julie's Party Hire

from tkinter import *
from PIL import Image, ImageTk #still comes out yellow

root=Tk()
root.title("Julie's Hire Party")
root.iconbitmap('C:\\Users\\super\\Downloads\\hireparty.ico')
root.minsize(height=450,width=500)

# Window 1 - Opening Window

def window_1():
    label1=Label(root, text="Welcome to...", font=("Century Gothic",35))
    label1.place(relx= 0.0, rely = 0.0,  anchor = 'nw')
    button1=Button(root,text='Proceed',font=('Catamaran',15),command=window_2)
    button1.pack(side=BOTTOM)
    
    #Images - 21-25
    party_Rentals = ImageTk.PhotoImage(Image.open("julies_party_rentals.png"))
   
    label2 = Label(root, image = party_Rentals)
    
    label2 = Label(root, image= party_Rentals, bd=3, relief="sunken")
    
    label2.pack(padx=20, pady=75 )
    
    
    def window_2():#page 2
        
        label1.destroy()
        button1.destroy()
        label3= Label(root,text="Julie's Party Hire", font=('Century Gothic',15))
        button3 = Button(root, text='Exit', font=('Century Gothic',15),command=back)
        label3.pack()
        button3.pack(side=RIGHT)
        def back():
            label3.destroy()
            button3.destroy()
            window_1()
window_1()
root.mainloop()