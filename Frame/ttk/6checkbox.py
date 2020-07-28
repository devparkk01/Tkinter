#  will learn how to add checkbox to the gui

import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title("Python Gui")
# win.resizable (0 , 0 ) 

#  creating labels 
name = ttk.Label(win , text ="Enter your name " , width = 16 )
name.grid(row= 0 , column = 0 , sticky = tk.W)
age= ttk.Label(win , text = "Enter your age " , width = 16 )
age.grid (row = 1, column = 0 , sticky = tk.W)
email = ttk.Label(win , text ="Enter your email " , width = 16 )
email.grid(row = 2 , column = 0  , sticky = tk.W)

# creating entryboxes
 
nameVar = tk.StringVar()
ageVar = tk.StringVar()
emailVar = tk.StringVar()
nameField = ttk.Entry(win , width = 16 , textvariable = nameVar)
nameField.grid(row = 0 , column = 1 )
nameField.focus() # this line puts the cursor by default in the nameField 
# so we don't have to take the cursor to the nameField 

ageField  = ttk.Entry(win , width = 16 , textvariable = ageVar )
ageField.grid (row = 1 , column = 1 )
ageField = ttk.Entry(win , width = 16 , textvariable = emailVar )
ageField.grid(row = 2 , column = 1 )

# creating combobox
#  it will have the option for selecting the gender

gender = ttk.Label(win , text = "Select gender " , width  = 16  )
gender.grid(row = 3 , column = 0 , sticky = tk.W )

genderVar = tk.StringVar() 
genderField = ttk.Combobox(win , width = 13 , textvariable = genderVar , state = "readonly")

# adding options inside Combobox 

genderField["values"] = ("Male" , "Female" , "Others")  

genderField.current(0)  
genderField.grid(row = 3 , column = 1 )

# creating radiobuttons which will store whether the person is student or faculty 
professionVar = tk.StringVar() 
radioButton1 = ttk.Radiobutton(win , text = "Student" , value = "Student" , variable = professionVar)
radioButton1.grid(row = 4 , column = 0 )
radioButton2 = ttk.Radiobutton(win , text = "Faculty" , value = "Faculty" , variable = professionVar)
radioButton2.grid(row = 4, column = 1 )

# creating checkbox 
# checkbox will contain whether the person wants to subscribe to the newsletter or not 

subscriptionVar = tk.IntVar()
checkButton = ttk.Checkbutton(win , text = "Subscribe to the newsletter ", variable = subscriptionVar)
checkButton.grid(row = 5 , columnspan = 2 )

"""
here , we have  `instead` of `textvariable`
if the checkbutton is selected then `variable` will store 1 , in other case it will store 0 
"""

#  creating final submit button 

subsValue = lambda value : "subscribed" if value == 1 else "Not subscribed"

def action ():
    userName = nameVar.get() 
    userAge = ageVar.get() 
    userEmail = emailVar.get() 
    userGender = genderVar.get()
    userProffesion = professionVar.get() 
    subscription = subsValue(subscriptionVar.get())
    print(f"{userName} , {userAge} , {userEmail} , {userGender } , {userProffesion } , {subscription} ")

submit = ttk.Button(win , text ="Submit" , command = action  )
submit.grid (row = 6 , column = 1 , sticky = tk.E  )

win.mainloop()