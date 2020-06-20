from pdb import set_trace

def externa(id):
  dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'hello'}

  def interna(nome):
    print('{} {}'.format(dic[id], nome))
  return interna
"""
Closure
"""
from pdb import set_trace


func = externa('pt')
func('Jean')
func('Borges')

pirata = externa('pi')
pirata('Jean')
pirata('Borges')

english = externa('en')
english('Jean')
english('Borges')