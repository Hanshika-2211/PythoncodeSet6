# WAP program to find the elast frequent character in the string
def least_frequent_char(input_str):
    char_frequency = {}
    for char in input_str:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    least_frequent = min(char_frequency, key=char_frequency.get)

    return least_frequent
input_string = "abracadddabra"
result = least_frequent_char(input_string)

print(f"The least frequent character in the string '{input_string}' is: {result}")