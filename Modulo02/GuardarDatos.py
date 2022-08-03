"""Cree un algoritmo para guarda cada una de las
personas del diccionario personas en un txt.
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
El nombre se tiene que guardar en minúsculas y
cada persona debe quedar en un renglón con un
guión del medio separando el nombre y la edad.
Ejemplo dentro del personas.txt se tendría que ver:
roberto-20
romina-32
"""

persona={"Juan": 20, "Romina": 32, "Tamara": 25, "Melanie": 19}


with open("Modulo02/personas.txt", "w") as f: 
  for n in persona:
    nc = str(persona.get(n))
    relleno = "{0} - {1}".format(n,nc)
    
    f.write('\n' + relleno.lower())
