"""Mostrar y eliminar:
          Utilizando un bucle while, elaborar un codigo que imprima
          en pantalla cada uno de los elementos de una lista y simultaneamente
          los elimine, hasta quedar vacia   
      """

#Creamos la lista a utilizar en este ejercicio
lista = [1,2,3,4,5,6,7,8,9,10]

#Creamos el bucle while en el cual utilizamos el metodo len en nuestra lista para obtener la longitud de misma
#Mientras la longitud de nuestra lista sea mayor a 0, nos va a recorrer la lista y luego eliminamos los valores de la lista
while len(lista) > 0:
       print(lista[0:])
       del lista[0:]

#Mostramos la lista vacia
print(lista) 