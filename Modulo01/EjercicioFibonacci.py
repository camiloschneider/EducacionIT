def fibo(num):
  list = []
  if num >=2:
    for i in range(0, num):
      if i == 0:
        list.append(0)
      elif i == 1:
        list.append(1)
      else:
        list.append(list[-2]+list[-1])
    return list
  return print('Debe ingresar un argumento mayor a 2')
 
print(fibo(4))