# we'll learn how to create buttons , let's say submit button
# last time we saw how to create entrybox , here we will see how to
# create buttons

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
# win.resizable( 0 , 0 )

# Creating labels
name = ttk.Label(win , text = "Enter your name " , width = 16 )
name.grid(row = 0 , column = 0 ,sticky = tk.W)

age= ttk.Label(win , text = "Enter your age " , width = 16 )
age.grid (row = 1, column = 0 )

email = ttk.Label(win , text ="Enter your email " , width = 16 )
email.grid(row = 2 , column = 0 )

#  creating entryboxes
nameVar = tk.StringVar()
ageVar = tk.StringVar()
emailVar = tk.StringVar()

nameField = ttk.Entry(win , width = 16 , textvariable = nameVar )
nameField.grid(row = 0 , column = 1 )
ageField  = ttk.Entry(win , width = 16 , textvariable = ageVar )
ageField.grid (row = 1 , column = 1 )
ageField = ttk.Entry(win , width = 16 , textvariable = emailVar )
ageField.grid(row = 2 , column = 1 )


# creating buttons

# submitBotton = ttk.Button(win , text = "Submit")
# submitBotton.grid(row = 3 , column =  1 , sticky = tk.E)

# what should happen when we click this button . we didn't specify anything as such while creating this button
# we can do so by giving a callback function as argument to 'command' argument

def action () :
    userName = nameVar.get() # to get the value stored inside nameVar
    userAge = ageVar.get() # to get the value stored inside ageVar
    userEmail = emailVar.get() # to get the value stored inside emailVar
    print( f"{userName} , {userAge} , {userEmail}")

submitBotton = ttk.Button(win , text = "Submit" , command = action )
submitBotton.grid(row = 3 , column =  1 , sticky = tk.E)



win.mainloop()