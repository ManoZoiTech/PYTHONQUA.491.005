# funções:
import math

def equacao_1_grau(a, b): 
    x = -b/a 
    return x 

def equacao_2_grau(a, b, c): # type: ignore
    # a a*x²+b*x+c = 0
    delta = (b**2)-(4*a*b)
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        yield f"x' = {x1}"
        yield f'x" = {x2}'
    elif delta == 0:
        x = -b/(2*a)
        yield f"x = {x}"
    else:
        yield "Não há raízes reais."

    

"""
# TODO - Crie um programa que calcule a equação do 1° grau.
# NOTE - Coloque um menu para o usuário decidir se quer calcular a equação ou sair do programa.
# NOTE - Coloque no menu a opção de calcular a equação do 2° grau
(não precisa desenvolver essa função por enquanto).
# NOTE - faça usando o conceito de módulo recém-ensinado,usando o commando ' import equacoes' no main,py
"""