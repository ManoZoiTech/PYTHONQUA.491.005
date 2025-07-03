from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name== "__main__":
    usuario = PessoaFisica(
        nome="",
        cpf="",
        profissao="",
        email="",
        telefone="",
        endereco="",
    )
    empresa = PessoaJuridica(
        razao_social="",
        nome_fantasia="",
        cnpj="",
        email="",
        telefone="",
        endereco="",
    )


print("Informe os dados do usário:\n")

usuario.nome = input("Informe o nome do usuario:").strip()



















dados_usuario = usuario

# saida de dados










print("Informe os dados da empresa:\n")

empresa.razao_social = input("Informe a razão social: ").strip().title()
empresa.razao_social = input("Informe a razão social: ").strip().title()
empresa.razao_social = input("Informe a razão social: ").strip().title()
empresa.razao_social = input("Informe a razão social: ").strip().title()
