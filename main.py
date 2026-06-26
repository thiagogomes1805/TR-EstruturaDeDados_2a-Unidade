
import time
import os

import PilhaArray as pa
import PilhaLista as pl

import FilaArray as fa
import FilaLista as fl

import ListaArray as la
import ListaLigada as ll

def medirTempo(funcao, entrada):

    inicio = time.perf_counter()

    funcao(entrada)

    fim = time.perf_counter()

    return (fim - inicio)*1000

def salvaResultado(algoritmo,n, resultado, ordem = None):

    os.makedirs('resultados',exist_ok=True)

    if ordem != None:

        caminhoArquivo = os.path.join('resultados',f'{algoritmo}-{ordem}.res')

    else:
        caminhoArquivo = os.path.join('resultados',f'{algoritmo}.res')

    with open(caminhoArquivo,'w') as arquivo:
       
       if ordem != None:

        arquivo.write(f'{algoritmo}-{ordem};{n}\n')

       else:

        arquivo.write(f'{algoritmo};{n}\n')

       for item in resultado:
           
           arquivo.write(str(item)+"\n")

       arquivo.flush()

       arquivo.close()

def executaExperimento(nome, numeros, funcao):

    resultado = []

    for n in numeros:

        if n % 100 == 0:

            print(f"Executando {nome}: {n}")

        resultado.append(medirTempo(funcao, n))

    salvaResultado(nome, numeros[-1], resultado)

    print(f"{nome} finalizado.")


if __name__ == "__main__":

    algoritmos = [
    "Historico-Pilha-Array",
    "Historico-Pilha-Lista",

    "Fila-Impressao-Array",
    "Fila-Impressao-Lista",

    "Playlist-Lista-Array",
    "Playlist-Lista-Ligada",
]
   
    funcoes = [
    pa.historico,
    pl.historico,

    fa.filaImpressao,
    fl.filaImpressao,

    la.playlist,
    ll.playlist,
]

    for i, nome in enumerate(algoritmos):
        print(f"[{i+1}] {nome}")

    opcao = int(input("Escolha uma opção: "))

    if 1 <= opcao <= len(funcoes):

        n = int(input("Quantidade máxima de operações: "))

        numeros = list(range(1, n + 1))

        print("Executando...")

        executaExperimento(
            algoritmos[opcao - 1],
            numeros,
            funcoes[opcao - 1]
        )
    else:
        print("Ação Inválida")