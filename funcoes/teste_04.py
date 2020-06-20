def decorador(func):
  print(func.__name__)
  def interna(x, y):
    if isinstance(x, int) and isinstance(y, int):
      return func(x, y)
    else:
      raise ValueError('Insira somente inteiros')

  return interna

# decorador(soma(2, 2))
@decorador
def soma(x: int, y: int):
  return x + y

@decorador
def div(x: int, y: int):
  return x / y

# Chamada da função com o decorador para customização do erro
print(soma(2, 2)) # Correto
print(div(2, 2))  # Correto

# print('###############################################')
# print(soma(2, 'teste')) # Errada
# print(div(2, 'teste'))  # Errada