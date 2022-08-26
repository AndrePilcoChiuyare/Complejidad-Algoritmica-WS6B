def findstring(str, tri):
    found = str.find(tri)
    for i in range(len(str)):
        found = str.find(tri,found)
        count = str.count(tri)
        if found != -1:
            found+=1
            print('Esta en la posicion : ', found)
    
    print ("Numero de ocurrencias", count)   
        
findstring("reyreyrey reyes","rey")