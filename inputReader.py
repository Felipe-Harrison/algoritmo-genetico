from os import walk

# Arquivo Input Estrutura
# Total Itens
# Item(id,value,weight)
# ...
# Capacidade Mochila


def getItens(inputFile:str) -> dict:
    
    numItens = 0
    capacidade = 0
    itens = []
    
    with open(inputFile,'r') as f:
        lines = f.readlines()
        capacidade = int(lines.pop(-1))
        numItens = int(lines.pop(0))
        for line in lines:
            _,value,weight = line.split()
            itens.append({
                'v': int(value), 'w': int(weight)
            })
        f.close()
    
    return {
        'input': inputFile,
        'numItens': numItens,
        'capacidadeMochila': capacidade,
        'itens': itens
    }
        
def getInputs(path:str) -> list:
    '''
    Retorna lista com os dados dos arquivos de entrada no path informado
    
    Returns:
        [{
            'input': nome do arquivo de entrada\n
            'numItens': Numero total de itens disponiveis\n
            'capacidadeMochila': capacidade maxima da mochila\n
            'itens': itens disponiveis
        }]
    '''
    
    inputs = []
    
    for _,_,files in walk(path):
        for file in files:
            if file.endswith(".in"):
                inputData = getItens(path+ file) 
                inputs.append(inputData)
    
    return inputs
                
if __name__ == "__main__":
    inputs = getInputs("./inputs/")
    for input in inputs:
        print(input['input'],input['capacidadeMochila'])
