from estruturas.LinkedList import LinkedList

# Playlist de músicas
def playlist(n):
    lista_musicas = LinkedList()
    for i in range(n):
        lista_musicas.insertAtLast(i)
