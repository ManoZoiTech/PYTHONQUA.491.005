#biblioteca
import classes
import os

#algoritmo
if __name__ =="__main__":
    # instancia de objetos
    usuario = classes.PessoaFisica("","","","","","","")
    empresa = classes.PessoaJuridica("","","","","","")

    #limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores ao objeto do tipo Pessoa Física
    print(f"{'-'*20} DADOS DO USÁRIO {'-'*20}\n")

    usuario.nome = input("Informe seu nome: ").title().strip()
    usuario.cpf = input("Informe seu cpf: ").strip()
    usuario.profissao = input("Informe seu profissão: ").strip()
    usuario.genero = input("Informe seu gênero: ").strip()
    usuario.email = input("Informe seu e-mail: ").strip().lower()
    usuario.endereço = input("Informe seu endereço: ").strip().title()
    usuario.telefone = input("Informe seu telefone: ").strip()

#limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

# atribui valores ao objeto do tipo Pessoa Juridica
    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")


    empresa.razao_social = input("Informe seu nome: ").title().strip()
    empresa.nome_fantasia = input("Informe seu nome: ").title().strip()
    empresa.cnpj = input("Informe seu nome: ").strip()
    empresa.email = input("Informe seu nome: ").strip().lower()
    empresa.endereço = input("Informe seu nome: ").strip().title()
    empresa.telefone = input("Informe seu nome: ").strip()

#limpar a tela
    os.system("cls" if os.name == "nt" else "clear")

# exibir os dados do usário e da empresa
    print("Dados do usúario:\n")
    usuario.exibir_dados()
    print("Dados da empresa:\n")
    usuario.exibir_dados()