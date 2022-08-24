import random as rm

# 1
def generar(numeros):
  arreglo = []
  for num in range(numeros):
    arreglo.append(rm.randrange(1,100))
  return arreglo

# 2
def mostrar(t):
  for i in range(len(t)):
    print(t[i])

# 3
def reverse(list):
  list.reverse()
  return list

# 4
def minArreglo(list):
  numero=None
  for i in list:
    if numero is None:
      numero=i
      continue
    if i < numero:
      numero=i 
  return(numero)

# 5
def mediaArreglo(list):
  media = len(list)
  suma = None
  for i in list:
    if suma is None:
      suma = i
      continue
    suma = suma + i
  return (suma/media)

# 6
def ocurrencias(t):
  s=[]
  index=0
  num=len(t)
  while num != 0:
    count=t.count(index)
    s.append(count)
    index=index+1
    num=num-1
  return s