notas = [7.9, 9.7, 8.2]

lista = []
lista = list()

lista_de_listas = [10, [1, 2, 3]]

#Indexaçãop e Slices (Fatiamento)

lista = [26, 'Maria', 3.14, False]
print(lista[0])

#Último elemento da lista
print(lista[-1])

lista = [10, 50, 30, 40, 25, 60, 5]

#posições de 0 até < 3 na lista
print(lista[0:3])

#2 até < 6 pulando de 2 em 2
print(lista[2:6:2])

#todos a partir do 3 (incluso)
print(lista[3:])

# Leitura da lista
for elemento in lista:
    print(elemento)

print('Tamanho da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])

