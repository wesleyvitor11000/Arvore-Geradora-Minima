from random import randint
from Aresta import Aresta

vertices_grafo = []
arestas_grafo = []
arvore_minima = []
vertices_arvore_minima = []

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

def Prim(arestas, vertices):
    arestas_grafo = arestas
    vertices_grafo = vertices
    
    vertice = randint(1, 3)
    vertices_arvore_minima.append(vertice)
    vertices_grafo.remove(vertice)

    while vertices_grafo.__len__() > 0:

        aresta, vertice = getMin()
        vertices_arvore_minima.append(vertice)
        vertices_grafo.remove(vertice)
        arvore_minima.append(aresta)
        arestas_grafo.remove(aresta)

