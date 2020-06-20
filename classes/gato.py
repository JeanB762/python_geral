class gato:
  def __init__(self, nome, cor, idade):
    self.nome = nome
    self.cor = cor
    self.idade = idade
    self.rodado = 0

  def miar(self): 
    if self.com_fome:
      return 'Miaaaaaauuuuuuuuuu'
    else:
      return 'Miau, Miau'

  def andar(self):
    self.rodado += 1
    return 'Mingau andando'

  def alimentar(self):
    self.rodado = 0
    return 'Mingau comendo'

  @property
  def velho(self):
    return True if self.idade > 3 else False

  @property
  def cansado(self):
    return True if self.rodado > 5 else False

  @property
  def com_fome(self):
    return True if self.rodado > 5 else False

mingau = gato('Mingau', 'Branco', 5)

print(mingau.nome)
print(mingau.cor)
print(mingau.idade)
print(mingau.miar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.andar())
print(mingau.miar())
print(mingau.alimentar())


print(mingau.velho)
print(mingau.andar())
print(mingau.andar())
print(mingau.cansado)
print(mingau.miar())
print(mingau.andar())
print(mingau.andar())
print(mingau.cansado)
print(mingau.miar())
print(mingau.andar())
print(mingau.andar())
print(mingau.cansado)
print(mingau.miar())
print(mingau.alimentar())
print(mingau.miar())