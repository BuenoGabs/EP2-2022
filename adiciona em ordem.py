pais = "siria"
distancia = 5919
lista = [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]
pais_a_adicionar = [pais,distancia]
for elemento in lista:
    distancias = elemento[1]
    
lista.insert(0,pais_a_adicionar)
print(lista)
#lista.insert(0,pais_a_adicionar)
#print(pais_a_adicionar)
#lista.insert(0,pais_a_adicionar)
#print(lista)