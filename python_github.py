
lista = [15,"Nombre",3.1415,True]

print(lista[0])

usuario = ["usernameTest1","pass123","correo@correo.com"]

numeros = [10,50,100,255,500]

numeros.append(1000)
print(numeros)

#extend = 
extra = [75,350,999]
numeros.extend(extra)
print(numeros)

#insert = agrega valor en lugares especificos
numeros.insert(6,5000)
print(numeros)

#remove = elimina un numero en especial
numeros.remove(50)
print(numeros)

#pop = elimina el ultimo numero
#pop(i) = elimina la posicion del numero
numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)

#reverse = invierte el orden de la lista
numeros.reverse()
print(numeros)

#sort = ordena valores de menor a mayor
numeros.sort()
print(numeros)

#sort=(reverse=True) = odena los valores de mayor a menor
numeros.sort(reverse=True)
print(numeros)
