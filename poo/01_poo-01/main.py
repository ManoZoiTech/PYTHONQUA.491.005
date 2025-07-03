# classe 
class Pessoa:
    # atributos
    nome = "Mano Zoi"
    idade = 25
    email = "manozoi@gmail.com"
    profissao = "programador"

# algoritmo principal
if __name__=="__main__":
    # instancia a classe Pessoa (cria objeto da classe)
    usuario = Pessoa()

    # exibe na tela os dados do usuário
    print(f"Nome:{usuario.nome}")
    print(f"Idade:{usuario.Idade}")
    print(f"email:{usuario.email}")
    print(f"profissao:{usuario.profissao}")