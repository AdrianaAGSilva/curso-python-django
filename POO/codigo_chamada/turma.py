class Turma:
    def __init__(self, codigo, professor):
        self.codigo = codigo
        self.professor = professor
        self.alunos = []  # Lista para armazenar alunos

    def matricular_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            return f"Aluno {aluno.nome} matriculado na turma {self.codigo}."
        return f"Aluno {aluno.nome} já está matriculado na turma {self.codigo}."

    def listar_frequencia(self):
        resultado = f"Frequência da turma {self.codigo}:\n"
        for aluno in self.alunos:
            resultado += aluno.consultar_frequencia() + "\n"
        return resultado
    
    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            return f"Aluno {aluno.nome} removido da turma {self.codigo}."
        return f"Aluno {aluno.nome} não está na turma {self.codigo}."
    
    def substituir_professor(self, novo_professor):
        self.professor = novo_professor
        return f"Professor da turma {self.codigo} substituído por {self.professor.nome}."
    
    def aluno_mais_frequente(self):
        if not self.alunos:
            return "Negum aluno matriculado na turma"
        
        aluno_mais = self.alunos[0]
        for aluno in self.alunos[1:]:
            if len (aluno.presenca) > len(aluno_mais.presenca):
                aluno_mais = aluno
        return f"Aluno com mais frequência: {aluno_mais.nome} ({len(aluno_mais.presencas)} presencas)."