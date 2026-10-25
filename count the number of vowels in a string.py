# Get string input from the user
text = input("Enter a string: ")

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"
count = 0

# Loop through each character in the string
for char in text:
  if char in vowels:
    count += 1

print(f"Number of vowels: {count}")
