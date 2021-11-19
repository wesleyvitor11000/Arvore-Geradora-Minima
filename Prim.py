from random import randint

class Aresta:
    def __init__(self, X : int, Y : int, peso : int):
        self.X = X
        self.Y = Y
        self.peso = peso
vertices_grafo = [1, 2, 3, 4, 5, 6]
arestas_grafo = [Aresta(1,2,1), Aresta(1,3,2), Aresta(2,3,3), Aresta(3,4,4),Aresta(3,6,6), Aresta(3,5,5), Aresta(4,5,7), Aresta(6,5,8)]
arvore_minima = list()
vertices_arvore_minima = list()

def getMin():
    min = 1000
    menor_aresta : Aresta
    novo_vertice = int()
    for vertice in vertices_arvore_minima:
        for aresta in arestas_grafo:
            if vertice == aresta.X:
                if not haveCycle(aresta):
                    if aresta.peso < min:
                        min = aresta.peso
                        menor_aresta = aresta
                        novo_vertice = aresta.Y
            elif vertice == aresta.Y:
                if not haveCycle(aresta):
                    if aresta.peso < min:
                        min = aresta.peso
                        menor_aresta = aresta
                        novo_vertice = aresta.X

    return menor_aresta, novo_vertice


def haveCycle(aresta : Aresta):
    if aresta.X in vertices_arvore_minima and aresta.Y in vertices_arvore_minima:
        return True
    else:
        return False

def Prim():
    vertice = randint(1, 3)
    vertices_arvore_minima.append(vertice)
    vertices_grafo.remove(vertice)

    while vertices_grafo.__len__() > 0:

        aresta, vertice = getMin()
        vertices_arvore_minima.append(vertice)
        vertices_grafo.remove(vertice)
        arvore_minima.append(aresta)
        arestas_grafo.remove(aresta)

Prim()
for x in arvore_minima:
    print(x.__dict__)