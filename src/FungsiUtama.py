from queue import PriorityQueue
from FungsiTambahan import *

def UCS(start, end, dict):
    visited = []
    hasil = []
    avail = PriorityQueue()
    # cost, path
    avail.put((0, [start]))
    target = end
    print(dict)

    while not avail.empty():
        cost, path = avail.get()
        tempPath = path.copy()
        curr = path[len(path)-1]
        visited.append(path)
        for i in dict[curr-1]:
            path = tempPath.copy()
            if i not in path:
                if(curr != target):
                    path.append(i)
                    avail.put((cost + dict[curr-1][i], path))
                    hasil.append((cost + dict[curr-1][i], (path)))
    #cari nilai minimum
    min = 9999999
    path = list
    for i in range(len(hasil)):
        if hasil[i][1][0] == (start) and hasil[i][1][len(hasil[i][1])-1] == (end):
            if(hasil[i][0] < min):
                min = hasil[i][0]         
                path = (hasil[i][1])
    
    return hasil, visited, min, path

def AStar(start, end, dict, coordinate):
    visited = []
    hasil = []
    avail = PriorityQueue()
    
    # cost, path
    avail.put((0, [start]))
    target = end
    count = 0

    if start == end:
        return hasil, visited, 0, [start]

    while not avail.empty():
        cost, path = avail.get(0)
        # print("path saat ini", path)
        tempPath = path.copy()
        print(path)
        print(path[len(path)-1])
        curr = path[len(path)-1]
        if curr == target:
            break
        if cost>0:
            # cost -= heuristic[path[-1]-1]
            cost -= getHeuristic(path[-1], end, coordinate)
        visited.append(path)
        for i in dict[curr-1]:
            path = tempPath.copy()
            if i not in path:
                if(curr != target):
                    path.append(i)
                    # avail.put((cost + dict[curr-1][i] + heuristic[i-1] , path))
                    avail.put((cost + dict[curr-1][i] + getHeuristic(i, end, coordinate) , path))
                    hasil.append((cost + (dict[curr-1][i]) , (path)))
                    print(curr-1," = ", hasil[len(hasil)-1])
                    count += 1
    
    return hasil, visited, cost, path