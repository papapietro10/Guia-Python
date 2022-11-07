# Crear una app para calcular el IMC ( Indice de masa corporal )
# IMC = al peso / (altura)x(altura)

print (' Proporciona el peso:')
peso=input()

print('proporciona el valor de la altura')
altura= input()

# DOBLE PARENTICIS LE DA PRIORIDAD A LA CONSULTA 
imc=int(peso)/((float(altura))*(float(altura)))

print( 'su IMC es:', imc)