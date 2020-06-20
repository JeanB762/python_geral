def decorador(argumentos_decorador):
  """
  Parametros do decorador
  """
  print(argumentos_decorador)
  def decorador_real(func):
    """
    Receber a função
    """
    print(func.__name__)
    def executar_func(*argumentos_funcao):
      """
      Executar a função
      """
      print(argumentos_funcao)
    return executar_func
  return decorador_real


@decorador('Jean')
def soma(x, y):
  return x + y

soma(2, 2)