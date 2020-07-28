# we will talk about labelframe here 

# The LabelFrame widget is used to draw a border around its child widgets. We can also display the title 
# for the LabelFrame widget. It acts like a container which can be used to group the number of 
# interrelated widgets such as Radiobuttons.

import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title("Python Gui")
# win.resizable (0 , 0 ) 


labelFrame = ttk.LabelFrame(win , text = "Enter your details")
labelFrame.grid(row = 0 , column = 0 , padx = 12 , pady = 8)

#  creating labels 
name = ttk.Label(labelFrame , text ="Enter your name " , width = 16 )
name.grid(row= 0 , column = 0 , sticky = tk.W  )
age= ttk.Label(labelFrame , text = "Enter your age " , width = 16 )
age.grid (row = 1, column = 0 , sticky = tk.W   )
email = ttk.Label(labelFrame , text ="Enter your email " , width = 16 )
email.grid(row = 2 , column = 0  , sticky = tk.W )

# creating entryboxes
 
nameVar = tk.StringVar()
ageVar = tk.StringVar()
emailVar = tk.StringVar()
nameField = ttk.Entry(labelFrame , width = 16 , textvariable = nameVar)
nameField.grid(row = 0 , column = 1 )
nameField.focus() # this line puts the cursor by default in the nameField 
# so we don't have to take the cursor to the nameField 

ageField  = ttk.Entry(labelFrame , width = 16 , textvariable = ageVar )
ageField.grid (row = 1 , column = 1  )
ageField = ttk.Entry(labelFrame , width = 16 , textvariable = emailVar )
ageField.grid(row = 2 , column = 1   )

# creating combobox
#  it will have the option for selecting the gender

gender = ttk.Label(labelFrame , text = "Select gender " , width  = 16  )
gender.grid(row = 3 , column = 0 , sticky = tk.W   )

genderVar = tk.StringVar() 
genderField = ttk.Combobox(labelFrame , width = 13 , textvariable = genderVar , state = "readonly")

# adding options inside Combobox 

genderField["values"] = ("Male" , "Female" , "Others")  

genderField.current(0)  
genderField.grid(row = 3 , column = 1 )

# creating radiobuttons which will store whether the person is student or faculty 
professionVar = tk.StringVar() 
radioButton1 = ttk.Radiobutton(labelFrame , text = "Student" , value = "Student" , variable = professionVar)
radioButton1.grid(row = 4 , column = 0 )
radioButton2 = ttk.Radiobutton(labelFrame , text = "Faculty" , value = "Faculty" , variable = professionVar)
radioButton2.grid(row = 4, column = 1 )

# creating checkbox 

subscriptionVar = tk.IntVar()
checkButton = ttk.Checkbutton(labelFrame , text = "Subscribe to the newsletter ", variable = subscriptionVar)
checkButton.grid(row = 5 , columnspan = 2  )

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
submit.grid (row = 6 , column = 0 , sticky = tk.E , padx = 10 , pady = 4 )

# there is a special method called `winfo_children()` 
# it returns a list of all widgets which are children of this widget



for child in labelFrame.winfo_children() :
    child.grid_configure(padx = 5 , pady = 5 ) # used to configure grid 

win.mainloop()