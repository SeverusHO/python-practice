#Testing if statements and input before full lesson on functions and loops#git add <file>
password = (input("Enter your password: "))
print("Password Set Successfully!")
if len(password) < 8:
  print("Password must be at least 8 characters long.")
elif len(password) > 20:
  print("Password is too long.")

#Lesson on how to measure the length of string alues
text = """ 
I love coding with python
python is looking great so far
I am excited to learn more about python
python python python python python python python python python python python python python python python python python python!

"""
print("The string appears", text.count("python"), "times")

#Data transformation using string methods 
price = "$450,000"
print (price.replace(",", " ").replace("$", ""))
phonenumber = "123-456-7890"
print(phonenumber.replace("-", " "),"We replaced things here successfully")