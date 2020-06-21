class Fila:
  def __init__(self, *args):
    self.f = list(args)

  def __repr__(self):
    return f'Fila: {self.f}'

  def __setitem__(self, pos, val):
    self.f[pos] = val

  def __getitem__(self, pos):
    return self.f[pos]
  
  def __lshift__(self, val):
    self.f.append(val)

  def __len__(self):
    return len(self.f)
  
  def __rshift__(self, val):
    self.f.remove(val) if val < len(self.f) else 'feijoada'

fila = Fila(1, 2, 3, 4, 5)

# print(fila[:-2])
# print(fila[2:])
# print(fila[2:4])
# print(fila[:4])

fila[3] = 81

print(fila)

for x in fila:
  print(x + 50)

fila << 34 # Inserção por lshift

print(fila)

fila >> 4

print(fila)
