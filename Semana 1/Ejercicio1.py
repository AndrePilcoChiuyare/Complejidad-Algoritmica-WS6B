import numpy as np
import array as arr

print(np.random.rand(5))
#1
def generar(n):
    np.random.randint(1,100,n)
#2
a = arr.array('i', [1, 2, 3,6,7,8,9])

def mostrar(t):
    for i in range (0,5):
        print(t[i])
    
mostrar(a)
#3
def reversa(original):
    return [original[len(original)-i] for i in range(1,len(original)+1)]
    
original=[12,20,25,65,78,45,12,56]
print(reversa(original))

#4
lista=[28,91,94,92,91,13,15]
min_val=lista[0]

for i in range(0,len(lista)):
    if lista[i] < min_val:
        min_val=lista[i]

print(min_val)
#5 media aritmetica
arr = [1, 2, 3, 4, 5];     
sum = 0;    
     
#Loop through the array to calculate sum of elements    
for i in range(0, len(arr)):    
   sum = sum + arr[i];    
     
print(sum/len(arr));  





EJERCICIO 4 
n = int(input("Ingrese un numero: "))
lista = list(range(2, n+1))

i = 0
while(lista[i]*lista[i] <= n):
    # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
    for num in lista:
        if num <= lista[i]:
            # Cada iteracion del while hace que el for comience desde el primer elemento. 
            # Esto es para omitir los numeros primos ya encontrados
            continue
        elif num % lista[i] == 0:
            # Si un numero es divisible entre el elemento actual del while
            # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
            lista.remove(num)
        else:
            # Si no es divisible, entonces omitirlo (no hacer nada)
            pass
    i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

print (lista)