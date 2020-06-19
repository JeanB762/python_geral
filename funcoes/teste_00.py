"""
 1 - Funções nomeadas (def)
 2 - Funções Anônimas (lâmbda)
 3 - Funções de classe (class)
"""

# Nomeada
def soma(x, y):
  return x + y

# Anônima
anonima = lambda x, y: x + y

# Classe
class classe_soma:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __call__(self):
    return self.x + self.y
