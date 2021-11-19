from Aresta import Aresta;
from kruskalAlgorithm import kruskalAlgorithm;

def importarArestas(nome):
    arestas = []
    vertices = []
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
                arestas.append(Aresta(x, y, peso))
                if x not in vertices:
                    vertices.append(x)
                if y not in vertices:
                    vertices.append(y)

    #print('\n'.join(str(aresta._dict_) for aresta in lista))  
    return arestas, vertices         



nome = input('Digite o nome do arquivo: ')

arestas, vertices = importarArestas(nome)

agm = kruskalAlgorithm(arestas)

for i in agm:
    print(i.__dict__)