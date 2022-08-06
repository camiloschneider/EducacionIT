print("Bienvenido a Hamburguesas IT")

encargado = input("Ingrese su nombre encargad@:")
while True:
  print(f"Encargad@ ---> {encargado}")
  print(f"{encargado} recuerda, siempre hay que recibir al cliente con una sonrisa :)")

  print("1 - Ingreso nuevo pedido")
  print("2 - Cambio de turno")
  print("3 - Apagar sistema")

  elec = int(input("Elige la opcion que desea: "))

  if elec == 1 :
    ComboSimple = 5
    ComboDoble = 6
    ComboTriple = 7
    McFlurby = 2
  
    total = 0
    cliente = input("Ingrese nombre del cliente: ")
    cantComboS = int(input("Ingrese   cantidad Combo Simple: "))
    cantComboD = int(input("Ingrese cantidad Combo Doble: "))
    cantComboT = int(input("Ingrese cantidad Combo Triple: "))
    cantFlurby = int(input("Ingrese cantidad Flurby: "))
  
    tCantComboS = ComboSimple * cantComboS
    tCantComboD = ComboDoble * cantComboD
    tCantComboT = ComboTriple * cantComboT
    tCantFlurby = McFlurby * cantFlurby
  
    total = tCantComboS + tCantComboD + tCantComboT + tCantFlurby
  
    print(f"Total $ {total}")
    pagoEfectivo = int(input("Abona con $ "))
    vuelto = pagoEfectivo - total
    print(f"Vuelto $ {vuelto}")
  
    confirmacion = input("¿Confirma pedido? Y/N: ")
  
    if confirmacion == "Y":
      with open("ProyectoIntegrador/ventas.txt", "w") as f:
        f.write(cliente)
  

  