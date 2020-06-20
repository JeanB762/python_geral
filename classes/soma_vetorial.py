class vetor:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, vetor):
    return(self.x + vetor.x, self.y + vetor.y)

  def __mul__(self, n):
    return (self.x * n, self.y * n)

v_1 = vetor(1, 2)
v_2 = vetor (3, 4)

print(v_1 + v_2)

print(v_2 * 3)