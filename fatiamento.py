# Retorna uma sublista a partir de uma lista, de um indice inicial até um indice final
lista = [5, 1, 40, 30, 10, 7]
lista2 = lista[0:4]
print(lista)

lista = [5, 1, 40, 30, 10, 7]
lista2 = lista[2:5]
print(lista2)


# A partir do inicio
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[:5])

# Até o final
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[3:])

# do inicio aé o fim
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[:])

#fatiamento inverso
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[::-1])

#fatiamento com incremento
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[2:6:2])

#fatiamento com incrento inverso
lista = [3, 6, 7, 8, 12, 4, 5, 6, 7, 8]
print(lista[6:1-2])

nome = 'João Silva'
primeironome = nome[:4]
sobrenome = nome[4:]
print(primeironome)
print(sobrenome)
