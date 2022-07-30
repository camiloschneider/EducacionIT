"""
Tenemos una lista donde se registran los ingresos del
personal a un sistema:
personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
Contar los ingresos en un diccionario. La clave debería
de ser el nombre y el valor debería ser la cantidad de
ingresos.
"""
list_personas = ["Carlos", "Emilia", "Alejandro", "Maria", "Hugo"]
ing_personal = [60000, 78000, 47000, 128000, 92000]

dict_ingresos = dict(zip(list_personas,ing_personal))
print(dict_ingresos)
