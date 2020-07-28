# here , we will see how to create a combobox  . 
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Python gui ")
# win.resizable( 0, 0 )
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

gender = ttk.Label(win , text = "Select gender " , width  = 16 )
gender.grid(row = 3 , column = 0 , sticky = tk.W)

genderVar = tk.StringVar() 
genderField = ttk.Combobox(win , width = 13 , textvariable = genderVar , state = "readonly")
# we have added state = "readonly" argument to it . This is because we don't want users to enter values manually
# in the combobox , rather we want users to select only those options which are there in the combobox 


# adding options inside Combobox 

genderField["values"] = ("Male" , "Female" , "Others")  # need to put these options in a tuple 
# If we run the code now ,this combobox will have all these options , but there won't be any option selected by default 
# we can do so in following way  

genderField.current(0)  # giving the default value to the Combobox, 0 specifies the tuple index 
genderField.grid(row = 3 , column = 1 )

#  creating final submit button 

def action ():
    userName = nameVar.get() 
    userAge = ageVar.get() 
    userEmail = emailVar.get() 
    userGender = genderVar.get()
    print(f"{userName} , {userAge} , {userEmail} , {userGender } ")

submit = ttk.Button(win , text ="Submit" , command = action )
submit.grid (row = 4 , column = 1 , sticky = tk.E )



win.mainloop() 
