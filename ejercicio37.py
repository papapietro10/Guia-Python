#Ejerccio de condicional
# Comparar 2 edades e indicar que edad es mayor, menor o igual con respecto a los datos ingresados
#Edad de pedro 
#Edad de Carlos

print("Escriba la edad de pedro")
edadPedro=int(input())
print("Escriba la edad de Carlos")
edadCarlos=int(input())

if edadPedro > edadCarlos:
    print('Pedro es mayor que carlos')
elif edadPedro == edadCarlos:
    print('Carlos y Pedro tienen la misma edad')
else:
    print('Carlor es mayor que pedro')