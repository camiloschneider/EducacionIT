paises = {
  "ar": "Argentina",
  "es": "España",
  "us": "Estados Unidos",
  "fr": "Francia"
}
salir = False
while salir == False:
    codPais = input("Ingrese el codigo pais que busca:")
    if codPais == 'salir':
      salir == True
      break
    try:
      if codPais in paises:
        print(paises.get(codPais)) 
    except KeyError:
        codPais = input("Ingrese el codigo pais que busca:")


    


