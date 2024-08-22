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