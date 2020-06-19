from pdb import set_trace

def externa(id):
  dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'hello'}

  def interna(nome):
    print('{} {}'.format(dic[id], nome))
  return interna

func = externa('pt')
func('Jean')