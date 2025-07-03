# importações
import classes
import os

if __name__=="__main__":
    # instancia objeto
    usuario = classes.PessoaFisica("","","","","","")
    empresa = classes.PessoaJuridica("","","","","","")

    while True:
        print("1 - Inserir dados do usuário.")
        print("2 - Inserir dados da empresa.")
        print("3 - Mostrar dados.")
        print("4 - Sair do programa.")
        opcao = input("Informa a opção desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                try:
                    usuario.nome = input("Informe o nome do usúario: ").title().strip()
                    usuario.cpf = input("Informe o cpf: ").strip()
                    usuario.profissao = input("Informe a profissao: ").strip().title()
                    usuario.endereco = input("Informe o endereco: ").title().strip()
                    usuario.telefone = input("Informe o telefone: ").strip()
                    
                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados de {usuario.nome} inseridos com sucesso!")

                except Exception as e:
                    print(f"Não foi possivel inserir dados do usúario.{e}.") 
                finally:
                    continue

            case "2":
                try:
                    empresa.razao_social = input("Informe a razão social da empresa: ").title().strip()
                    empresa.nome_fantasia = input("Informe nome da empresa: ").title().strip()
                    empresa.cnpj = input("Informe o cnpj: ").strip()
                    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
                    empresa.endereco = input("Informe o endereco: ").strip().title()
                    empresa.telefone = input("Informe o telefone: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados da empresa {empresa.nome_fantasia} inseridos com sucesso!")
                except Exception as e:
                    print(f"Não foi possivel inserir dados da empresa. {e}.")
                finally:
                    continue

            case "3":
                try:
                    print(f"{'-'*20} DADOS DO USÚARIO {'-'*20}\n. ")
                    usuario.exibir_dados()
                    print(f"{'-'*20} DADOS DO USÚARIO {'-'*20}\n. ")
                    usuario.exibir_dados()
                except Exception as e:
                    print(f"Não foi possivel inserir dados do usúario.{e}.")
                                                     
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue