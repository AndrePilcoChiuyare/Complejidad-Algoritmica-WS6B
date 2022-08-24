import random as rand
import statistics as stats
def generar(n):
    t = []
    for indice in range(n):
        t.append(rand.randrange(1,100))
    return t
    
def mostrar(t):
    print(t)

def reversa(list):
    list.reverse()

def minArreglo(list):
    minimo = 101
    for i in list:
        if(list[i] < minimo): minimo = list[i]
    
    return minimo

def mediaArreglo(list):
    return stats.mean(list)

def ocurrencias(list):
    s = []
    for i in range(len(list)):
        s.append(list.count(i))

    return s



t = generar(100)
print('LISTA NORMAL')
print('')
mostrar(t)
reversa(t)
print('')
print('LISTA REVERSA')
mostrar(t)
print('')
print('ELEMENTO MINIMO')
print('')
print(str(minArreglo(t)))
print('')
print('MEDIA ARITMETICA')
print('')
print(str(mediaArreglo(t)))
print('')
print('OCURRENCIAS')
print('')
print(ocurrencias(t))
print('')
