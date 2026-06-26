from estruturas.Array import Array

class ListaArray:

    def __init__(self):
        self.items = Array()

    def inserir(self, item):
        # Insere no final da lista
        self.items.insertAt(item, self.items.logicalSize)

    def remover(self, indice):

        if indice < 0 or indice >= self.items.logicalSize:
            return None

        elemento = self.items[indice]
        self.items.removeAt(indice)

        return elemento

    def buscar(self, item):

        for i in range(self.items.logicalSize):

            if self.items[i] == item:
                return i

        return -1

    def obter(self, indice):

        if indice < 0 or indice >= self.items.logicalSize:
            return None

        return self.items[indice]

    def size(self):
        return self.items.logicalSize

    def isEmpty(self):
        return self.items.logicalSize == 0
    
def playlist(n):

    playlist = ListaArray()

    # Cria a playlist inicial
    for i in range(n):
        playlist.inserir(f"Musica {i}")

    # Adiciona novas músicas (25% da quantidade inicial)
    novasMusicas = max(1, n // 4)

    for i in range(novasMusicas):
        playlist.inserir(f"Nova Musica {i}")

    # Remove todas as músicas
    while not playlist.isEmpty():
        playlist.remover(0)