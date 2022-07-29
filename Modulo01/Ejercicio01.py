"""Sumatoria:
          Crear un bucle que almacene en una variable la suma
          de todos los elementos numericos de una lista, con
          excepcion del ultimo
"""
# Creamos la lista a utilizar
lista = [1,2,3,4,5,6,7,8,9,10]

#Creamos la variable que utilizaremos luego en el ciclo para almacenar la suma de los valores de la lista creada anteriormente
sum = 0

#Creamos el for en el cual con la variable i recorremos nuestra lista, en la cual estamos indicando que recorra toda la lista con excepcion el ultimo valor [:-1] 
for i in lista[:-1]:       
        sum = sum + i
          
#Mostramos el resultado
print(sum)
