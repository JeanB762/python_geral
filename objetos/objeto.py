class num:
  """
  Classe simulando um int
  """
  def __init__(self, numero):
    self.numero = numero

  def __repr__(self):
    return 'Num: {}'.format(self.numero)

print(num(8))   # Implementando o metodo __repr__, agora temos um metodo de formatar a saida