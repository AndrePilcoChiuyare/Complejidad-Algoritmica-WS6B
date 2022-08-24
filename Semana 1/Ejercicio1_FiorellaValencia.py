import numpy as np


def generar(n):
    return np.random.randint(1,100,n)
 # O(n)
def mostrar(t):
    for i in range (0,5):
        print(t[i])
 # O(n)
def reversa(original):
    return [original[len(original)-i] for i in range(1,len(original)+1)]
 # O(n)
def minval(t):
  min_val=t[0]
  for i in range (0,len(t)):
    if t[i] < min_val:
      min_val=t[i]

  return min_val
 # O(n) 
def media(t):
  suma=0
  for i in range(0, len(t)):    
   suma = suma + t[i];

  return (suma/len(t))
# O(n)
def ocurencia(t):
  s=[]
  i=0
  index=len(t)
  while(index>0):
      s.append(t.count(i))
      index=index-1

  return s 
# O(n^2)