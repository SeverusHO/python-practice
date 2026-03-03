# text = "hi"
# number = 10

# print(len(text))
# #print (len(number)) - Wont work because you can only use methods from same class type?
# print(text.upper())
# print (number.bit_length())



#Python Challenge
#Create 5 variables - each with a different data type:
#1. Your age
#2. Your height (with decimals)
#3. Your name
#4. Are you a student?
#5. Something with no value yet
#Then print the values, data types, lengths of all #


# a = "Your age"
# b = "Your height (with decimals)"
# c = "Your name"
# d = "Are you a student?"
# e = None
# print(a)

age = 30 #int
height = 162.2 #float
name = "ThreeBN" #str
studentstatus = True #bool
emptyvalue = None  #Gap, No assigned value yet

print()
print("1-> age".upper())
print("------------------------------------------------------------------------------------")
print(age),
print ("The type is", type(age),"However i get class interger instead",)
print(age.bit_length())


print()

print("2. >- height".upper())
print("------------------------------------------------------------------------------------")
print(height)
print("This is the type-->",type (height),)
# #print(height.bit_length())# 
# print ("'float' which is object has no attribute 'bit_length'" "\ntry again")
# #print(len(height) )
# print ("'float' which is object has no length'" "\ntry again")
print(emptyvalue,"-No len or bit.len for float type") 


print()

print("3  >-".upper(),name.upper())
print("------------------------------------------------------------------------------------")
print(name)
print("This is the type of class the data belongs to-->",type,(name))
print(len(name),"Is the total length") 

print()

print("4. >-student status".upper())
print(studentstatus)
print("This is the type of class the data belongs to-->",type,(studentstatus))
print(studentstatus.bit_length)

print()

print("5. >-print something with no value".upper())
print("------------------------------------------------------------------------------------")
print( "\n The answer is...",emptyvalue, "...\t >>No value has been assigned here")

