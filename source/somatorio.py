def multiplicar(*argumentos):
    resultado = 1
    for n in argumentos:
        resultado*=n
    return resultado

print(multiplicar(2, 3, 4))
