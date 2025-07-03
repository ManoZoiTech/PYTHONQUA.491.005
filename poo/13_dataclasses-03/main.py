from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.sustem("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(nome="",profissao="",genero="",email="", telefone="", endereco="",)
     empresa = PessoaJuridica(nome_fantasia="",cnpj="",website="",email="", telefone="", endereco="",)
    
    limpar()

    print(f"{'-'*10} DADOS DO USÚARIO {'-'*10}")
    usuario.nome = input("Informe o nome do usúario: ").strip().title()
    usuario.profissao = input("Informe a profissao do usúario: ").strip().title()
    usuario.genero = input("Informe o gênero do usúario: ").strip()
    usuario.email = input("Informe o e-mail do usúario: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usúario: ").strip()
    usuario.endereco = input("Informe o endereço do usúario: ").strip().title()

    limpar()
    
    print(f"{'-'*20} DADOS DO USÚARIO {'-'*20}")
    usuario.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    usuario.cnpj = input("Informe a profissao do usúario: ").strip().title()
    usuario.website = input("Informe o website da empresa: ").strip()
    usuario.email = input("Informe o e-mail da empresa: ").strip().lower()
    usuario.telefone = input("Informe o telefone da empresa: ").strip()
    usuario.endereco = input("Informe o endereço da empresa: ").strip().title()

limpar()

#saida de dados
print(f"{usuario}. Segue meus dados:")
usuario.exibir_dados()
print(f"{empresa}. Segue os dados da empresa:")

# destrói os objetos
del(usuario)
del(empresa)

