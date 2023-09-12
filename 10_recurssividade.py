"""
    RECURSIVIDADE   

    Trata-se de uma técnica de programação pela qual uma função
    chama a si mesma, em uma condição diferente da inicial. O
    principal objetivo do uso da recursividade é diminuir a 
    coplexidade de algoritmos.
"""

def fatorial_iter(num):
    """
    Calcula o fatorial de um número, usando um algoritmo
    ITERATIVO (não recursivo)
    """

    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossivel")

    resposta = 1
    for n in range(num, 0, -1): resposta *= n 
    
    return resposta

def fatorial_rec(num):
    """
        Cálculo do fatorial, usando um algoritmo RECURSIVO
    """
    # não é possivel calcular o fatorial de um número negativo
    if num < 0:
        raise Exception("ERRO: número negativo, calculo impossivel")

    if num <= 1: return 1       # fatorial de 0 é igual a 1
    else: return num * fatorial_rec(num-1)     # chamada recursiva à função

#####################################################

print(f"Fatorial de 6 (recursivo): {fatorial_rec(6)}")
print(f"Fatorial de 6 (iterativo): {fatorial_iter(6)}")