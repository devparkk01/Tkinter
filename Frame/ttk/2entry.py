# Learn how to create an entry box
#  we'll use Entry() to create an entry box

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
# win.geometry("400x400")
# win.resizable(0 ,0 )

# Creating a label
name = ttk.Label(win , text = "Enter your name : " ,width = 16)
name.grid(row = 0 , column = 0 , sticky = tk.W )

age = ttk.Label(win , text = "Enter your age : ", width = 16 )
age.grid (row = 1 , column = 0 , sticky = tk.W)

email = ttk.Label(win , text ="Enter your email : " , width = 16 )
email.grid(row = 2 , column = 0 , sticky = tk.W)


# Creating entrybox
# width argument specifies the width of the entrybox

# nameField = ttk.Entry(win , width = 16  )
# nameField.grid(row = 0 , column = 1  )
#
# ageField = ttk.Entry(win , width = 16  )
# ageField.grid(row = 1 , column = 1 )
#
# emailField = ttk.Entry(win , width = 16  )
# emailField.grid(row = 2 , column = 1 )


# creating only entry box is not sufficient , we need to create variables where enterred values will
# be stored

nameVar = tk.StringVar() # creating an instance of StringVar()
nameField = ttk.Entry(win , width = 16 , textvariable = nameVar )
nameField.grid (row = 0 , column = 1 )

ageVar = tk.StringVar()
ageField = ttk.Entry(win , width = 16 , textvariable = ageVar)
ageField.grid(row = 1 , column = 1 )

emailVar = tk.StringVar()
emailField = ttk.Entry(win  , width = 16 , textvariable = emailVar)
emailField.grid(row = 2 , column = 1 )


win.mainloop()

