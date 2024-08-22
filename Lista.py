# Listas em Python

# 1. Lista vazia
lista_vazia = []

# 2. Lista com elementos
lista = [4, 10, 59, 2]

# 3. Estrutura heterogênea (contém diferentes tipos de dados)
lista_heterogenea = [4, 6, "Texto", 3.6, True, False, 8]

# 4. Estrutura mutável - podemos alterar os itens da lista
lista_mutavel = [5, 6, 7, 10]
lista_mutavel[0] = 9090909090909009
print("Lista após alteração:", lista_mutavel)

# 5. Percorrer os itens da lista e contar os pares
lista_pares = [5, 6, 10, 30, 7]
contagem_pares = 0
for item in lista_pares:
    if item % 2 == 0:
        contagem_pares += 1
print(f'Quantidade de pares: {contagem_pares}')

# 6. Percorrer os índices da lista e alterar os valores
for i in range(len(lista_pares)):
    if lista_pares[i] % 2 == 0:
        lista_pares[i] = 0
print("Lista após alterar valores pares:", lista_pares)

# 7. len - retorna o tamanho da lista
lista_tamanho = [4, 60, 2, 5, 10]
print("Tamanho da lista:", len(lista_tamanho))

# 8. append - insere um item no final da lista
lista_append = [4, 60, 2, 5, 10]
lista_append.append(100)
print(lista_append)

# 9. insert - insere um item em um índice específico da lista
lista_insert = [4, 60, 2, 5, 10]
lista_insert.insert(0, 200)  # Insere 200 no índice 0
print( lista_insert)

# 10. pop - remove o item do final da lista
lista_pop = [4, 60, 2, 5, 10]
lista_pop.pop()
print( lista_pop)

# 11. pop(indice) - remove o item de um índice específico
lista_pop_indice = [4, 60, 2, 5, 10]
lista_pop_indice.pop(2)  # Remove o item no índice 2
print(lista_pop_indice)

# 12. remove - remove o item de acordo com o valor indicado
lista = [3, 200, 40, 6, 200, 6]
lista.remove(200)  # Remove a primeira ocorrência de 200
print(lista)

while 200 in lista:
    lista.remove(200)
print(lista)

4

#count - conta a quantidade de vezes que um item ocorre na lista
lista = [2, 5, 6, 7, 6, 10, 6]
print(lista.count(6))

#index - retorna o indice de um item
lista = [2, 5, 6, 7, 6, 10, 6]
valor = int(input('Digite um numero: '))
if valor in lista:
    print(lista.index(valor))
else:
    print('O valor nao esta na lista')

# exibe todos os indices onde um item se encontra
lista = [3, 200, 5, 200, 5, 6, 7,200]
for i in range(len(lista)):
    if lista[i] == 200:
        print(i)

# sort - ordena uma lista em ordem crescente
lista = [3, 200, 5, 200, 5, 6, 7, 200]
lista.sort()
print(lista)

# O mesmo pode ser feito com 'strings'
lista = ['maça', 'laranja', 'abacaxi','abc','teste']
lista.sort()
print(lista)

7
# Sort(reverese = True) ordena uma lista em ordem decrescente
lista = [3, 200, 5, 200, 5, 6, 7, 200]
lista.sort(reverse=True)
print(lista)

# sorted - retorna uma cópia de lista ordenada
lista = [4, 8, 1, 3, 19, 2]
listaordenada = sorted(lista)
print(listaordenada)

#min - menor item da lista
lista = [4, 8, 1, 3, 19, 2]
print(min(lista))

# max - retorna o maior item da lista
lista = [4, 8, 1, 3, 19, 2]
print(max(lista))

#sum - somatorio de uma lista
lista = [4, 8, 1, 3, 19, 2]
print(sum(lista))

#media dos itens da lista
media = sum(lista) / len(lista)
print(media)

#preencher uma lista com entradas do usuario
lista = []
for i in range(5):
    n = int(input('Numero: '))
    lista.append(n)
print(lista)


lista = []
while True:
    n = int(input('numero:'))
    if n == 0:
        break
    lista.append(n)
print(lista)