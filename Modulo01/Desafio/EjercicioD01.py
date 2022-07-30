"""
Dada 2 listas con números enteros, crear una tercera con los
números que pertenecen a ambas. Pero con la salvedad que
en esta tercera no debe tener elementos repetidos.
primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
Usar únicamente sentencias de control: condicionales y bucles.
También es probable que tengas que usar el operador de
pertenecía.
"""


list_1 = [2,3,5,6,7,8,8,7,2,9]
list_2 = [3,4,6,7,8,9]

list_3 = []
for i  in list_1 + list_2:
  if i not in list_3:
    list_3.append(i)
    list_3.sort()
 
print(list_3)