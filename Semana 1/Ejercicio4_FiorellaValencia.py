#Criba de eratostenes
n = int(input("Ingrese un numero: "))
lista = list(range(2, n+1))

i = 0
while(lista[i]*lista[i] <= n):
    for num in lista:
        if num <= lista[i]:
            continue
        elif num % lista[i] == 0:
            lista.remove(num)
        else:
            pass
    i += 1 
print (lista)

# O(n^2)