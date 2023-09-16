# Variaveis de estatica

# divs ~> número de divisões

# jucs ~> número de junções

# comps ~> número de comparações

divs = juncs = comps = 0

 

def merge_sort(lista):

    """

    ALGORITMO DE ORDENAÇÃO MERGE SORT

 

    No processo de ordenação, esse algoritmo "desmonta"

    a lista original, contendo N elementos, até obter

    N listas com apenas um elemento cada uma. Em seguida,

    usando a técnica de mesclagem (merging), "remonta" a

    lista, desta vez com os elementos já em ordem.

    """

    global divs, juncs, comps

 

    if len(lista) > 1:

 

        # encontra a posição do meio da lista, para fazer a divisão

        # em duas metades

        meio = len(lista) // 2

 

        # Tira uma cópia da primeira metade da lista

        sublista_esq = lista[:meio]

 

        # Tira uma cópia da segunda metade da lista

        sublista_dir = lista[meio:]

 

        divs += 1

 

        # Chamamos recursivamente a própria função

        # continue repartindo cada sublista em duas partes menores

        sublista_esq = merge_sort(sublista_esq)

        sublista_dir = merge_sort(sublista_dir)

 

        # PARTE 2: REMONTAGEM DA LISTA, ORDENADAMENTE

 

        pos_esq = pos_dir = 0

 

        ordenada = []  # Lista vazia

        # Compara os elementos das sublistas entre si e insere

        # na lista ordenada o menor dentre dois elementos

 

        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

 

            comps += 1

 

            # O menor elemento está na sublista da esquerda

            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:

 

                # "Desce" o elemento da esquerda para a lista ordenada

                ordenada.append(sublista_esq[pos_esq])

                pos_esq += 1  # Incrementa a posição esquerda

 

            # O menor elemento está na sublista da direita

            else:

                # "Desce" o elemento da direita para a lista ordenada

                ordenada.append(sublista_dir[pos_dir])

                pos_dir += 1  # Incrementa a posição da direita

 

        # Verificação da sobra

        sobra = []

 

        # Sobra à esquerda

        if pos_esq < pos_dir:

            sobra = sublista_esq[pos_esq:]

 

        # Sobra à direita

        else:

            sobra = sublista_dir[pos_dir:]

 

        juncs += 1

 

        # O resultado final é a junção (concatenação) da lista

        # ordenada com a sobra

        return ordenada + sobra

 

    else:

        return lista

 

########################################################################

 

#nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

nums = [2, 8, 0, 7, 1, 9, 4, 6, 5, 3]

 

nums_ord = merge_sort(nums)

print(f"lista original: {nums}")

print(f"lista ordenada: {nums_ord}")

print (f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")

 

#############################################################################

 

divs = juncs = comps = 0


from data.nomes_desord import nomes

from time import time

 

hora_ini = time()

merge_sort(nomes)

hora_fim = time()

print(nomes)

print(f"tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

print (f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")

