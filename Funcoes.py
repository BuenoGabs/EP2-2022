from  math import * 
import random
#normaliza base
def normaliza(dict_entrada):
    dict_retorno = {}
    for continente, infos in dict_entrada.items():
        for pais, dados in infos.items():
            dict_retorno[pais] = dados
            dict_retorno[pais]["continente"] = continente
    return dict_retorno

#sorteia pais
def sorteia_pais(dict_entrada):
    lista_paises = []
    for paises,info in dict_entrada.items():
        lista_paises.append(paises)
    return(random.choice(lista_paises))

#distancia de haversine
def haversine(raio,omega1,lambda1,omega2,lambda2):
    omega1_r = radians(omega1)
    lambda1_r = radians(lambda1)
    omega2_r = radians(omega2)
    lambda2_r = radians(lambda2)
    d1 = sin(omega2_r-omega1_r/2)**2 + cos(omega1_r) * cos(omega2_r) * sin(lambda2_r-lambda1_r/2)**2
    d2 = sqrt(d1)
    distancia = 2*raio*asin(d2)
    return degrees(distancia)

#adiciona em ordem
def adiciona_em_ordem(pais, distancia, lista_de_paises):
    if len(lista_de_paises) == 0:
        return [[pais, distancia]]
    if distancia > lista_de_paises[-1][1]:
        lista_de_paises.append([pais, distancia])
    for el in range(len(lista_de_paises)):
        if pais == lista_de_paises[el][0]:
            return lista_de_paises
        elif distancia < lista_de_paises[el][1]:
            lista_de_paises.insert(el, [pais, distancia])
            return lista_de_paises

#está na lista
def esta_na_lista(pais_entrada, lista):
    lista_paises = []
    for info in lista:
        paises = info[0]
        lista_paises.append(paises)
    return pais_entrada in lista_paises

#sorteia com restrições 
#funciona no vs e no pythutor 
def sorteia_letra(palavra, lista_restrita):
    #tratamento da palavra:
    palavra= palavra.replace(" ","")
    palavra =''.join(letra for letra in palavra if letra.isalnum())
    palavra= palavra.lower()

    for i in palavra:
        for r in lista_restrita:
            if i == r:
                palavra= palavra.replace(i,"")
            if palavra == "":
                return ('')
   
    sorteada= random.randint(0,len(palavra)-1)
    palavra[sorteada]
    return(palavra[sorteada])
print(sorteia_letra("Cabul", ['a', 'c', 'b', 'l', 'u']))