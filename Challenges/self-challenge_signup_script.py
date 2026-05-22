#Create a sign up page usng what you have learnt from boolean operators and what you have learnt so far in python.
# The sign up page should have the following fields: name, email, phone, username. 
# The user should be able to sign up if they provide at least one of the fields. 
# However, if they provide all the fields, they should be able to sign up as well.

name = input("Enter your name: ")
email = input("Email address")
phone =input("Phone number")
username = input("Choose username")

if any([name, email, phone, username]): #Can replace with all to see what happens.
    print("SignUp Successful")
else: print("NOTE!Please fill in atleast one field to sign up")