from random import randint

lenGrafp = int(input('Digite o número de vertices do grafo:\n'))
vertices = [x for x in range(1,lenGrafp+1)]
arquivo = f"grafos/grafo-completo-{lenGrafp}.txt"

with open(arquivo, 'w') as grafo:
    for i in vertices:
        for j in range(i+1, lenGrafp + 1):
            grafo.write(f"{i} {j} {randint(1,10)}\n")
            