# date = "11-May-2026"
# # find out if the the starting character is true/false
# print(date.startswith("11"))

# # find out if the the ending character is true/false
# print(date.endswith("9 "))

# # find out if the string contains a specific character no matter the postion
# print("10" in date)
# #ind methods works by finding the indes of the first character if the item and returns -1 if not found
# print(date.find("May"))
# print(date.find("September"))

# #Quick use of  search methods in real application
# phone = "+61-123-456-789"
# print(phone.startswith("+61"))
# email = "santa@myspace.com"
# print(email.endswith("@gmail.com"))
# file = "data_backup.csv"
# print (file.endswith(".csv"))
# print("@" in email)
# url = "https://www.google.com/v1/ask"
# print("google" in url)
# # print(url.find("google"))

# Using find 

phone1 = "+299-590-345-324"
phone2 = "341-459-324-234"
phone3 = "00341-459-324-234"
print(phone1[5:])
print(phone2[4:])
print(phone1.find("-"))
# nest find for easier execution
print(phone1[phone1.find("-")+ 1:]) #find the first dash and then find the second dash
print(phone2[phone2.find("-")+ 1:])
print(phone3[phone3.find("-")+ 1:])


