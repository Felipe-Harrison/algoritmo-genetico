import numpy as np

def analisarResultados(numeros:list) -> dict:
    return {
        'media': np.average(numeros),
        'desvio': np.std(numeros)
    }

def adicionarRegistro(registro,arquivo):
    with open(arquivo,"+a") as f:
        f.write(registro + "\n")
        f.close()

def registrarGrupo(grupo,arquivo):
    with open(arquivo,'+a') as f:
        line = f"Melhor -> Mochila: {grupo[0].itens} R${grupo[0].valor} Valido:{grupo[0].valido} \n"
        f.write(line)
        line = f"Pior -> Mochila: {grupo[-1].itens} R${grupo[-1].valor} Valido:{grupo[-1].valido} \n"
        f.write(line)
        f.close()

def registrarResultado(arquivo,texto,grupo):
    adicionarRegistro(texto,arquivo)
    registrarGrupo(grupo,arquivo)
    resultado = analisarResultados([item.valor for item in grupo])
    adicionarRegistro(f"Media: {resultado['media']} Desvio: {resultado['desvio']}",arquivo)
