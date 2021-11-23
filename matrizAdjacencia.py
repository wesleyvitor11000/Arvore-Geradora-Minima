from Aresta import Aresta

def mostrarMatriz(grafo : list(), vertices:list()):
    matriz = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

    for aresta in grafo:
        matriz[aresta.X-1][aresta.Y-1] = aresta.peso
    
    for i in matriz:
        for j in i:
            print(j, '   ' , end='')
        print()
