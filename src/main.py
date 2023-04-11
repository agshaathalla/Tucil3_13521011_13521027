from tes2 import *
import networkx as nx
import matplotlib.pyplot as plt


print("===========================================")



print("===========================================")

filename = input("Masukkan nama file: ")

#baca file
# matrix = bacaFile()
matrix, koordinat = bacaFile2(filename)

print("Pilih Algorithm yang ingin digunakan: ")
print("1. UCS")
print("2. A*")

algo = int
while(algo!=1 and algo!=2):
    algo = mintaInputInt("Masukkan pilihan: ", 2)

if(algo==1):
    print("Kamu memilih UCS")
elif(algo==2):
    print("Kamu memilih A*")


a = mintaInputInt("Masukkan Node Awal: ", len(matrix))
b = mintaInputInt("Masukkan Node Tujuan: ", len(matrix))

#convert ke dictionary
dictMat = convertMatrixToDict(matrix)


if(algo==1):
    hasil, visited, cost, path = UCS(a, b, dictMat)
    print("Hasil UCS: ")
    printPath(path)
    print("Jarak:", cost,"Meter")
    # print("UCS")
elif(algo==2):
    hasil, visited, cost, path = AStar(a, b, dictMat)
    printPath(path)
    print("Jarak:", cost,"Meter")

# Membuat objek graf kosong
G = nx.Graph()

# Menambahkan simpul ke dalam graf
for i in range(len(matrix)):
    G.add_node(i+1)

# Menambahkan sambungan antar simpul beserta bobotnya ke dalam graf
for i in range(1,len(dictMat)+1):
    for j in dictMat[i-1]:
        if(i in path and j in path):
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
for i in (path):
    node_colors[i-1] = 'r'
    
# setting buat warnain edge
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]

# Menggambar graf menggunakan matplotlib
# pos = nx.spring_layout(G)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos,edge_color=colors, width=1.0)
# nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()

nx.draw_networkx_labels(G, koordinat)
nx.draw_networkx_edges(G, koordinat,edge_color=colors, width=1.0)
nx.draw_networkx_nodes(G, koordinat, node_color=node_colors, node_size=500)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, koordinat, edge_labels=labels)
plt.show()