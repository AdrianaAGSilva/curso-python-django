class Aluno:
    def __init__(self, matricula, cpf, nome, curso, media):
        self.matricula = matricula
        self.cpf = cpf
        self.nome = nome
        self.curso = curso
        self.media = media

    def exibir_infor(self):
        print(f"Dados do aluno: {self.matricula} {self.cpf} {self.nome} {self.curso} {self.media}")

# Fim class Aluno

class Professor:
    def __init__(self, cpf, nome, titulação):
        self.cpf = cpf
        self.nome = nome
        self.titulacao = titulação

    def exibir_infor(self):
        print(f"Dados do professor: {self.nome} {self.cpf} {self.titulacao}")    

# Fim class Professor

class Turma:
    def __init__(self, curso, professor, lista_alunos):
        self.curso = curso
        self.professor = professor
        self.alunos = lista_alunos        
    
# Fim class Turma

professor = Professor(123456, "Claudio", "Mestre")
aluno1 = Aluno("abcd", 147258, "Adriana", "Python", 7)
aluno2 = Aluno("qwer", 456789, "Luciana", "Javascript", 9)
aluno3 = Aluno("sgfg", 789456, "Gabriela", "Html", 10)
lista_alunos = []
lista_alunos.append(aluno1)
lista_alunos.append(aluno2)
lista_alunos.append(aluno3)
turma_python = Turma("Python", professor, lista_alunos)

print(f"A turma de {turma_python.curso} é composta por:")
print(f"Professor: {turma_python.professor.nome}")
for aluno in turma_python.alunos:
    aluno.exibir_infor()
