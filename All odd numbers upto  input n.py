n = int(input("Enter a number (n): "))

print(f"Odd numbers up to {n}:")
for i in range(1, n + 1):
  if i % 2 != 0:  # If not divisible by 2, it's odd
    print(i, end=" ")
