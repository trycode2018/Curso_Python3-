def somar(*args):
    return sum(args)

a = somar(3,4,5,6)
print(a)

def mostrar_valores(**kwargs):
    for chave,valor in kwargs.items():
        print(f'{chave} : {valor}')

mostrar_valores(nome='Henrique',idade=13)