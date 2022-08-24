import random as rm

def generar():
  arreglo = []
  for num in range(100):
    arreglo.append(rm.randrange(1,100))
  return arreglo
# Big O: O(1)
arr = generar()

def mismoPosicion(list):
  for i in range(len(list)):
    list[i]=i
  return list
# Big O: O(1)

print(arr)