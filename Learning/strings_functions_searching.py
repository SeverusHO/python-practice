a= "2026-Mar-10"
print(a.startswith("2026")) #output is boolean
print(a.endswith("20")) #output is boolean
print("Mar" in a) #output is boolean
print(a.find("Mar")) #output is an integer representing the index(starts from zero) of the first occurrence of "Mar"

phone = "+34-174-12345"
print(phone.startswith("+34"))

email = "eggs@gmail.com"
print(email.endswith("gmail.com") )
print  ("@" in email)

file ="data_backup.csv"
print (file.endswith(".csv"))

phone1 = "+34-174-12345"

phone2 = "33-742-14584 "

phone3 = "445-7242-14584 "

print(phone1[4:])
print(phone2[3:])

print (phone1[phone1.find("-")+1:])
print (phone2[phone2.find("-")+1:])
print (phone3[phone3.find("-")+1:])