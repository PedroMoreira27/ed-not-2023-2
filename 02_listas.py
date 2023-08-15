# LISTAS  
# Listas são uma forma de armazenar mais de um valor em uma unica variavel.
# Os valores podem ser de tipos diferentes

#Uma lista de Numeros
valores = [2,3,4,7,9,11]

#Uma lista com valores de tipos variados
mix = ["batata",1.25,True,"Tomate",44]

#lista de strings
legumes = ["batata", "tomate", "abobrinha", "cenoura"]

#OPERACOES SOBRE LISTAS 

#1) PERCURSO: significa percorrer a lista do primeiro 
#úlitmo elemento, fazendo algo com cada um deles

#imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-" * 40) #Traço de 40 hifens

#imprimindo o dobro do valor de cada elemento da lista
for x in valores:
    print(x*2)

print("-" * 40)
#2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA
valores.append(13)
legumes.append("Cebola")

print(valores)
print(legumes)
''
print("-" * 40)

#3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA
# Parâmetros:
# 1°: a posição onde será inserido o novo elemento
# 2°: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

valores.insert(1,30)
print(valores)

print("-" * 40)
#4) ACESSANDO  UM VALOR EM UMA POSIÇÃO ESPECIFICA
print("Elemento na quarta posição:" , valores[3])
print("Elemento na primeira posição:" , valores[0])
print("Elemento na ÚLTIMA posição: ", valores[-1])
print("Elemento na PENÚLTIMA posição: ", valores[-2])