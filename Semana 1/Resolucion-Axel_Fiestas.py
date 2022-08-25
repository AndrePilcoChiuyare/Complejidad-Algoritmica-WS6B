import random
#Escriba un método generar(n) que genere un arreglo de tamaño n con todos sus elementos
#aleatorios entre 1 y 100.


def generar(n):
    lista=[]
    for elemento in range(0,n):
        elemento=random.randint(1, 101)
        lista.append(elemento)

    return lista


print(generar(5))

#1 Ciclo For involucrado por tanto: Complejidad O(n)


#------------------------------------------------------------------------------------------------------------

#Escriba un método mostrar(int[] t) que muestra todos los elementos de un arreglo t.

def mostrar(t):
    for elemento in t:
        print(elemento)

lista=[4,6,1,2]

mostrar(lista)

#1 Ciclo For involucrado por tanto: Complejidad O(n)

#------------------------------------------------------------------------------------------------------------

#Escriba un método reversa(int[] t) que invierte el orden de todos los elementos de un arreglo t
#(sin crear arreglos auxiliares)

frutas=["pera","manzana","platano","fresa","mango"]
numeros=[1,2,3]

def invetir(lista):

    tamanioLista=len(lista)

    for i in range(tamanioLista):

        if(i>=tamanioLista/2):
            break
        else:
            primerElemento=lista[i]
            ultimoElemento=lista[tamanioLista-1-i]

            lista[i]=ultimoElemento
            lista[tamanioLista-i-1]=primerElemento

    return lista

print(invetir(frutas))

#1 Ciclo For involucrado por tanto: Complejidad O(n)

#------------------------------------------------------------------------------------------------------------

#Escriba un método int minArreglo(int[] t) que devuelve el elemento más pequeño de un arreglo.

numeros=[6,10,3,8,10,8,2]

def minArreglo(lista):

    numeroMenor=lista[0]

    for numero in lista:

        if(numeroMenor>=numero):
            numeroMenor=numero

    return numeroMenor


print(minArreglo(numeros))

#1 Ciclo For involucrado por tanto: Complejidad O(n)


#------------------------------------------------------------------------------------------------------------

#Escriba un método int mediaArreglo(int[] t) que devuelve la media aritmética de los elementos de un arreglo


numeros=[14,16,12,12,10,18,20,14]

def mediaArreglo(lista):

    tamanioLista=len(lista)
    suma=0

    for elemento in lista:
        suma+=elemento

    media=suma/tamanioLista

    return media

print(mediaArreglo(numeros))

#1 Ciclo For involucrado por tanto: Complejidad O(n)

#------------------------------------------------------------------------------------------------------------

#Escriba un método int[] ocurrencias(int[] t) que devuelve un nuevo arreglo s tal que s[i] es el
#número de veces que el entero i aparece en t.
import random

numeros=[0,7,7,1,2,3,1,1,1,1,1,1,10,10,10,10]

def apareceNumero(lista,numeroDado):
    contador=0
    for numero in lista:
        if(numeroDado==numero):
            contador+=1


    return contador


def ocurrencias(lista,numeroDado):

    i=apareceNumero(lista,numeroDado)
    listaNueva=[]

    for elemento in range(i):
        listaNueva.append(numeroDado)


    return listaNueva


print(ocurrencias(numeros,10))

#1 Ciclo For involucrado por tanto: Complejidad O(n)


#------------------------------------------------------------------------------------------------------------

#Cree un arreglo de 100 enteros.
#Inicialice el arreglo de forma que la casilla i contenga el entero i.
#Muestre el arreglo.
#Analice la complejidad de este algoritmo.

def crearLista():
    lista=[]
    for i in range(101):
        lista.append(i)

    return lista

def mostrarLista(lista):
    print(lista)


listaNumeros=crearLista()
mostrarLista(listaNumeros)

#1 Ciclo For involucrado por tanto: Complejidad O(n)


#------------------------------------------------------------------------------------------------------------
#REALIZAR UN SUDOKU

filas=9
columnas=9

def dibujarTablero(matriz):

    print("\tSUDOKU\t")

    for i in range(filas):

        if(i%3==0):print("------------------")

        for j in range(columnas):

            if(j==2 or j==5 or j==8):print(matriz[i][j], end='|')
            else:print(matriz[i][j],end=" ")
        print(" ")

def devolverTableroRellenado():
    matrizNueva=[]
    for i in range(filas):
        matrizNueva.append([])
        for j in range(columnas):
            valor=input("Fila {}, Columna {}: ".format(i+1,j+1))
            matrizNueva[i].append(valor)

    return matrizNueva

def revisarNumeroExistenteEnFila(matriz,numero,fila):

    contador=0
    for j in range(columnas):
        if(matriz[fila][j]==numero):
            contador+=1

    if(contador>1):
        return True
    else:
        return False

def revisarNumeroExistenteEnColumna(matriz,numero,columna):
    contador=0
    for i in range(filas):
        if(matriz[i][columna]==numero):
            contador+=1

    if(contador>1):
        return True
    else:
        return False


def revisarSudoku(matriz):

    for i in range(filas):
        for j in range(columnas):

            apareceEnFila=revisarNumeroExistenteEnFila(matriz,matriz[i][j],i)
            apareceEnColummna=revisarNumeroExistenteEnColumna(matriz,matriz[i][j],j)

            if(apareceEnFila or apareceEnColummna):
                return "Sudoku Incorrecto"
            else:
                pass

    return "Sudoku Correcto"


matrizEjemplo=devolverTableroRellenado()
dibujarTablero(matrizEjemplo)
print(revisarSudoku(matrizEjemplo))

#2 for anidados manisfetados como funciones dentro de 2 for anidados -> Orden Polinomico O(n^4)


#------------------------------------------------------------------------------------------------------------

#Criba de Eratostenes (Incompleto)


def generarLista(n):
    lista=[]
    for i in range(2,n):
        lista.append(i)

    return lista

def suprimirPares(lista):
    listaAuxiliar = []

    for numero in lista:
        if (numero%2==0 and numero!=2):
            pass
        else:
            listaAuxiliar.append(numero)
    lista = listaAuxiliar
    return lista


def esMultiplo(numeroRecibido,multiplo):

    numeroAuxiliar=multiplo

    for i in range(numeroRecibido):

        if(numeroAuxiliar>numeroRecibido):
            return False
        else:
            pass

        numeroAuxiliar=multiplo*i

        if(numeroRecibido==numeroAuxiliar):
            return True
        else:
            pass


def suprimirMultiplos(lista,multiplo):

    listaAuxiliar=[]

    for numero in lista:
        if(esMultiplo(numero,multiplo) and numero!=multiplo):
            pass
        else:
            listaAuxiliar.append(numero)

    lista=listaAuxiliar

    return lista


def verificar(numeroPequeno,numeroGrande):

    numeroPequenoAlCuadrado=numeroPequeno*numeroPequeno

    if(numeroPequenoAlCuadrado>numeroGrande):
        return True
    else:
        return False


def cribaEratostenes(n):

    listaEratostenes=generarLista(n)
    listaEratostenes=suprimirPares(listaEratostenes)
    tamanioLista=len(listaEratostenes)

    listaAux=[]

    for i in range(tamanioLista):
        if(verificar(listaEratostenes[i+1],listaEratostenes[tamanioLista-1])):
            break
        listaAux=suprimirMultiplos(listaEratostenes,listaEratostenes[i+1])

    return listaAux

#No me salió F :,v

print(cribaEratostenes(30))






