nome = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')
sexo = input('Digite seu sexo: ')

idade = int(idade_usuario)

if (idade>=18) and (sexo.lower() == 'masculino'):
    print(f'{nome}, você é um homem adulto.')
elif (idade>=18) and (sexo.lower() == 'feminino'):
    print(f'{nome}, você é uma mulher adulta.')
else:
    print(f'{nome}, você é menor de idade ou não se identificou corretamente.')