# we will use tabs here in a bigger aspect 

import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title ("Python GUI")

# creating a notebook 
nb = ttk.Notebook(win )

# creating a page(frame). This will store personal details  
personalDetail = ttk.Frame(nb) 

labelframe = ttk.LabelFrame(personalDetail , text = "Enter your Personal Details") 
ttk.Label(labelframe , text = "Enter your name",width = 20).grid(row = 0 , column = 0 , sticky = tk.E )
ttk.Label(labelframe, text = "Enter your age" , width =20).grid (row = 1 , column = 0 , sticky = tk.E )
ttk.Label (labelframe, text = "Enter your address", width =20 ).grid ( row = 2 , column = 0 , sticky = tk.E )
ttk.Label(labelframe, text = "Select your gender", width =20).grid (row = 3 , column = 0 , sticky = tk.E )

#  not creating textvariables here 
ttk.Entry(labelframe , width = 20).grid(row = 0 , column = 1 , sticky = tk.W)
ttk.Entry(labelframe , width =20 ).grid(row = 1 , column = 1 , sticky = tk.W)
ttk.Entry(labelframe , width = 20 ).grid(row = 2 , column = 1 , sticky = tk.W)

genderField = ttk.Combobox(labelframe , width = 17, state = "readonly")
genderField["values"] = ("Male" , "Female" , "Others")
genderField.current(0)

genderField.grid(row = 3,  column = 1 )
labelframe.grid(row = 0 , column = 0 , pady = 10 )


for child in labelframe.winfo_children() :
    child.grid_configure(padx = 10 , pady = 5 )

submitField = ttk.Button(personalDetail , text = "Submit" , command = lambda : print("Hello"))
submitField.grid(row = 4 , column = 1 )


# creating another page(frame) . This is for academic details . 
academicDetail = ttk.Frame(nb) 

labelframe2 = ttk.LabelFrame(academicDetail , text = "Enter your Academic Details")

ttk.Label(labelframe2 , text = "Enter your USN" ,width = 20  ).grid(row = 0 , column = 0 )
ttk.Label(labelframe2, text = "Select your Branch" , width = 20 ).grid(row = 1 , column = 0 )
ttk.Label(labelframe2 , text = "Select Your Sem" , width = 20).grid(row =2 , column = 0 )

usnField = ttk.Entry(labelframe2 , width = 20 )
usnField.focus()
usnField.grid(row = 0 , column = 1 )

branchField = ttk.Combobox(labelframe2 , width = 17, state = "readonly")
branchField['values'] = ("MECH" , "ISE" , "CSE" , "ECE" , "CIV")
branchField.current(1)
branchField.grid(row = 1 , column = 1 )

semField = ttk.Combobox(labelframe2 , width = 17 , state = "readonly")
semField["values"] = (1, 2 , 3, 4, 5, 6, 7, 8)
semField.current(0)
semField.grid(row = 2 , column = 1 )

labelframe2.grid(row = 0 , column = 0 , pady = 10 )

for child in labelframe2.winfo_children() :
    child.grid_configure(padx = 10 , pady = 5 )

submitField2 = ttk.Button(academicDetail , text = "Submit" , command = lambda : print("Hello"))
submitField2.grid(row = 3 , column = 1  )

#  adding the pages to the notebook `nb`
nb.add(personalDetail , text ="Personal Details")
nb.add(academicDetail , text = "Academic Details")



# packing the notebook
nb.pack(expand = True , fill = "both")



win.mainloop()