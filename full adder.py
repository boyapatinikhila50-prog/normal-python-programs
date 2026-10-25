def full_adder(a, b, c_in):
  # Sum is A XOR B XOR C_in
  sum_bit = a ^ b ^ c_in

  # Carry out is (A AND B) OR (C_in AND (A XOR B))
  carry_out = (a & b) | (c_in & (a ^ b))

  return sum_bit, carry_out


# --- Testing with a Truth Table ---
print("A | B | Cin | Sum | Cout")
print("-" * 22)

for a in (0, 1):
  for b in (0, 1):
    for c_in in (0, 1):
      s, cout = full_adder(a, b, c_in)
      print(f"{a} | {b} |  {c_in}  |  {s}  |   {cout}")
