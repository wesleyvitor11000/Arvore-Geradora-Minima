class Aresta:
    def __init__(self, X : int, Y : int, peso : int):
        self.X = X
        self.Y = Y
        self.peso = peso
    
    def _repr_(self):
        return repr(self.peso, self.X, self.Y)