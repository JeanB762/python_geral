"""
Pontos, Quadrados e ...
"""

class Ponto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return 'Ponto: ({}, {})'.format(self.x, self.y)


class Linha:
  def __init__(self, p_1, p_2):
    self.ponto_1 = p_1
    self.ponto_2 = p_2

  def __repr__(self):
    return 'Linha: [ {}, {}]'.format(self.ponto_1, self.ponto_2)

  @property
  def distancia_x(self):
    return abs(self.ponto_2.x - self.ponto_1.x)

  @property
  def distancia_y(self):
    return abs(self.ponto_2.y - self.ponto_1.y)



ponto_1 = Ponto(1, 1)
# print(ponto_1)

ponto_2 = Ponto(2, 4)
# print(ponto_2)

# ponto_3 = Ponto(3, 9)
# print(ponto_3)


linha_1 = Linha(ponto_1, ponto_2)

print('Distancia x: ',linha_1.distancia_x)
print('Distancia y: ', linha_1.distancia_y)
print(linha_1)