"""
Cree una función llamada “superior”, que reciba por
argumento una función y una lista. La función que se
pasa por argumento a superior debe elevar al cubo un
número y retornarlo. Para que luego al aplicarla en la
de orden superior, esa operación se realice miembro
a miembro de la lista.
Para finalizar la función “superior” debe de devolver
una nueva lista.
"""


def cubo(num):
  return num ** 3


def superior(funcion, lista):
  resultList = []
  for i in lista:
    resultList.append(funcion(i))
  return resultList

numeros = [2,3,5]

print(superior(cubo, numeros ))