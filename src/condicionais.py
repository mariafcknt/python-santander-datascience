'''idade = 18

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")'''

media = float(input('Informe a média do estudante: '))
presenca = float(input('Digite a porcentagem de presença: '))

if media >= 7 and presenca >= 70:
    print('Aprovado!')
    print('Parabéns!')
elif media >= 5 and presenca >= 70:
    print('Recuperação')
else:
    print('Reprovado.')
    print('Tente novamente')
