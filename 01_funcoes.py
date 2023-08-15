def calc_imc(peso, altura):
    return peso / (altura ** 2)
p = float(input("Qual seu peso?: "));
a = float(input("Qual sua altura?: "));
imc = calc_imc(p,a)

print(imc)
#################################################
from math import pi
"""
    Função que calcula a área de uma figura geometrica plana

"""

def calc_area(base,altura,tipo):
    resultado = None
    if tipo == 'R': #Retangulo
        resultado = base * altura 
    elif tipo == 'T':
        resultado = (base * altura)/2
    elif tipo == 'E': 
        resultado = (base/2)*(altura/2)*pi
    return resultado            
print("Retangulo 20x30: ", calc_area(20,30,'R'))

print("Triangulo 20x30: ", calc_area(45,32,'T'))

print("Elipse 20x30: ", calc_area(10,15,'E'))

print("Desconhecido 12x16: ", calc_area(12,16,"X"))