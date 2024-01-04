# WAP a program to access and print characters from the string 
# print first character,second character,last character,second last character,characters from 0th to 4th index,first 5 characters,characters from 2nd to 2nd last index and string character by character
str_val = "Hello world"
print("First character:", str_val[0])
print("Second character:", str_val[1])
print("Last character:", str_val[-1])
print("Second last character:", str_val[-2])
print("Characters from 0th to 4th index:", str_val[0:5])
print("First 5 characters:", str_val[:5])
print("Characters from 2nd to 2nd last index:", str_val[2:-1])
print("String character by character:")
for char in str_val:
    print(char)