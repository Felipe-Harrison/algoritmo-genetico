import numpy as np
import re
import time
from os import walk

def knapsack(size, value, weight, capacity, dp):
    if size == 0 or capacity == 0:
        return 0
    if dp[size - 1][capacity] != -1:
        return dp[size - 1][capacity]
    if weight[size - 1] > capacity:
        dp[size - 1][capacity] = knapsack(size - 1, value, weight, capacity, dp)
        return dp[size - 1][capacity]
    a = value[size - 1] + knapsack(size - 1, value, weight, capacity - weight[size - 1], dp)
    b = knapsack(size - 1, value, weight, capacity, dp)
    dp[size - 1][capacity] = max(a, b)
    return dp[size - 1][capacity]

def solve_knapsack_problem(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    capacity = int(lines[-1].strip())
    
    id, value, weight = [], [], []
    for line in lines[1:-1]:
        numbers = re.findall(r"[0-9]+", line)
        id.append(int(numbers[0]) - 1)
        value.append(int(numbers[1]))
        weight.append(int(numbers[2]))
    
    dp = np.full((n, capacity + 1), -1, dtype=int)
    max_value = knapsack(n, value, weight, capacity, dp)
    return max_value

def main():
    output_max_values = []
    
    # Alteração: Mudar maneira como é feito o input
    for _,_,files in walk("./inputs/"):
        for file in files:
            if file.endswith(".in"):
                try:
                    max_value = solve_knapsack_problem("./inputs/"+file)
                    output_max_values.append(max_value)
                    output_line = f"Instancia {file} : {max_value}\n"
                except:
                    output_line = f"Erro na instancia {file}\n"
                    
                with open("./outputs/valoresIdeiais.out", "a+") as output_file:
                    output_file.write(output_line)

def dynamic(path):
    try:
        max_value = solve_knapsack_problem(path)
    except:
        max_value = 0
    
    return max_value

if __name__ == "__main__":
    
    for i in range(5):
        print(f"Teste {i+1}")
        with open("./outputs/valoresIdeiais.out", "a+") as output_file:
            output_file.write(f"Teste {i+1}\n")
        start_time = time.time()
        main()
        execution_time = time.time() - start_time
        print(f"Execution time: {execution_time} seconds\n")
        with open("./outputs/valoresIdeiais.out", "a+") as output_file:
            output_file.write(f"Execution time: {execution_time} seconds\n")
    
