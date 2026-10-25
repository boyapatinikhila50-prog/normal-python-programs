# Get input from the user
n = int(input("Enter a number (n): "))

print(f"Odd numbers up to {n}:")

i = 1
while i <= n:
  print(i, end=" ")
  i += 2  # Increment by 2 to get the next odd number
