import time

from algoritmo1 import algoritmoGenetico as algoritmo1

def Main():

    # Mochila 1
    # Resposta ideal = 42
    itensDisponiveis = [
        { 'w': 5, "v": 3, },
        { 'w': 4, "v": 6, },
        { 'w': 3, "v": 9, },
        { 'w': 2, "v": 12, },
        { 'w': 1, "v": 15, },
    ]
    mochilaTamanhoMaximo = 10

    # Mochila 2
    # Resposta ideal = 60
    # itensDisponiveis = [
    #         { 'w': 1, "v": 20, },
    #         { 'w': 2, "v": 5, },
    #         { 'w': 3, "v": 10, },
    #         { 'w': 8, "v": 40, },
    #         { 'w': 7, "v": 15, },
    #         { 'w': 4, "v": 25, },
    #     ]
    # mochilaTamanhoMaximo = 10

    algoritmo1(
        itensDisponiveis=itensDisponiveis,
        capacidadeMaxMochila=mochilaTamanhoMaximo
    )

if __name__ == "__main__":
    start = time.time()
    Main()
    finish = time.time() - start
    print(finish)