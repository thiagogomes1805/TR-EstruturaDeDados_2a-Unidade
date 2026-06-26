from estruturas.Array import Array

class FilaArray:

    def __init__(self):
        self.items = Array()

    def enqueue(self, item):
        # Insere no final da fila
        self.items.insertAt(item, self.items.logicalSize)

    def dequeue(self):
        if self.isEmpty():
            return None

        primeiro = self.items[0]
        self.items.removeAt(0)

        return primeiro

    def front(self):
        if self.isEmpty():
            return None

        return self.items[0]

    def isEmpty(self):
        return self.items.logicalSize == 0

    def size(self):
        return self.items.logicalSize

def filaImpressao(n):

    fila = FilaArray()

    # Documentos enviados inicialmente
    for i in range(n):
        fila.enqueue(f"Documento {i}")

    # Enquanto alguns documentos são impressos,
    # novos documentos chegam à fila
    novosDocumentos = max(1, n // 4)

    for i in range(novosDocumentos):

        fila.dequeue()

        fila.enqueue(f"Novo Documento {i}")

    # Impressão dos documentos restantes
    while not fila.isEmpty():
        fila.dequeue()