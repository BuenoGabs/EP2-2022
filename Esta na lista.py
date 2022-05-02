'''Faça uma função 
que recebe o nome de país
 e uma lista de países e 
 retorna se o tal país está na lista ou não, 
 respectivamente: True ou False.'''



pais_entrada = 'libia'
lista = [
    ['libia', 3678],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]
#Saída: True
#lista_paises = []
#for info in lista:
    #paises = info[0]
    #lista_paises.append(paises)
#print(lista_paises)
#print(pais_entrada in lista_paises)
#print(pais in lista[0]) 
def alg(pais_entrada, lista):
    lista_paises = []
    for info in lista:
        paises = info[0]
        lista_paises.append(paises)
    return pais_entrada in lista_paises
print(alg(pais_entrada,lista))