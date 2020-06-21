class num:
   """
   Classe simulando um int
   """
   def __init__(self, numero):
     self.numero = numero

print(num(8)) # Nesse momentp ainda não definimos __repr__, portando ela não pode ser "printada"
print(num(8).numero)  # Porem conseguimos acessar o atributo numero que foi passado para a classe