from Aresta import Aresta;
from kruskalAlgorithm import kruskalAlgorithm;

def importarArestas(nome):
    lista = []
    with open(nome) as arquivo:
        while True:
            line = arquivo.readline()
            #print(line)
            if line == '':
                break
            else:
                x, y, peso = line.split(' ')
                x = int(x)
                y = int(y)
                peso = peso.replace('\n', '')
                lista.append(Aresta(x, y, peso))

    #print('\n'.join(str(aresta._dict_) for aresta in lista))  
    return lista          



nome = input()
grafo = importarArestas(nome)

agm = kruskalAlgorithm(grafo)

for i in agm:
    print(i.__dict__)