comps = trocas = passd = 0

 

def bubble_sort(lista):

    """

    ALGORITIMO DE ORDENAÇÃO BUBBLE SORT

    Percorre a lista a ser ordenada em sucessivas passadas,

    trocando entre si dois elementos adjacentes sempre que

    o segundo for MENOR que o primeiro. Efetua tantas

    passadas quanto necessárias, até que, na última delas,

    nenhuma troca tenha sido realizada.

    ESTA VERSÃO TEM UMA PEQUENA MODIFICAÇÃO QUE VAI DIMINUINDO 
    A QUANTIDADE DE COMPARAÇÕES A CADA PASSADA

    """

 

    # Usando as variaveis globais

    global comps, trocas, passd

    comps = trocas = passd = 0

 

    # Loop etrno, não sabemos de antemão quantas passadas

    # serão necessárias

    while True:

        # Inicio de uma nova passada

        passd += 1

 

        # Controla se houve troca na passada

        trocou = False

 

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento
        # com acesso a cada posição
        # Nas demais passadas, o percurso vai diminuindo uma posição

        for pos in range(len(lista) - passd):

         

          # Se o valor que está na frente na lista (pos + 1)

          # for MENOR do que aquele que está atrás (pos),

          # faz uma TROCA

          if lista[pos + 1] < lista[pos]:

             lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]

             trocou = True # Houve troca na passada

             trocas += 1

 

          # 0 if representa uma comparação

          comps +=1

   

        if not trocou:         # Não houve troca na passada

           break               # Interrompe o loop eterno

       

##########################################################################

 

# nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

 

# Melhor caso

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 9, 9]

 

# Pior caso

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("ANTES:", nums)

bubble_sort(nums)

print("DEPOIS:", nums)

print(F"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

#####################################################################
# TESTE COM ARQUIVO DE 1M+ NOMES

import sys
sys.dont_write_bytecode = True #impede criação de cache

#import lista nomes
from data.nomes_desord import nomes
from time import time

nomes1000 = nomes[:1000]

hora_ini = time()
bubble_sort(nomes1000)
hora_fim = time()
print(nomes1000)
print(f"tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

