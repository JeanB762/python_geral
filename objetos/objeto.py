class num:
  """
  Classe simulando um int
  """
  def __init__(self, numero):
    self.numero = numero

  def __repr__(self):
    return 'Num: {}'.format(self.numero)

  def __add__(self, op):
    return self.numero + op

  def __radd__(self, op):
    return self.numero + op

  def __sub__(self, op):
    return self.numero - op

  def __rsub__(self, op):
    return self.numero - op

  def __mul__(self, op):
    return self.numero * op
  
  def __rmul__(self, op):
    return self.numero * op

  def __truediv__(self, op):
    return float(self.numero / op)

  def __rtruediv__(self, op):
    return float(self.numero / op)

n = num(8)
print(n)
print(n + 2)
print(2 + n)
print(n - 2)
print(2 - n)
print(n * 2)
print(2 * n)
print(n / 2)
print(2 / n)