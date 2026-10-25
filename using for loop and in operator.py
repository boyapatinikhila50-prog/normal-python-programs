#String to check
text = "Python Programming"

# Define the vowels to look for
vowels = "aeiouAEIOU"

print(f"Original text: {text}")
print("Vowels found in the text:")

# Using 'for' loop and 'in' operator
for char in text:
  if char in vowels:  # 'in' checks if char exists in the vowels string
    print(char, end=" ")
