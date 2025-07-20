import soma, subtrair, multiplicar, dividir

num1 = input('Digite o primeiro numero : ')
num2 = input('Digite o segundo numero :')

sum = soma.somar(int(num1),int(num2))
dif = subtrair.subtracao(int(num1),int(num2))
mult = multiplicar.multiplicar(float(num1),int(num2))
div = dividir.divisao(float(num1),float(num2))

print()
print('BEM VINDO A MINHA CALCULADORA EM PYTHON')
print()

print(f'A soma de {num1} + {num2} = {sum}')
print(f'A subtracao de {num1} - {num2} = {dif}')
print(f'A multiplicacao de {num1} * {num2} = {mult}')
print(f'A divisao de {num1} / {num2} = {div}')


