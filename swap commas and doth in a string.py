# Get string input from the user
text = input("Enter a string: ")

# Create a translation table to swap ',' and '.'
trans_table = str.maketrans(",.", ".,")

# Apply the translation
swapped_text = text.translate(trans_table)

print("Swapped string:", swapped_text)
