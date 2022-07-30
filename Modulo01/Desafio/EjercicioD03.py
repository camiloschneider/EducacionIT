"""
Crear una función que reciba un número como
argumento, ese número representará los segundos
que se quieren convertir a horas, minutos y segundos.
Por ejemplo, conversion(3600) retornaría el texto
“01:00:00” , en cambio si recibe 1000, devolverá
“00:16:40”
No se puede usar ninguna función built-in, ni
tampoco ningún módulo que haga la conversión. 
"""

def conversion(num):   
     seg = int(num % 60)
     minuts = int(num%3600/60)
     hours = int(num/3600)
     if seg < 10:
      segs = "0" + str(seg) 
     else:
        segs = str(seg)
     if minuts < 10:
      mins = "0" +str(minuts)
     else:
      mins = str(minuts)
     if hours < 10:
      hourss = "0" +str(hours)
     else:
      hourss = str(hours)
     return  f'{hourss} : {mins} : {segs}'

print(conversion(4700))