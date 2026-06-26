from estruturas.Array import Array

def historico(n):

    historico = Array(n)
    topo = -1

    # Push
    for i in range(n):
        topo += 1
        historico[topo] = f"pagina{i}"

    # Pop
    while topo > 0:
        historico[topo] = None
        topo -= 1