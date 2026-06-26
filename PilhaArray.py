from estruturas.Array import Array

class PilhaArray:

    def __init__(self):
        self.items = Array()

    def push(self, item):
        # Insere sempre no final da estrutura
        self.items.insertAt(item, self.items.logicalSize)

    def pop(self):
        if self.items.logicalSize == 0:
            return None

        elemento = self.items[self.items.logicalSize - 1]
        self.items.removeAt(self.items.logicalSize - 1)

        return elemento

    def peek(self):
        if self.items.logicalSize == 0:
            return None

        return self.items[self.items.logicalSize - 1]

    def isEmpty(self):
        return self.items.logicalSize == 0


def historico(n):

    historico = PilhaArray()

    # O usuário acessa n páginas
    for i in range(n):
        historico.push(f"Pagina {i}")

    # O usuário volta algumas páginas e acessa outras novas
    novasPaginas = max(1, n // 4)

    for i in range(novasPaginas):

        # Volta uma página
        historico.pop()

        # Acessa uma nova página
        historico.push(f"Nova Pagina {i}")

    # Fecha todas as páginas restantes
    while not historico.isEmpty():
        historico.pop()