from estruturas.LinkedList import LinkedList

# Fila de senhas
def filaImpressao(n):
    fila = LinkedList()
    for i in range(n):
        fila.insertAtLast(i)