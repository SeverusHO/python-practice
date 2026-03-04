# Python Challenge
# Convert the messy phone number into a clean number format with "+49 (176)123-4567"

text = "+49 (176)123-4567"
print(text.replace("+", "").replace(" ", "").replace("(","").replace(")","").replace("-", ""))
