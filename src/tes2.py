from queue import PriorityQueue


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
    file = open(filename, "r")
    file = file.readlines()

    matrix = []
    coordinates = {}
    for i in range(len(file)):
        file[i] = file[i].split(" " or ",")
        if(len(file[i])==3):
            coordinates[i-len(file[0])+1] = np.array([int(file[i][1]), int(file[i][2])])
        else:
            temp = []
            for j in range(len(file[i])):
                file[i][j] = int(file[i][j])
                temp.append(file[i][j])
            matrix.append(temp)
    return matrix, coordinates
    
def convertMatrixToDict(matrix):
    ## baru buat semalem tapi sekarang udah lupa cara bikinnya wkwkwk
    temp = []
    for i in range(len(matrix)):
        tempDict = {}
        for j in range(len(matrix[i])):
            if matrix[i][j] >= 1:
                ## ini buat apaa? wkwkwk
                tempDict[j+1] = matrix[i][j]
        temp.append(tempDict)
    return temp

def UCS(start, end, dict):
    visited = []
    hasil = []
    avail = PriorityQueue()
    # cost, path
    avail.put((0, str(start)))
    target = end

    while not avail.empty():
        cost, path = avail.get()
        curr = int(path[-1])
        visited.append(path)
        for i in dict[curr-1]:
            if str(i) not in path:
                if(curr != target):
                    avail.put((cost + dict[curr-1][i], path + str(i)))
                    hasil.append((cost + dict[curr-1][i], (path + str(i))))
    
    #cari nilai minimum
    min = 9999999
    path = str
    for i in range(len(hasil)):
        if hasil[i][1][0] == str(start) and hasil[i][1][-1] == str(end):
            if(hasil[i][0] < min):
                min = hasil[i][0]         
                path = hasil[i][1]     
    
    return hasil, visited, min, path
    
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
        
def printPath(path):
    for i in range(len(path)):
        if(i == len(path)-1):
            print(path[i], end="")
        else:
            print(path[i],"-> ", end="")
    print()
    
# a = mintaInputInt("Masukkan Node Awal: ")
# b = mintaInputInt("Masukkan Node Tujuan: ")



# mat = bacaFile("mat3.txt")
# printMatrix(mat)

# print(a,b)



        