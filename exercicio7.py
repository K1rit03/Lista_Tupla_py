lista = []
for i in range(5):
    n = int(input('Insira 5 numeros: '))
    lista.append(n)
    media = sum(lista) / len(lista) 

print(max(lista))
print(min(lista))
print(media)


