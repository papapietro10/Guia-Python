#Crear una aplicacion que le solicite al usuario una cantidad de numeros a ongresar a una lista 
#Posterior mente imprimir dicha lista 

print('agrega cuantos productos quieres')
agregarUno=input()

#indicar elementos de alamcenar
contador=1
lista=[]

#Leer los datos  ( cantidad de numeros solicitados )
while contador<=int(agregarUno):
    print('agrga un numeor'+str(contador)+':')
    agregarDos=input()
    lista.append(int(agregarDos))
    contador+=1
    print(lista)

