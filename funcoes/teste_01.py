# Funções nomeadas

def soma(x, y):
  """
  Função que soma dois valores
  """
  return x + y

print(soma(2, 2))
print(soma.__name__)

print(soma.__doc__)



# Funções anonimas

resultado = (lambda x: x + 2)(3)
print(resultado)

print(list(map(lambda x: x +2, [1, 2, 3, 4, 5])))
 

# Função de classe

class classe_soma:
  def __call__(self, x, y):
    return x + y

a = classe_soma(2, 2)

print(a())