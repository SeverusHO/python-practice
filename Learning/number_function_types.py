x = 5
y = 4.5
z = 2+3j
#type() function is used to determine the type of a variable or value. It returns the data type of the variable or value as an object. In this case, x is an integer, y is a float, and z is a complex number.
print(type(x)) 
print(type(y)) 
print(type(z))
 
#Example
p = "67"
print(p)
print ((p *4)) #This will print the string "67676767" because multiplying a string by an integer repeats the string that many times.
p = int(p) #This converts the string "67" to the integer 67. Now p is an integer, and we can perform arithmetic operations on it. 
print(int(p))
print ((p *4))

y = 4.5 
print(int(y)) #This will convert the float 4.5 to the integer 4 by truncating the decimal part. The result is 4.
x = 5
print(float(x)) #This will convert the integer 5 to the float 5.0. The result is 5.0.
x = "5"
print(float(x)) #This will convert the string "5" to the float 5.0. The result is 5.0.

x = 2
y = 3
print(complex(x,y)) #This will create a complex number with the real part as x (2) and the imaginary part as y (3). The result is (2+3j).