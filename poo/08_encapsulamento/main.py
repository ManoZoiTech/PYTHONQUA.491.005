from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    return os.system("cls" if os.name == "nt" else "cls")

if __name__=="__main__":
    usuario = PessoaFisica(nome="",cnpj="", profissao="",email="",telefone="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia ="", cnpj="",email="",telefone="")

    print(f"{'-'*20}DADOS DO USÚARIO {'-'*20})
    usuario.nome = input("Informe o nome: ").title().strip()
    usuario.cpf = input("Informe o CPF: ").title().strip()
    usuario. = input("Informe o nome: ").title().strip()
    usuario. = input("Informe o nome: ").title().strip()
    usuario. = input("Informe o nome: ").title().strip()
    usuario. = input("Informe o nome: ").title().strip()
    usuario. = input("Informe o nome: ").title().strip()

    limpas()
    print(f"{'-'*20}DADOS DO USÚARIO {'-'*20})
    print(f"Nome: {usuario.nome}")
    print(f"Cpf: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"{'-'*20}DADOS DO EMPRESA {'-'*20})
    print(f"Nome: {usuario.nome}")
    print(f"Cpf: {usuario.cpf}")
    print(f"Profissão: {usuario.profissao}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}") 