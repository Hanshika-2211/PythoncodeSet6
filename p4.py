# WAP to check whether a given string is binary or not
def is_binary(string):
    valid_binary_digits = {'0', '1'}
    return all(char in valid_binary_digits for char in string)
input_string = "101010101"
if is_binary(input_string):
    print(f"The string '{input_string}' is a binary string.")
else:
    print(f"The string '{input_string}' is not a binary string.")