#for i in range(1, 12, 3):
#   print(i)

soma = 0
for i in range(1, 4):
    nota = float(input(f'Digite a nota {i}: '))
    soma += nota
media = soma / 3
print(media)