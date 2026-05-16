# measuring distance
print(2-10)
print(abs(2-10)) #abs function gives the absolute value of a number.
import math
# rounding numbers 
price = 35.5738393
print ("rounded price is " + str(    round(price))) #python rounds to the nearest even number when the number is exactly in the middle.
print("floor  price is " + str(math.floor(price))) #need to import math module to use floor and ceil functions 
print("ceil price is " + str(math.ceil(price)))
print(round(price,2)) #rounding to 2 decimal places
print (math.trunc(price)) #trunc function removes the decimal part of the number without rounding it.
print (int(price))#another way to remove the decimal part of the number without rounding it is to convert it to an integer using the int() function