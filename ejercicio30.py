# Format se utiliza para completar con variables un string 

cantidad=3
numeroID=10
precio=59.90

precioDeVenta='El producto vale {} y son {} productos el numero de control es {}'

print(precioDeVenta.format(precio,cantidad,numeroID))