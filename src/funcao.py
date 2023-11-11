#função com parâmetros
def saudacao(nome, curso):
    print(f'Seja bem-vinda(o) ao curso de {curso}!')
    print(f'É um prazer te conhecer, {nome}!')

#saudacao('Maria', 'Python')

#função com parâmetros default
def saudacao(nome, curso = 'Python'):
    print(f'Seja bem-vinda(o) do curso de {curso}!')
    print(f'É um prazer te conhecer, {nome}!')

#saudacao('Maria', 'C++')

#função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print(f'Resultado da soma: {resultado}')

def calculadora(num1, num2, operacao = '+'):
    if operacao == "+":
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == 'x':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

print("Resultado do cálculo:", calculadora(10, 20, '/'))