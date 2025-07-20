#Funcoes em python
"""
def boas_vindas():
    print("Ola seja bem vindo ao meu programa")


boas_vindas()

def dobro(num):
    d = num * 2
    return d

numero = dobro(4.5)
print(f'O dobro de {4.5} = {numero}')
"""
def nota(*args):
    for p in args:
        print(p)

nota(1,'Anna',3,'Eva',5,6,7,8,'Wilson')

def nota2(**kwargs):
    for k, v in kwargs.items():
        print(k + ' - ' + str(v))

nota2(nome='Wilson',sobrenome='Ventura',idade=26)
