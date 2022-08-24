import random as rand
import statistics as stats
def generar(n):
    t = [] #O(1)
    for indice in range(n): #O(n)
        t.append(rand.randrange(1,100))#O(1)
    return t #O(1)
#0(n)

def mostrar(t):
    print(t)
    #O(1)

def reversa(list):
    list.reverse()
    #O(n)

def minArreglo(list):
    minimo = 101 #O(1)
    for i in list: #O(n)
        if(list[i] < minimo): minimo = list[i] #O(1)

    return minimo #O(1)
#O(n)

def mediaArreglo(list):
    return stats.mean(list)
#O(n)

def ocurrencias(list):
    s = [] #O(1)
    for i in range(len(list)): #O(n)
        s.append(list.count(i)) #O(n)

    return s #O(1)
#O(n^2)


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
