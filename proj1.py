#Algoritmo genético para resolução de problema da mochila binária
import time
import random

class Cromossomo:
    def __init__(self, itens, tamanhoMaximo) -> None:
        self.itens = itens
        self.max = tamanhoMaximo
        self.len = len(itens)
        self.aptidao = 0.0
    
    def avalia(self,itensDisponiveis) -> tuple:
        tamanhoAtual = 0
        valorAtual = 0
        
        for i in range(len(self.itens)):
            tamanhoAtual += self.itens[i] * itensDisponiveis[i]['w']
            valorAtual += self.itens[i] * itensDisponiveis[i]['v']
        
        eValido = tamanhoAtual < self.max

        if not eValido:
            valorAtual = -1
        
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
    
    # gerar grupo de soluções aleatórias
    
    maxTamanhoGrupo = 10
    grupo = [
        Cromossomo([ random.randint(0,1) for _ in range(len(itensDisponiveis))],mochilaTamanho) for _ in range(maxTamanhoGrupo)
    ]
    
    # loop:

    numInteracoes = 1
        # Avalia grupo, rankeando as melhores
    for i in range(numInteracoes):   
        grupo.sort(key= lambda item: item.avalia(itensDisponiveis)[1], reverse=True)

        # Cross over
        for i in grupo:
            print(i.itens,i.avalia(itensDisponiveis))
        
        # Selecionar os pais
        populacaoInter = []

        #Elitismo manter o melhor
        populacaoInter.append(grupo[0])

        while len(populacaoInter) < (maxTamanhoGrupo/2):
            escolhido = random.randint(1,len(grupo)-1)
            populacaoInter.append(grupo[escolhido])
        
        print("Pais")
        for i in populacaoInter:
            print(i.itens,i.avalia(itensDisponiveis))
        
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