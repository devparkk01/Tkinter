#  will learn how to add radio buttons in the gui

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

# we don't have `textvariable` here , instead we have `variable `. It will have the same functionality.
#  `text` argument will appear in the widget .
#  `value` argument gives what `variable` will contain
#  if that radiobutton is selected  . 


#  creating final submit button 

def action ():
    userName = nameVar.get() 
    userAge = ageVar.get() 
    userEmail = emailVar.get() 
    userGender = genderVar.get()
    userProffesion = professionVar.get() 
    print(f"{userName} , {userAge} , {userEmail} , {userGender } , {userProffesion } ")

submit = ttk.Button(win , text ="Submit" , command = action  )
submit.grid (row = 5 , column = 1 , sticky = tk.E  )

win.mainloop()