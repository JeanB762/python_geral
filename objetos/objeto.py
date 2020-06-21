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

n = num(8)
print(n)
print(n + 2)  # O metodo __add__ configura a operação entre a nossa classe + numero
print(2 + n)  # O metodo __radd__ configura a operação entre a um numero + nossa classe

## Agora o objeto esta apto a realizar as operações de adição com os inteiros nativos
