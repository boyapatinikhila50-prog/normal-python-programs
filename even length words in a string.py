# Get string input from the user
text = input("Enter a string: ")

# Split the string into individual words
words = text.split()

print("Words with an even length:")
for word in words:
  if len(word) % 2 == 0:
    print(word)
