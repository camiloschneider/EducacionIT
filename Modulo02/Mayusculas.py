def mayusculas(lista):
  listt = []
  for n in lista:
    txt = n.title()
    listt.append(txt)
  return listt


list = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

print(mayusculas(list))