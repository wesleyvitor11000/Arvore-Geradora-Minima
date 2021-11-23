from random import randint


from random import randint

escolhas = [True, False]

lenGrafp = int(input('Digite o número de vertices do grafo:\n'))
vertices = [x for x in range(1,lenGrafp+1)]
arquivo = f"grafos/grafo-incompleto-{lenGrafp}.txt"

with open(arquivo, 'w') as grafo:
    for i in vertices:
        for j in range(i+1, lenGrafp + 1):
            if escolhas[randint(0,1)]:
                grafo.write(f"{i} {j} {randint(1,10)}\n")
            