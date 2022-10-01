from tkinter import Tk

from tkinter import *
root = Tk()   #putting tkinter into a root file

root.geometry("500x300")   #Creating a window to show the registration form
root.title("Registration Form")

def sendvalues():
    print("Data sent")  #Print data sent on the terminal

Label(root, text="Please Fill the Form", font="Helvetica 20 bold").grid(row=0, column=5)

#Creation of the various required fields
#********************* START *********************
name = Label(root, text="Name")
email = Label(root, text="Email")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
payment_mode = Label(root, text="Payment mode")

#Packing the field variables to display them using grid
name.grid(row=1, column=2)
email.grid(row=2, column=2)
phone.grid(row=3, column=2)
gender.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)
#********************* END *********************

#Variables for storing our values 
# ********************* START *********************
name_value = StringVar
email_value = StringVar
phone_value = StringVar
gender_value = StringVar
payment_mode_value = StringVar
#Using checkbox
check_value = IntVar

#Asking users to Enter values
name_entry = Entry(root, textvariable=name_value)
email_entry = Entry(root, textvariable=email_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_mode_entry = Entry(root, textvariable=payment_mode_value)

#Packing the field variables to display them using grid
name_entry.grid(row=1, column=3)
email_entry.grid(row=2, column=3)
phone_entry.grid(row=3, column=3)
gender_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

#Creating a remember me checkbox
rmber = Checkbutton(text="remember me?", variable=check_value)
rmber.grid(row=6, column=3)
#********************* END *********************

#Creating a submit button
Button(text="Submit", command=sendvalues).grid(row=7, column=3)

#Making root file always main loop
root.mainloop()