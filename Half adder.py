class HalfAdder:

  def compute(self, a: int, b: int) -> dict:
    self.sum = a ^ b
    self.carry = a & b
    return {"sum": self.sum, "carry": self.carry}
