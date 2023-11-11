lista = [1, 3, 12, 8, 2]

#append
print('Antes:', lista)
lista.append(3)
print('Depois:', lista)

#insert
#(índice, elemento)
lista.insert(2, 10)
print(lista)

#extend
#concatena duas listas
#lista2 = [1, 2, 3]
#lista.extend(lista)

#pop
#remove o elemento no índice informado ou remove o último
lista.pop(0)
print('Lista após o pop:', lista)

#remove
#remove o elemento informado (não o índice)
#remove apenas o primeiro elemento encontrado
lista.remove(3)
print(lista)

#count
#conta a quantidade de elementos na lista
print('Quantidade de 2 na lista:', lista.count(2))

#index
#acha o index pelo elemento
print(lista.index(10))

#sort
#ordena a lista em ordem crescente
lista.sort()
#ordem decrescente
lista.sort(reverse=True)
print(lista)

#len
#tamanho da lista
print(len(lista))

#sum
#soma dos elementos da lista
print(sum(lista))

#max
#maior elemento da lista
print('Maior elemento:', max(lista))

#min
#menor elemento da lista
print('Menor elemento:', min(lista))