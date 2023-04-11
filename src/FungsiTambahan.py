import numpy as np

def mintaInputInt(string, max=10):
    try:
        x = int(input(string))
        if(x > max):
            print("Input harus kurang dari", max)
            return mintaInputInt(string, max)
        return x
    except:
        print("Input harus berupa angka")
        return mintaInputInt(string)
    
def bacaFile(filename):
    try:
        file = open(filename, "r")
        file = file.readlines()
        matrix = []
        for i in range(len(file)):
            temp = []
            file[i] = file[i].split(" " or ",")
            for j in range(len(file[i])):
                file[i][j] = int(file[i][j])
                temp.append(file[i][j])
            matrix.append(temp)
                
            # Validasi jumlah node perbaris
            if(i>0 and len(file[i]) != len(file[i-1])):
                print("Jumlah node perbaris tidak sama")
                filename = input("Masukkan nama file lain: ")
                return bacaFile(filename)
            
        # Validasi apakah jumlah node kurang dari 8
        if(len(matrix[0])<8):
            print("Jumlah node kurang dari 8")
            filename = input("Masukkan nama file lain: ")
            return bacaFile(filename)
                
        print("File berhasil dibaca")
        return matrix
    except:
        print("File tidak ditemukan atau tidak dapat dibuka")
        filename = input("Masukkan nama file: ")
        return bacaFile(filename)
def bacaFile2(filename):
    try:
        file = open(filename, "r")
        file = file.readlines()

        matrix = []
        namaTempat = []
        coordinates = {}
        for i in range(len(file)):
            if(i==0):
                file[i] = file[i].split(",")
            else:
                file[i] = file[i].split(" ")
            if(i==0):
                for j in range(len(file[0])):
                    namaTempat.append(file[i][j])
            elif(len(file[i])==3):
                coordinates[i-len(file[1])] = np.array([float(file[i][1]), float(file[i][2])])
            else:
                temp = []
                for j in range(len(file[i])):
                    file[i][j] = int(file[i][j])
                    temp.append(file[i][j])
                matrix.append(temp)
                # Validasi jumlah node perbaris
                if(i>0 and len(file[i]) != len(file[i-1])):
                    print("Jumlah node perbaris tidak sama")
                    filename = input("Masukkan nama file lain: ")
                    return bacaFile2(filename)
        
        # Validasi apakah jumlah node kurang dari 8
        if(len(matrix[0])<8):
            print("Jumlah node kurang dari 8")
            filename = input("Masukkan nama file lain: ")
            return bacaFile2(filename)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #validasi apakah matrix simetris
                if(matrix[i][j] != matrix[j][i]):
                    print("Matrix tidak simetris")
                    filename = input("Masukkan nama file lain: ")
                    return bacaFile2(filename)
                #validasi apakah matrix diagonal nol
                if(matrix[i][i]!=0):
                    print("Diagonal matrix tidak nol")
                    filename = input("Masukkan nama file lain: ")
                    return bacaFile2(filename)
                
        print("File berhasil dibaca")        
        return matrix, coordinates, namaTempat
    except:
        print("File tidak ditemukan atau tidak dapat dibuka")
        filename = input("Masukkan nama file: ")
        return bacaFile2(filename)

def getHeuristic(start, end, coordinate):
    x = coordinate[start][0] - coordinate[end][0]
    y = coordinate[start][1] - coordinate[end][1]
    return np.linalg.norm(np.array([x,y]))
 
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
        
def printPath(path, nama):
    for i in range(len(path)):
        if(i == len(path)-1):
            print(nama[path[i]-1], end="")
        else:
            print(nama[path[i]-1],"-> ", end="")
    print()
    
def convertMatrixToDict(matrix):
    temp = []
    for i in range(len(matrix)):
        tempDict = {}
        for j in range(len(matrix[i])):
            if matrix[i][j] >= 1:
                tempDict[j+1] = matrix[i][j]
        temp.append(tempDict)
    return temp




        