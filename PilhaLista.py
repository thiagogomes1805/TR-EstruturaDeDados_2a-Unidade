from estruturas.LinkedList import LinkedList

# Histórico de navegação
def historico(n):
    historico_web = LinkedList()
    for i in range(n):
        historico_web.insertAtFirst(i)
