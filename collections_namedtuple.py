from collections import namedtuple

# Uma tupla é uma sequencia imutavel

t = (1, 2, 3, 4)

print('# Acesso index')
print(t[0])

print('# Acesso slice')
print(t[0:3])
print(t[::2])


tupla = (1, 2, 5, 10, 4, 3, 8, 7, 1, 3, 45, 22, 37, 49)

# Tuplas executam 2 métodos

print('# O metodo count retorna a quantidade de ocorrencias do valor dentro da tupla')
print(tupla.count(3))

print('# O método index retorna o indice da primeira ocorrencia do valor')
print(tupla.index(3))

print('# Apesar da tupla ser imutável, se houver objetos mutáveis no seu conteudo')
print('# eles poderão ser manipulados de acordo com seus metodos')
a = (1, 2, 3, [1])

print('# Tupla "a"')
print(a)
print('# Após a realização de um append "2"')
a[3].append(2)
print(a)

# Atribuição de funções
func = lambda x: x**x
tupla = (func, 2)

print('#Aplicando a função de um indice no proximo item da tupla')
print('Tupla: ', tupla)
print(tupla[0](tupla[1]))


# A principal caracteristica da namedtuple, é o acesso por atributos
# Uma namedtuple pode ser encarada como uma abstração da construção de objetos que
# Pode ser util em diversas ocasiões tornando o codigo mais simples e menos verboso
### Exemplo ###
print('### Named Tuple ###')

jogador_nt=namedtuple("jogador", ['nome', 'time', 'camisa'])
ronaldo = jogador_nt('Ronaldo', 'Brasil', 9)
bruxo = jogador_nt('Bruxo', 'Brasil', 10)
print(ronaldo.nome)
print(ronaldo.time)
print(ronaldo.camisa)

print('#########################')

print(bruxo.nome)
print(bruxo.time)
print(bruxo.camisa)
