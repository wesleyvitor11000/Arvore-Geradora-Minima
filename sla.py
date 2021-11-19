
class Aresta:
    def __init__(self, X : int, Y : int, peso : int):
        self.X = X
        self.Y = Y
        self.peso = peso
        
lista = []
with open('sla.txt') as arquivo:
        while True:
            line = arquivo.readline()
            if line == '':
                break
            else:
                x, y, peso = line.split(' ')
                x = int(x)
                y = int(y)
                peso = peso.replace('\n', '')
                lista.append(Aresta(x, y, peso))

print('\n'.join(str(aresta.__dict__) for aresta in lista))