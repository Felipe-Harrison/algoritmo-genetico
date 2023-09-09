#Algoritmo genético para resolução de problema da mochila binária
import time
import random

class Cromossomo:
    def __init__(self,itens,tamanhoMaxMochila) -> None:
        self.itens = itens
        self.tamMochila = tamanhoMaxMochila
        self.aptidao = 0.0
        self.valido = False
        self.valor = 0
    
    def avalia(self, itensDisponiveis) -> None:
        tamanhoAtual = 0
        valorAtual = 0
        
        for i,item in enumerate(self.itens):
            tamanhoAtual += item * itensDisponiveis[i]['w']
            valorAtual += item * itensDisponiveis[i]['v']
        
        eValido = tamanhoAtual < self.tamMochila

        if not eValido:
            valorAtual = -1
        
        # Salvar valores no cromossomo, evitar recalcular
        self.valido = eValido
        self.valor = valorAtual

    def calculaAptidao(self,totalValoresGrupo):
        if(totalValoresGrupo > 0):
            self.aptidao = self.valor/totalValoresGrupo
    
    def mutacao(self,taxaMutacao = 0.2):
        for i,item in enumerate(self.itens):
            probabilidade = random.random()
            if(probabilidade <= taxaMutacao):
                self.itens[i] = 0 if item == 1 else 1


def cruzar(cromossomo1,cromossomo2):
    
    pontoCorte = random.randint(1,len(cromossomo1.itens)-1)
    head1,tail1 = cromossomo1.itens[0:pontoCorte],cromossomo1.itens[pontoCorte:]
    head2,tail2 = cromossomo2.itens[0:pontoCorte],cromossomo2.itens[pontoCorte:]

    head1.extend(tail2)
    head2.extend(tail1)

    filho1 = Cromossomo(head1,cromossomo1.tamMochila)
    filho2 = Cromossomo(head2,cromossomo1.tamMochila)

    return filho1,filho2

def criarGrupo(numCromossomos,tamanhoMaximoMochila,itensDisponiveis) -> list[Cromossomo]:
    
    numeroItens = len(itensDisponiveis)
    novoGrupo = [
        Cromossomo(
            [
                random.randint(0,1) for _ in range(numeroItens)
            ],
            tamanhoMaximoMochila
        ) for _ in range(numCromossomos)
    ]

    for cromossomo in novoGrupo:
        cromossomo.avalia(itensDisponiveis)
    
    ordenarGrupo(novoGrupo)
    return novoGrupo

def ordenarGrupo(grupoCromossomos) -> None:
    grupoCromossomos.sort(key= lambda item: item.valor, reverse=True)

def realizaTorneio(grupoCromossomos,k) -> Cromossomo:

    cromossomosSelecionados = random.choices(grupoCromossomos,k=k)

    # Seleciona o melhor
    ordenarGrupo(cromossomosSelecionados)

    return cromossomosSelecionados[0]
    
def Main():

    #itensDisponiveis = [
    #        { 'w': 5, "v": 3, },
    #        { 'w': 4, "v": 6, },
     #       { 'w': 3, "v": 9, },
    #        { 'w': 2, "v": 12, },
    #        { 'w': 1, "v": 15, },
    #    ]
    #mochilaTamanhoMaximo = 10

    itensDisponiveis = [
            { 'w': 1, "v": 20, },
            { 'w': 2, "v": 5, },
            { 'w': 3, "v": 10, },
            { 'w': 8, "v": 40, },
            { 'w': 7, "v": 15, },
            { 'w': 4, "v": 25, },
        ]
    mochilaTamanhoMaximo = 10
            
    # gerar grupo Inicial de soluções aleatórias, Ordenado

    maxTamanhoGrupo = 10
    grupo = criarGrupo(
        numCromossomos=maxTamanhoGrupo,
        tamanhoMaximoMochila=mochilaTamanhoMaximo,
        itensDisponiveis=itensDisponiveis
    )

    print("Grupo Inicial")
    for item in grupo:
        print(item.itens,item.valor,item.valido)

    # Algoritmo genetico
    numeroInteracoes = 100
    numeroPais = maxTamanhoGrupo - 2

    for _ in range(numeroInteracoes):

    # Cross over
    
        # Selecionar os pais
        populacaoIntermediaria = []

        #Elitismo manter o melhor
        populacaoIntermediaria.append(grupo[0])

        #Realizar torneio
        while len(populacaoIntermediaria) < numeroPais:
            escolhido = realizaTorneio(grupo,2)
            populacaoIntermediaria.append(escolhido)
        
        #Cruzamento

        filhos = []
        for i in range(0,numeroPais,2):
            filhos.extend(list(cruzar(populacaoIntermediaria[i],populacaoIntermediaria[i+1])))

        # Mutação dos filhos
        # Avaliar os filhos
        for filho in filhos:
            filho.mutacao()
            filho.avalia(itensDisponiveis)

        # Reformular grupo

        #Manter melhor e pior e mudar os demais

        melhorCromossomo,piorCromossomo = grupo[0],grupo[-1]
        novogrupo = filhos
        novogrupo.extend([melhorCromossomo,piorCromossomo])
    
        ordenarGrupo(novogrupo)
        grupo = novogrupo

    # goto loop:
    print("Grupo Final")
    for item in grupo:
        print(item.itens,item.valor,item.valido)



if __name__ == "__main__":
    start = time.time()
    Main()
    finish = time.time() - start
    print(finish)