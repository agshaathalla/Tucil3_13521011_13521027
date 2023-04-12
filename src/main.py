# from tes2 import *
import networkx as nx
import matplotlib.pyplot as plt
import webbrowser
from SplashScreen import *
from FungsiUtama import *
from FungsiTambahan import *
from maps import *

def main():
    splashScreen()
    print("===========================================")

    filename = input("Masukkan nama file: ")

    #baca file
    matrix, koordinat, nama = bacaFile2(filename)

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

    print("DAFTAR NODE:")
    for i,j in enumerate(nama):
        print(i+1, j)
    a = mintaInputInt("Masukkan Node Awal: ", len(matrix))
    b = mintaInputInt("Masukkan Node Tujuan: ", len(matrix))

    #convert ke dictionary
    dictMat = convertMatrixToDict(matrix)


    if(algo==1):
        hasil, visited, cost, path = UCS(a, b, dictMat)
        print("Hasil UCS: ")
        print("Jarak:", cost,"Meter")
        printPath(path, nama)
    elif(algo==2):
        hasil, visited, cost, path = AStar(a, b, dictMat, koordinat)
        print("Hasil A*: ")
        print("Jarak:", cost,"Meter")
        printPath(path, nama)

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
    
    showMap(koordinat, path)
    tanyaMaps = input("Apakah ingin menampilkan maps? (Y/N): ")
    if(tanyaMaps=="Y" or tanyaMaps=="y"):
        webbrowser.open_new_tab('file://'+os.getcwd()+'bin/maps.html')
    

    # Menggambar graf menggunakan matplotlib
    nx.draw_networkx_labels(G, koordinat)
    nx.draw_networkx_edges(G, koordinat,edge_color=colors, width=1.0)
    nx.draw_networkx_nodes(G, koordinat, node_color=node_colors, node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, koordinat, edge_labels=labels)
    plt.show()
    
    

    pilihan = input("Apakah ingin mengulang pencarian? (Y/N): ")
    if(pilihan=="Y" or pilihan=="y"):
        main()
    else:
        print("Terima kasih telah menggunakan program ini")

if __name__ == "__main__":
    main()