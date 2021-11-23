from Aresta import Aresta;
from Prim import Prim;
from kruskalAlgorithm import kruskalAlgorithm;
from time import perf_counter_ns
from matrizAdjacencia import mostrarMatriz;

#Função que lê um txt e cria um grafo a partir do mesmo
def importarArestas(nome):
    arestas = []
    vertices = []
    with open(nome) as arquivo:
        while True:
            line = arquivo.readline()
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
  
    return arestas, vertices         



nome = input('Digite o nome do arquivo: ')
arestas, vertices = importarArestas(nome)

#medição do algoritmo de Kruskal
inicio_Kruskal = perf_counter_ns()
kruskalAGM = kruskalAlgorithm(arestas)
fim_Kruskal = perf_counter_ns() - inicio_Kruskal

#medição do algoritmo de Prim
inicio_Prim = perf_counter_ns()
primAGM = Prim(arestas, vertices)
fim_Prim = perf_counter_ns() - inicio_Kruskal

#imprime tanto o tempo gasto, como a Arvore geradora minima para cada algoritmo
print(f"Kruskal: demorou {fim_Kruskal} ns \n")
mostrarMatriz(kruskalAGM, vertices)
#print('\n'.join(str(aresta.__dict__) for aresta in kruskalAGM))
print(f"\nPrim: demorou {fim_Prim} ns\n")
mostrarMatriz(primAGM, vertices)
#print('\n'.join(str(aresta.__dict__) for aresta in primAGM))
