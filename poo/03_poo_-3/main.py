# classe 
class Pessoa:
    def __init__(self, nome, idade, email, profissao):
    # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    # método de ação
    def apresentar(self):
        print(f"Olá, eu me chamo {self.nome}, tenho {self.idade} anos, trabalho como {self.profissao} e meu e-mail é {self.email}.")

    # algoritmo principal 
    if __name__=="__main__":
    # instancia a classe
        usuario = "Pessoa"("",0,"","")

        try:
            # seta valores aos atributos do objeto
            usuario.nome = input("Informa o nome do usúario: ").title().strip()
            usuario.idade = int(input("Informa a idade: "))
            usuario.email = input("Informa o email: ").lower().strip()
            usuario.profissao = input("Informa sua profissao: ").strip()

            # executa o método
            usuario.apresentar()
        except Exception as e:
            print(f"Não foi possível executar o programa. {e}.")