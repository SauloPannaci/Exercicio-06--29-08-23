class Escola:
    def __init__(self):
        self.alunos = {}  

    def cadastrar_aluno(self, matricula, nome, idade, nota):
    
        if matricula in self.alunos:
            print(f"Já existe um aluno cadastrado com a matrícula {matricula}.")
        else:
            
            aluno = {'nome': nome, 'idade': idade, 'nota': nota}
            
            self.alunos[matricula] = aluno
            print(f"Aluno {nome} cadastrado com sucesso.")

    def listar_alunos(self):
        print("\nLista de Alunos:")
        for matricula, aluno in self.alunos.items():
            print(f"Matrícula: {matricula}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")

    def excluir_aluno(self, matricula):
        
        if matricula in self.alunos:
            del self.alunos[matricula]
            print(f"Aluno com matrícula {matricula} excluído com sucesso.")
        else:
            print(f"Não existe aluno cadastrado com a matrícula {matricula}.")


escola = Escola()


escola.cadastrar_aluno(1, 'Leonardo', 20, 8.0)
escola.cadastrar_aluno(2, 'Gabriella', 7, 9.0)
escola.cadastrar_aluno(3, 'Raphaella', 11, 7.0)


escola.listar_alunos()


escola.excluir_aluno(2)


escola.listar_alunos()