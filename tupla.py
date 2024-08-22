#TUPLA
#Sequencia de itens delimitada por parenteses

tuple = (3, 6, 2, 10, 30)

print(tuple[0])

for item in tuple:
    print(item)

# estrutura imutavel - não pode ser modiciada 
#tuple[0] = 100

#tupla vazia
tuple = ()
print(tuple)

#tupla com um elemento
tuple = (10,)
print(tuple)

tuple = (4, 6, 10, 3, 1)
print(max(tuple))
print(min(tuple))
print(sum(tuple))
print(len(tuple))

print(tuple.count(6))
print(tuple.index(6))

ufs = ('AC','SP','RJ')

coordenadas = [(23.555,.108880), (45.4989, 34.989)]
print(coordenadas[0][1])

coordenadas[0] = 3
print(coordenadas)

tupla = ([3, 5, 6], [1, 2, 3])
tupla[0][0] = 999
print(tupla)

# lista - converte uma tupla para lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)

#tuple - converte uma lista para tupla
lista = [4, 7, 10]
tupla = tuple(lista)
print(tupla)
