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
print(adiciona_em_ordem('siria', 5919,
[
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]))