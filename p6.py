# WAP for removing i-th character from a string
def remove_ith_character(input_str, i):
    if 0 <= i < len(input_str):
        result_str = input_str[:i] + input_str[i+1:]
        return result_str
    else:
        print(f"Invalid index {i}. Please provide a valid index.")
input_string = "example"
index_to_remove = 2  
result = remove_ith_character(input_string, index_to_remove)
if result:
    print(f"After removing the {index_to_remove}-th character from '{input_string}': {result}")