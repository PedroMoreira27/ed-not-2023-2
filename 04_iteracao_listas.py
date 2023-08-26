#lista de frutas
frutas = ["Laranja", "maçã" , "uva", "Pera" , "Mamão", "Abacate", "Amora"] 

#Para percorrer uma lista e exibir apenas seus elementos,
# usamos a estrutua for .. in, como ja já vimos no arquivo n° 02
for f in frutas:
    print(f)

print("-"*40)

#Imprimindo uma lista de trás para frente: reversal()
for x in reversed(frutas):
    print(x)

print("-"*40)

# No entanto, frequentemente precisamos exibir, além do
# valor do elemento, também sua posição. nesse caso devemos 
# usar a estrutura for .. in combinada com as funções range() e len ()
for pos in range(len(frutas)):
    # print(frutas[pos],':',pos)
    # print("A fruta", frutas[pos], "esta na posição", pos,".")
    print(f"A fruta {frutas[pos]} está na posição {pos}.")


print("-"*40)

# Ás vezes, é necessário percorrer a lista de trás para a frente, 
# mas tendo acesso também à posição dos elementos. para isso,
# usamos a estrutura for .. in, range() com três parâmetros e len()
for i in range(len(frutas)-1,-1,-1):
    print(f"A fruta {frutas[pos]} está na posição {pos}.")
