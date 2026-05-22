# 1. BOOLEAN OPERATORS
# print(True)
# print(False)
# print (not True) #The not operator negates the value of True, resulting in False.
# print(type(True))
# print(bool(1)) #In Python, the boolean value of 1 is True, while the boolean value of 0 is False.
# print(bool(0)) #In Python, the boolean value of 0 is False, while the boolean value of 1 is True.
# print(bool(-1)) #In Python, the boolean value of -1 is True.
# print(bool(None)) #In Python, None is considered False.

# #Using all and any functions to check if at least one field is provided or if all fields are provided for sign up.
# email = ""
# phone = "+2394-205950"
# username = ""
# #Allow sign up
# # If any field is provided
# print(any([email, phone, username]))#Must have at least one field provided to sign up
# print(all([email,phone,username]))#Must have all fields provided to sign up

# #Using isinstance to check if a variable is of a certain type.
# print(isinstance(345, int))
# print(isinstance("Hello", str))
# print("Hello World".endswith("D"))
# print("Hello World".startswith("H"))

# 2. COMPARISON OPERATORS

# print(5>10)
# print(5<10)
# print(5==10)
# print(5!=10)
# print(5>=10)
# print(5 <= 10)
# Expressions with comparison operators can be combined using boolean operators

# print(5-1 == 2-1)
# print(len("Hello World") == 5+6)
# print("a" < "b")
# print("a" == "b")
# print("a" == "A")  # False  because python is case sensitive

# #Chain comparison operators
# print(1 < 2 < 3) #True because 1 is less than 2 and 2 is less than 3

#Check if age ins between 45 and 85- self challenge learnt how to use elif and comparison operators. Also learnt "or not" boolean operators to check if the user input is empty or not a number.
age =input("Enter Age?")
if age == "" or not age.isdigit():
    print("Must enter your a number for age to continue")
elif 45 <int(age) <85:
    print("You are and oldie! Great to have you here. Welcome!")
else:
    print("Oops! Come back in", 45- int(age),"years")
 
