#Algoritmo genético para resolução de problema da mochila binária
import time
import random

class Mochila:
    def __init__(self, itens, tamanhoMaximo) -> None:
        self.itens = itens
        self.max = tamanhoMaximo
        self.len = len(itens)
        pass
    
    def avalia(self,itensDisponiveis):
        tamanhoAtual = 0
        valorAtual = 0
        
        for i in range(len(self.itens)):
            tamanhoAtual += self.itens[i] * itensDisponiveis[i]['w']
            valorAtual += self.itens[i] * itensDisponiveis[i]['v']
        
        eValido = tamanhoAtual < self.max
        
        return eValido,valorAtual
    
def teste():
    
    itensDisponiveis = [
        { 'w': 5, "v": 3, },
        { 'w': 4, "v": 6, },
        { 'w': 3, "v": 9, },
        { 'w': 2, "v": 12, },
        { 'w': 1, "v": 15, },
    ]
    mochilaTamanho = 10
    
    # Carregar a mochila
    
    
    # gerar grupo de soluções aleatórias
    
    maxTamanhoGrupo = 10
    grupo = [
        Mochila([ random.randint(0,1) for _ in range(len(itensDisponiveis))],mochilaTamanho) for _ in range(maxTamanhoGrupo)
    ]
    
    # loop:

    numInteracoes = 1
        # Avalia grupo, rankeando as melhores
    for i in range(numInteracoes):   
        grupo.sort(key= lambda item: item.avalia(itensDisponiveis)[1], reverse=True)

        for i in grupo:
            print(i.itens,i.avalia(itensDisponiveis)[1])
        
        # Cross over
            # Selecionar os pais
            # Cruzar 
        # Mutação dos filhos
        
        # Avaliar os filhos
        
        # Reformular grupo
    
    # goto loop:

    
    
    
    


if __name__ == "__main__":
    start = time.time()
    teste()
    finish = time.time() - start
    print(finish)