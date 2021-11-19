from operator import attrgetter


def kruskalAlgorithm (grafo: list()):

    subgrafos = list()
    agm = list()


    for aresta in grafo:

        grafo = sorted(grafo, key=attrgetter('peso'))
        
        if(not subgrafos):
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
    
    return agm
