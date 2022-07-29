def fibo(num):
  list = []
  for i in range(0, num):
    if i == 0:
      list.append(0)
    elif i == 1:
      list.append(1)
    else:
      list.append(list[-2]+list[-1])
  return list

print(fibo(15))