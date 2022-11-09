# * se utiliza para meter todo lo que sobra en la tupla en una variable 
marcasCarros=('mazsa','forter','ferrari','bmw')


(marca1,marca2,*marca3)=marcasCarros


print(marca1)
print(marca2)
print(marca3)