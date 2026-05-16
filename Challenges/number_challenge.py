#CHALLANGE
#Generate a random number between 1 and 100 and check if the result is an even number.
import random
number = random.randint(1, 100)
if number % 2 == 0: print(f"{number} is an even number.")
else: print(f"{number} is an odd number.")
