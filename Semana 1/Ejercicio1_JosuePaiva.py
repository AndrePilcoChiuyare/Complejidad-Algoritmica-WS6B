import random as r

#Item1
def generar(num):
array = []
for n in range(num): array.append(r.randrange(1,100))
return array

#Item2
def mostrar(array):
	print (array)

#Item3
def reversa(array):
	array.reverse()
	return array

#Item4
def minArreglo(array):
	exp=100
	for array[i] in array:
	if array[i]<exp:
	exp=array[i]
	return exp

#Item5
def mediaArreglo(array):
	sum=0
	for array[i] in array:
		sum=sum+array[i]
e=len(array)
media=(sum/e)
