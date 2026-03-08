# name  = "        Software ###### Engineer        "

# print(name)

# print(name.lsclear
# trip()) #remove left space

# print(name.rstrip()) #remove right space

# print(name.strip()) #remove both left and right space

# name= "Software ###### Engineer ".replace("#","") #remove # from the string
# print (name)
# name= "Software ###### Engineer ".strip("#") #remove # from the string
# print (name)

# text = " Software"
# print (text)
# print (len (text))
# print (text.strip())#remove left and right space but does not change the original string
# print (len(text.strip())) #length of the string after removing left and right space
# print (len (text) - len(text.strip())) #length of the string before removing space - length of the string after removing space = number of spaces removed
# print (len (text) == len(text.strip()))
# print (len (text) > len(text.strip()))
# print (len (text) < len(text.strip()))
# print (len (text) <= len(text.strip()))

# Cleaning white space and checking  if the data is purely string characters or not
# text = "  Software"
# print("This is the text in question:", text)
# total_characters = "Total length of characters:", len(text)
# print(total_characters)
# nr_of_characters = "Number of characters without spaces:", len(text.strip())
# print(nr_of_characters)
# characters_without_spaces = "Number without spaces:", len(
#     text) - len(text.strip())
# print(characters_without_spaces)
# is_data_clean = "Is the data clean? ", len(text) == len(text.strip())
# print(is_data_clean)

# Case conversions

# text_display = "SofTwaRe EnG inEer"
# print(text_display.upper())
# print(text_display.lower())
# print(text_display.capitalize())
# print(text_display.title())

search="Email ".lower().strip()
data= "email" .lower()
print(search==data)
