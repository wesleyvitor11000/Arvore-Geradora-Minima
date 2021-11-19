from operator import itemgetter, attrgetter

class Aresta:
    def __init__(self, X : int, Y : int, peso : int):
        self.X = X
        self.Y = Y
        self.peso = peso
    
    def _repr_(self):
        return repr(self.peso, self.X, self.Y)

def kruskalAlgo (grafo: list()):

    subgrafos = list()
    agm = list()


    for aresta in grafo:

        grafo = sorted(grafo, key=attrgetter('peso'))
        
        if(not subgrafos):
            print('Adcionado por null: ', aresta.X, ' , ', aresta.Y)
            subgrafos.append([aresta.X, aresta.Y])
            agm.append(aresta)
            continue

        for subgrafo in subgrafos:
            
            encontrou = False

            if(aresta.X in subgrafo):

                if(aresta.Y in subgrafo):
                    encontrou = True
                    break
                else:
                    for subgrafo2 in subgrafos:
                        if(subgrafo == subgrafo2):
                            continue

                        if(aresta.Y in subgrafo2):
                            subgrafo += subgrafo2
                            subgrafos.remove(subgrafo2)
                            agm.append(aresta)
                            encontrou = True
                            break
                
                    if(not encontrou):
                        subgrafo += [aresta.Y]
                        agm.append(aresta)
                        encontrou = True

            elif(aresta.Y in subgrafo):
                
                for subgrafo2 in subgrafos:
                    if(subgrafo == subgrafo2):
                        continue

                    if(aresta.X in subgrafo2):
                        subgrafo += subgrafo2
                        subgrafos.remove(subgrafo2)
                        agm.append(aresta)
                        encontrou = True
                        break

                if(not encontrou):
                    subgrafo += [aresta.X]
                    agm.append(aresta)
                    encontrou = True
            
        if(not encontrou):
            subgrafos.append([aresta.X, aresta.Y])
            agm.append(aresta)
    
    print('Arvore geradora mínima do grafo:')
    for i in agm:
        print(i.__dict__)


            



#grafo = [ Aresta(3,6, 2), Aresta(1,2,1), Aresta(5,6,4), Aresta(4,3,5), Aresta(4,5,3), Aresta(1,4,7),Aresta(2,3,6)]
grafo = [Aresta(1,2,1), Aresta(1,3,2), Aresta(2,3,3), Aresta(3,4,4), Aresta(3,6,6), Aresta(3,5,5), Aresta(4,5,7), Aresta(6,5,8)]



kruskalAlgo(grafo)