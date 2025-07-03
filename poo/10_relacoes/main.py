from classes import Aluno, Curso 
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__=="__main__": 
    alunos = []
    cursos = [] 
    matricula = 0
    
while True:
    aluno = aluno(nome="", matricula=0, cpf="")
    curso = curso(nome_curso="")

    print(f"{'-'*20} SISTEMA ESCOLAR {'-'*20}")
    print("1 - Cadastrar Aluno.")
    print("2 - Cadastrar Curso.")
    print("3 - Matricula aluno curso.")
    print("4 - Listar curso.")
    print("5 - Listar Aluno.")
    print("6 - Sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()

    limpar()
    match opcao:
        case"1":
            try:
                matricula == 1
                aluno.nome = input("Informe o nome do aluno: ").strip().title()
                aluno.cpf = input("Informe o CPF do aluno: ").strip()
                aluno.matricula = matricula

                alunos.append(aluno)
                print(f"Aluno {aluno.nome} matriculado com sucesso;")
            except Exception as e:
                 print(f"Não foi possivel cadastrar aluno. {e}.")
            finally:
                continue
        case"2":
            try:
                curso.nome_curso = input("Informe o curso: ").strip().title()

                curso.append(curso)
                limpar()

                print(f"curso {curso.nome_curso} cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possivel o curso. {e}.").strip().title()
            finally:
                continue
        case"3":
            try:
                print(f"{'-'*10} LISTA DE ALUNOS {'-'*10}")
                print(f"Nome: - {aluno.nome}.")
                print(f"Matrícula: - {aluno.matricula}.")
                print(f"CPF: - {aluno.cpf}.")
                print('-'*40)
                inscricao = int(input("Informe a matricula: "))
                for aluno in alunos:
                    aluno = {
                        'nome': aluno.nome,
                        'matricula': aluno.matricula,
                        'cpf': aluno.cpf
                    }
                    
                    if inscricao in alunos['matricula']:                        break
                    else:
                        ...
                    limpar()

                print(f"{'-'*10} lista de curso {'-'*10}")
                for curso in cursos:

                    print(f"Curso: {curso.nome_curso}")
                curso_inscricao = input("Curso desejado:").strip().title()

                aluno.inscrever_curso(curso_inscricao)
                limpar()

                print(f"Aluno {aluno.nome} inscrito no curso {curso.nome_curso} com sucesso.")
                # else:
                #     print("Não foi possivel encontrar a matrícula.")
            except Exception as e:
                print(f"Não foi possivel o curso. {e}.").strip().title()
            finally:
                continue                        
        case"4":
            cursos.nome_cursos.sort()
            for curso in cursos:
                print(f"Cursos: {curso.nome_curso}")
                print("Alunos:")
                curso.listar_alunos().sort()
                for aluno in curso.listar_alunos():
                    print(aluno)
                print('-'*40)
        case"5":
           alunos.nome.sort()
           for aluno in alunos:
                print(f"Nome: {aluno.nome}")
                print(f"Matrícula: {aluno.matricula}")
                print(f"CPF: {aluno.cpf}")
                print("Cursos matriculados: ")
                aluno.listar_cursos().sort()
                for curso in aluno.listar_cursos():
                    print(curso)
                print('-'*40)
               
        case"6":
            print("Programa encerrado.")
            break
        case _:
              print("Opção inválida.")
              continue
    
    
    
    # alunos   
    # aluno01 = Aluno("Fulano",101, "157.157.157-98")
    # aluno02 = Aluno("Fulano",102, "158.158.158-98")
    # aluno03 = Aluno("Fulano",103, "159.159.159-98")
    # aluno04 = Aluno("Fulano",104, "154.154.154-98")
    # aluno05 = Aluno("Fulano",105, "155.155.155-95")
    # aluno06 = Aluno("Fulano",104, "156.156.156-98")
    
    # # curso
    # curso01 = curso("Python Developer")
    # curso02 = curso("IA com Python ")
    # curso03 = curso("Desenvolvedor Java")

    # # inscrevendo os alunos no cursos
    # aluno01.inscrever_curso(curso01)
    # aluno02.inscrever_curso(curso01)
    # aluno03.inscrever_curso(curso01)

    # aluno04.inscrever_curso(curso02)
    # aluno05.inscrever_curso(curso02)

    # aluno06.inscrever_curso(curso03)

    # # mostrar alunos nos cursos
    # print(f"Curso {curso01.nome_curso} tem os alunos: {curso01.listar_alunos()}.")