# biblioteca
import os
import equacoes as eq

# algaritmo principal:
if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular equação do 1°grau.")
            print("2 - Calcular equação do 2°grau.")
            print("3 - Sair do programa.")
            opcao = input("Informe a operação desejada: ").strip()

            os.system("cls" if os.name == "nt" else "clear")
            match opcao:
                case"1":
                    a = float(input("Informe o valor de 'a':").replace(",","."))
                    b = float(input("Informe o valor de 'b':").replace(",","."))
                    result = eq.equacao_1_grau(a,b) # type: ignore
                    print(f"{a}x = {b} = 0")
                    print(f"x = {result}")
                    continue
                case"2":
                    a = float(input("Informe o valor de 'a':").replace(",","."))
                    b = float(input("Informe o valor de 'b':").replace(",","."))
                    c = float(input("Informe o valor de 'c':").replace(",","."))
                    os.system("cls" if os.name == "nt" else "clear")
                    result = eq.equacao_2_grau(a, b, c) # type: ignore
                    for x in result:
                        print(x)
                    continue
                case"3":
                    print("Programa encerrado")
                case _:
                    print("Operação inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível calcular. {e}.")
            continue