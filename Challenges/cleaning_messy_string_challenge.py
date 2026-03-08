##Python Challenge Turn the messy string into a single clean summary with name, role, and age
# ##"968-Maria, ( Data Engineer );; 27y  "##
text = "968-Maria, ( D@t@ Engineer );; 27y  "

# print("Name:",text[4:9],"|".strip(),"Role:",text[12:26].strip(),"|" " ", "Age:",text[-5:-3].strip(), )


print("Name:",text[4:9],"|".strip(),"Role:",text[12:26].strip().replace("@","a"),"|" " ", "Age:",text[-5:-3].strip())