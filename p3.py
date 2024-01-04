# WAP to find uncommon words from two strings
def find_uncommon_words(str1, str2):
    words1 = str1.split()
    words2 = str2.split()
    uncommon_words = set(words1) ^ set(words2)
    return uncommon_words
string1 = "Hello World .!"
string2 = "Hello World , How are you?"

uncommon_words = find_uncommon_words(string1, string2)

print("Uncommon words:", uncommon_words)