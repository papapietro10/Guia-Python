#Realiza una app que le pida al usuario una cantidad determinada de numeros 
#Muestre al usuario todos los numeros impares que existen en la longitud proporcionada

print( "Proporcione la longitud de numeros a evaluar:")
cantidad=int(input())
numero=1
print('Los siguientes numero son impares:')
while numero<cantidad:
    if((numero%2)!=0):
        print(numero)
    numero+=1