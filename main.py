from Aresta import Aresta;
from Prim import Prim;
from kruskalAlgorithm import kruskalAlgorithm;
from matrizAdjacencia import mostrarMatriz;

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
                peso = int(peso)
                arestas.append(Aresta(x, y, peso))
                if x not in vertices:
                    vertices.append(x)
                if y not in vertices:
                    vertices.append(y)

    #print('\n'.join(str(aresta._dict_) for aresta in lista))  
    return arestas, vertices         



nome = input('Digite o nome do arquivo: ')

arestas, vertices = importarArestas(nome)

kruskalAGM = kruskalAlgorithm(arestas)
primAGM = Prim(arestas, vertices)


print('Kruskal:\n')
#print('\n'.join(str(aresta.__dict__) for aresta in kruskalAGM))
mostrarMatriz(kruskalAGM, vertices)

print('\nPrim:\n')
#print('\n'.join(str(aresta.__dict__) for aresta in primAGM))
mostrarMatriz(primAGM, vertices)