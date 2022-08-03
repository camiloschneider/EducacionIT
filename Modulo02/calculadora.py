
try:
  num01 = int(input("Ingrese un numero: "))
  num02 = int(input("Ingrese otro numero: "))   

  suma = lambda n,nn: n + nn
  resta = lambda n,nn: n - nn
  mult = lambda n, nn: n * nn
  division = lambda n,nn:n/nn


  print(f'la suma es:{suma(num01,num02)}, la resta es:{resta(num01,num02)}, la multiplicacion es:{mult(num01,num02)}, la division es:{division(num01,num02)}')
except ValueError as ve:
    print("Por favor ingresar valores numericos en cada campo solicitado")
    num01 = int(input("Ingrese un numero: "))
    num02 = int(input("Ingrese otro numero: "))   
    suma = lambda n,nn: n + nn
    resta = lambda n,nn: n - nn
    mult = lambda n, nn: n * nn
    division = lambda n,nn:n/nn


    print(f'la suma es:{suma(num01,num02)}, la resta es:{resta(num01,num02)}, la multiplicacion es:{mult(num01,num02)}, la division es:{division(num01,num02)}')
    
except ZeroDivisionError as ze:
    print("No se puede dividir por cero")