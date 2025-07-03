# importações
import classes 
import os

# algoritmo principal
if __name__ =="__main__":
    # instancia a classe Filho
    filho = classes.Filho("","","","",0.0,0.0)

try:
    # input
    filho.nome = input("Informe o nome: ").strip().title()
    filho.email = input("Informe o e-mail: ").strip().lower()
    filho.telefone = input("Informe o telefone: ").strip()
    filho.genero = input("Informe o gênero: ").strip()
    filho.peso = float(input("Informe o peso: ").strip().replace(",","."))
    filho.altura = float(input("Informe o altura: ").strip().replace(",","."))

    os.system("cls" if os.name == "nt" else "cls")

# output
    filho.exibir_info()
except Exception as e:
        print(f"Não foi possivel executar. {e}.")