#Testing if statements and input before full lesson on functions and loops#git add <file>
password = (input("Enter your password: "))
print("Password Set Successfully!")
if len(password) < 8:
  print("Password must be at least 8 characters long.")
elif len(password) > 20:
  print("Password is too long.")