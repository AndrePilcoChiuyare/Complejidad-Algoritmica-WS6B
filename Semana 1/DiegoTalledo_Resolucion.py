# -*- coding: utf-8 -*-
"""Hoja de Ejercicios 1 Complejidad Algorítmica

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Pk7Uheou2ZUxuKIV0l_PXaNUOq8Fslr
"""

# Escriba un método generar(n) que genere un arreglo de tamaño n con todos sus elementos 
# aleatorios entre 1 y 100
import random as rdm
def generar(n):
  array=[]
  for i in range(n):
   array.insert(i,rdm.randint(0,100))
  return array
prueba=generar(10)
print(prueba)

#Escriba un método mostrar(int[] t) que muestra todos los elementos de un arreglo t.

def mostrar(n):
  for i in range(len(n)):
    print(f"Elemento {i}: {n[i]}")

t=[1,4,5,6,9,8,2,3,5]
mostrar(t)

# Escriba un método reversa(int[] t) que invierte el orden de todos los elementos de un arreglo t (sin crear arreglos auxiliares)
def reversa(t):
  t.reverse()
  return t

array=[1,2,3,4,5,6,7,8,9]
reversa(array)
print(array)

# Escriba un método int minArreglo(int[] t) que devuelve el elemento más pequeño de un arreglo.
def minArreglo(t):
  min=999
  for i in t:
    if i<min:
      min=i
  return min

array=[4,2,8,9,1,10]
minArreglo(array)

# Escriba un método int mediaArreglo(int[] t) que devuelve la media aritmética de los elementos de un arreglo.
def mediaArreglo(t):
  ma=0
  for i in t:
    ma+=i 
  ma/=len(t)
  return ma

array=[5,7,6,2]
mediaArreglo(array)

# Escriba un método int[] ocurrencias(int[] t) que devuelve un nuevo arreglo s tal que s[i] es el número de veces que el entero i aparece en t.
def ocurrencias(a,t):
  return t.count(a)

array=[1,2,1,3,1]
ocurrencias(1,array)

#Cree un arreglo de 100 enteros. Inicialice el arreglo de forma que la casilla i contenga el entero i. Muestre el arreglo.
def generar(n):
  array=[]
  for i in range(n):
   array.append(i)
  return array

array=generar(100)
print(array)

#Escriba u n programa que pide al usuario d e entrar una grilla de sudoku1 completamente llena y verifique que esta grilla es correcta.


def grillaG():
  grilla=set()
  for i in range(9):
    num=int(input(f"Eliga un numero {i+1} de la grilla: "))
    grilla.add(num)
  if len(grilla)<=8:
      print("Grilla no valida")
  else: 
      print("Grilla  valida")

grillaG()

def criba(n):
  t=[]
  for i in range(n):
   t.append(i)
  for i in range(int(n/2)):
    eliminador=2*(i+2)
    if t.count(eliminador)>=1:
        t.remove(eliminador)
    eliminador=3*(i+2)
    if t.count(eliminador)>=1:
        t.remove(eliminador)
    eliminador=5*(i+2)
    if t.count(eliminador)>=1:
        t.remove(eliminador)
    eliminador=7*(i+2)
    if t.count(eliminador)>=1:
        t.remove(eliminador)
    eliminador=11*(i+2)
    if t.count(eliminador)>=1:
        t.remove(eliminador)
  return t


array=criba(100)
print(array)