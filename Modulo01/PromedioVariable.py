"""Construir una función que se llame “promedio_variable”.
Esta función debe tomar un número arbitrario de
argumentos numéricos y devolver el promedio."""

def promedio_variable(*args):
  total = 0
  totalPromedio = 0
  acum = len(args)
  for x in args:
    total += x
    totalPromedio = total / acum
  return totalPromedio

print(promedio_variable(2,3,4))