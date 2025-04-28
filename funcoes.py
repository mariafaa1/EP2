# EXERCÍCIO 1
import random
def rolar_dados(n):
    lista = []
    i = 0
    while i < n:
        s = random.randint(1,6)
        lista.append(s)
        i+=1
    return lista


# EXERCÍCIO 2
def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    del dados_rolados[dado_para_guardar]
    return [dados_rolados,dados_no_estoque]


# EXERCÍCIO 3
def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    del dados_no_estoque[dado_para_remover]
    return [dados_rolados,dados_no_estoque]


# EXERCÍCIO 4
def calcula_pontos_regra_simples(dados_rolados):
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in dados_rolados:
        if dado in pontos:
            pontos[dado] += dado
        else:
            pontos[dado] = dado  
    return pontos


# EXERCÍCIO 5
def calcula_pontos_soma(dados_rolados):
    soma = 0
    for dado in dados_rolados:
        soma += dado
    return soma


#EXERCICIO 6
def calcula_pontos_sequencia_baixa(dados):
    
    if len(dados) < 4:
        return 0

    n = len(dados)
    for i in range(n):
        for j in range(n):
            if j == i:
                
        for k in range(n):
            if k == i or k == j:
                    
        for l in range(n):
            if l == i or l == j or l == k:
                        

                    
            possivel_sequencia = sorted([dados[i], dados[j], dados[k], dados[l]])
            if possivel_sequencia == [1, 2, 3, 4] or possivel_sequencia == [2, 3, 4, 5] or possivel_sequencia == [3, 4, 5, 6]:
                 return 15

    return 0

# Exemplos de uso:
print(calcula_pontos_sequencia_baixa([1, 2, 3, 4, 6]))   # Saída: 15
print(calcula_pontos_sequencia_baixa([5, 4, 3, 2, 1]))   # Saída: 15
print(calcula_pontos_sequencia_baixa([2, 3, 4, 5]))      # Saída: 15
print(calcula_pontos_sequencia_baixa([6, 5, 4, 3]))      # Saída: 15
print(calcula_pontos_sequencia_baixa([1, 1, 2, 3, 4]))   # Saída: 15
print(calcula_pontos_sequencia_baixa([1, 3, 4, 5, 6]))   # Saída: 0
print(calcula_pontos_sequencia_baixa([1, 2, 4, 5]))      # Saída: 0
print(calcula_pontos_sequencia_baixa([1, 2, 3]))        # Saída: 0