def calcular(*args):
    media = soma = 0
    for n in args:
        soma+=n
    media = soma/len(args)
    return media

print(calcular(5,10,5))