#Algoritmo genético para resolução de problema da mochila binária
import random
from inputReader import getInputs
import time

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
        
        eValido = tamanhoAtual <= self.tamMochila

        # inválidos: valor negativo
        if not eValido:
            valorAtual *= -1
        
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

def realizaTorneio(grupoCromossomos,k = 2) -> Cromossomo:

    # Selecionar no grupo k elementos para fazer o torneio
    cromossomosSelecionados = random.choices(grupoCromossomos,k=k)

    # Seleciona o melhor
    ordenarGrupo(cromossomosSelecionados)

    return cromossomosSelecionados[0]
    
def algoritmoGenetico(
        itensDisponiveis: list,
        capacidadeMaxMochila: int,
        maxTamanhoGrupo = 10,
        numeroInteracoes = 100,  
        taxaMutacao = 0.2,
        taxaSubstituicao = 0.4,
    ) -> Cromossomo:
    
    # gerar grupo Inicial de soluções aleatórias, Ordenado
    grupo = criarGrupo(
        numCromossomos=maxTamanhoGrupo,
        tamanhoMaximoMochila=capacidadeMaxMochila,
        itensDisponiveis=itensDisponiveis
    )

    # Salvar Registro Grupo Inicial
    # registrarResultado("./resultados3.txt","Grupo Inicial",grupo)
    # print("Grupo Inicial")
    # for item in grupo:
    #     print(item.itens,item.valor,item.valido)

    # Algoritmo genetico

    # Definir número de pais que vão reproduzir
    numeroPais = 2 #int(taxaSubstituicao* maxTamanhoGrupo)

    for _ in range(numeroInteracoes):
        
    # Cross over

        # Selecionar os pais
        populacaoIntermediaria = []

        # Elitismo: Escolher o melhor cromossomo
        populacaoIntermediaria.append(grupo[0])

        # Realizar torneio
        while len(populacaoIntermediaria) < numeroPais:
            escolhido = realizaTorneio(grupo,2)
            populacaoIntermediaria.append(escolhido)
        
        # Cruzamento
        filhos = []
        for i in range(0,numeroPais,2):
            filhos.extend(list(cruzar(populacaoIntermediaria[i],populacaoIntermediaria[i+1])))

        # Mutação dos filhos e avaliação
        for filho in filhos:
            filho.mutacao(taxaMutacao = taxaMutacao)
            filho.avalia(itensDisponiveis)

    # Reformular grupo

        # Substituir os 4 piores pelos novos filhos
        pontoSeparacaoGrupo = (len(filhos)+1)*-1
        del grupo[pontoSeparacaoGrupo:-1]
        grupo.extend(filhos)
        ordenarGrupo(grupo)
        
    # endLoop Interações
    
    #Retornar o melhor cromossomo obtido
    return grupo[0]

if __name__ == "__main__":
    
    entradas = getInputs(path="./inputs/")
    
    numeroExecuções = 5
    
    for i in range(numeroExecuções):
        
        print(f"Teste {i+1}")
        with open("./outputs/genetic.out", "a+") as output_file:
            output_file.write(f"Teste {i+1}\n")
        
        start_time = time.time()
        
        for entrada in entradas:
            melhorResultado = algoritmoGenetico(
                itensDisponiveis=entrada['itens'],
                capacidadeMaxMochila=entrada['capacidadeMochila'],
                maxTamanhoGrupo = 20,
                numeroInteracoes = 50000,
                taxaMutacao=0.15,
            )
            with open("./outputs/genetic.out", "a+") as output_file:
                output_file.write(f"Instancia {entrada['input']} : {melhorResultado.valor}\n") 
                
        execution_time = time.time() - start_time
        print(f"Execution time: {execution_time} seconds\n")
        with open("./outputs/genetic.out", "a+") as output_file:
            output_file.write(f"Execution time: {execution_time} seconds\n")
