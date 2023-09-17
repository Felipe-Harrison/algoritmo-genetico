import time

from inputReader import getInputs
from algoritmos.genetic import algoritmoGenetico
from algoritmos.dynamic import dynamic
from analisarResultados import analisarResultados,analisarFrequencia

pathEntrada = "./inputs/"
pathSaida = "./outputs/"

def Main():
    
    # Realizar a analise comparativa dos algoritmos
    
    entradas = getInputs(path=pathEntrada)
    
    numeroExecucoes = 30
    
    for entrada in entradas:
        
        temposGastos = []
        valoresObtidos = []
        
        # Programacao dinamica
        for _ in range(numeroExecucoes):
            start = time.time()
            valor = dynamic(entrada['input'])
            finish = time.time() - start
            valoresObtidos.append(valor)
            temposGastos.append(finish)

        analise = analisarResultados(temposGastos)
        valores = analisarFrequencia(valoresObtidos)
        
        with open("./outputs/dynamic.out", "a+") as output_file:
            output_file.write(f"{entrada['input']}\n")
            output_file.write(f"Media tempo: {analise['media']}\n")
            output_file.write(f"Desvio tempo: {analise['desvio']}\n")
            output_file.write("Frequencia de valores\n")
            for valor in valores:  
                output_file.write(f"{valor[0]} {valor[1]}\n")
            output_file.write("\n")
        
        temposGastos = []
        valoresObtidos = []
        
        # Algoritmo Genético
        for _ in range(numeroExecucoes):
            start = time.time()
            valor = algoritmoGenetico(
                itensDisponiveis=entrada['itens'],
                capacidadeMaxMochila=entrada['capacidadeMochila'],
                maxTamanhoGrupo = 20,
                numeroInteracoes = 50000,
                taxaMutacao= 0.15,
            )
            finish = time.time() - start
            valoresObtidos.append(valor.valor)
            temposGastos.append(finish)

        analise = analisarResultados(temposGastos)
        valores = analisarFrequencia(valoresObtidos)
        
        with open("./outputs/genetic.out", "a+") as output_file:
            output_file.write(f"{entrada['input']}\n")
            output_file.write(f"Media tempo: {analise['media']}\n")
            output_file.write(f"Desvio tempo: {analise['desvio']}\n")
            output_file.write("Frequencia de valores\n")
            for valor in valores:  
                output_file.write(f"{valor[0]} {valor[1]}\n")
            output_file.write("\n")     
        
if __name__ == "__main__":
    start = time.time()
    Main()
    finish = time.time() - start
    print(f"Execução total da analise: {finish} segundos")