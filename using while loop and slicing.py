# String to slice
text = "PythonProgramming"
chunk_size = 3
index = 0

print(f"Original string: {text}")
print(f"Dividing into chunks of {chunk_size}:\n")

# Using a while loop and slicing together
while index < len(text):
  # Extract a slice from index up to index + chunk_size
  chunk = text[index : index + chunk_size]
  print(chunk)

  # Move the index forward by the chunk size
  index += chunk_size
