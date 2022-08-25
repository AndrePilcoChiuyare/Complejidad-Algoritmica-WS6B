def Matriz():
    matriz = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],]
    return matriz
#O(1)

def Llenar(matrix):
    for i in range(9): #O(1)
        for j in range(9): #O(1)
           resp = -1
           while resp < 0 or resp > 9: #O(1)
               resp = int(input('Ingrese un numero del 1 al 9:')) #O(1)
               if(resp < 0 or resp > 9): print('NO VALIDO') #O(1)
               matrix[i][j] = resp #O(1)
               
    return matrix
#O(1)

def Mostrar(matrix):
    for i in range(9): #O(1)
        print(matrix[i])
#O(1)

def Validar(matrix):
    suma = 0 
    CindexI = 0 
    CindexJ = 0 
    check = None 
    counter = 0
    cont = False
    rang = 0

    while 1: #O(1)
        for i in range(3): #O(1)
            for j in range(3): #O(1)
                suma += int(matrix[i + CindexI][j + CindexJ]) #O(1)
        if suma == 45:  #O(1)
            if CindexJ != 6:  #O(1)
                CindexJ += 3
            elif CindexI !=6: #O(1)
                CindexJ = 0
                CindexI += 3
            if CindexI and CindexJ == 6: #O(1)
                cont = True
                break
            suma = 0 #O(1)
        else:
            print("Matriz incorrecta") #O(1)
            break #O(1)

    if cont == True: #O(1)
        while 1: #O(1)
            for i in range(9): #O(1)
                check = int(matrix[i][rang])
                counter = matrix[i].count(check)
                if counter != 1: #O(1)
                    print("Matriz incorrecta")
                    break
                   
            if counter != 1: #O(1)
                break     
            
            if rang < 8: #O(1)
                rang += 1
            else: #O(1)
                print("matriz correcta")
                break
#O(1)


            
sudoku = Matriz()
sudoku = Llenar(sudoku)
print('')
Mostrar(sudoku)
Validar(sudoku)


    
