class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome 
        self.__matricula = matricula
        self.__cpf__ = cpf
        self.cursos_inscritos = [] # lsita dos cursos associados ao aluno

    # métodos de acesso
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # método de ação
    def increver_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self) # Assosia o aluno ao curso

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome_curso)
        return lista

class Curso:
    def __init__(self, nome_curso):
        self.__nome_curso = nome_curso  
        self.alunos_inscritos = []

    #métodos de ação
    def adicionar_aluno(self,aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self) # Associa o curso ao aluno

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome_aluno)
        return lista
   
     # método especial
    def __del__(self):
        print(f"Objeto {self.nome} destruido com sucesso.")