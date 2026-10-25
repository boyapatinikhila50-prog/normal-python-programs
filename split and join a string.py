# Original string
text = "Hello world welcome to python"

# 1. Split the string into a list of words (default separator is space)
words_list = text.split()
print("Split list:", words_list)

# 2. Join the list back into a single string using a hyphen (-)
joined_text = "-".join(words_list)
print("Joined string:", joined_text)
