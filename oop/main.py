from alunos import Aluno
from professores import Professor

aluno = Aluno('Henrique Ventura',26,'Informatica')
professor = Professor('Gildo Zage',31,'Matematica')

print(f'O aluno {aluno.nome} tem aulas de {professor.disciplina} com o professor {professor.nome}')

