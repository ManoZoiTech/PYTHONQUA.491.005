# biblioteca
import os 
import modulo

# algoritmo principal
while True:
    try:
        # menu
        print("1 - Somar")
        print("2 - subtrair")
        print("3 - multiplicar")
        print("4 - Dividir")
        print("5 - Sair do programa")
        opcao = input("informe a oprcação desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            x = float(input("Indorme o valor de x: ").replace(",", "."))
            y = float(input("Indorme o valor de y: ").replace(",", "."))
        match opcao:
            case"1":
                result = modulo.somar(x,y) # type: ignore
                print(f"O valor da é{result}.")
            case"2":
                result = modulo.subtrair(x,y) # type: ignore
                print(f"O valor da é{result}.")
            case"3":
                result = modulo.multiplicar(x,y) # type: ignore
                print(f"O valor da é{result}.")
            case"4":
                result = modulo.dividir(x,y) # type: ignore
                print(f"O valor da é{result}.")
            case"5":
                print("Operação inváçida.")
                continue
    except Exception as e:
        print(f"Não foi possivel calcular. {e}.")
        continue
        