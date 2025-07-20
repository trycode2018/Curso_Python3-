lista = [1,2,3,4,5,6,7,8,9,10,11,12]

"""
for x in lista:
    for y in range(1,11):
        print(f'{x} * {y} = {x*y}')
    print()
"""
print(lista)

personagem = {'nome':"Henrique Ventura",
              'idade':25,
              'formacao':
              ['Tecnico de Informatica','Engenharia de Informatica']
             }

print(personagem)
print(personagem['nome'])
print(personagem.get('formacao')[1])

print(type(personagem))

for v in personagem.values():
    print(v)

personagem['formacao'].append('Tecnico de IT')
print(personagem)
#p = new Pessoa('Wilson',12)

class Pessoa:
    print('ola classe')
    def Pessoa(nome,idade):
        print(123)