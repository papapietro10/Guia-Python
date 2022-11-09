# DE esta forma se puedemodificar una tupla usando la etiquta list y tuple 

marcasCarros=('mazsa','for','ferrari','bmw')
print(marcasCarros)
listaMarcaCarros= list(marcasCarros)
listaMarcaCarros.append('coco')
marcasCarros=tuple(listaMarcaCarros)
print(marcasCarros)
