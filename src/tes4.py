import networkx as nx
import matplotlib.pyplot as plt
from tes2 import *


#minta nama file
filename = input("Masukkan nama file: ")

#baca file
matrix = bacaFile(filename)

#convert ke dictionary
dictMat = convertMatrixToDict(matrix)

#minta input node awal dan tujuan
a = mintaInputInt("Masukkan Node Awal: ")
b = mintaInputInt("Masukkan Node Tujuan: ")

hasil, visited, cost, path = UCS(a, b, dictMat)
# print("visited", visited)
# print("hasil", hasil)
print("cost", cost)
printPath(path)


# Membuat objek graf kosong
G = nx.Graph()

# Menambahkan simpul ke dalam graf
for i in range(len(matrix)):
    G.add_node(i+1)

# Menambahkan sambungan antar simpul beserta bobotnya ke dalam graf
for i in range(1,len(dictMat)+1):
    for j in dictMat[i-1]:
        if(str(i) in path and str(j) in path):
            # warnain edge yang dikunjungin jadi merah
            G.add_edge(i, j, weight=dictMat[i-1][j], color='r')
        else:
            # warnain edge yang ga dikunjungin jadi hitam
            G.add_edge(i, j, weight=dictMat[i-1][j], color='black')

# warnain semua jadi biru
node_colors = []
for i in range(len(dictMat)):
    node_colors.append('b')
    
# warnain yang dikunjungi jadi merah 
for i in str(path):
    node_colors[int(i)-1] = 'r'
    
# setting buat warnain edge
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]

# Menggambar graf menggunakan matplotlib
pos = nx.spring_layout(G)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos,edge_color=colors, width=1.0, alpha=0.5)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
