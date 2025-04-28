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


# EXERCÍCIO 6
def calcula_pontos_sequencia_baixa(dados_rolados):
    dados = []
    for dado in dados:
        if dado not in dados:
            dados.append(dado)
    for i in range(len(dados)):
        for j in range(0, len(dados)-i-1):
            if dados[j] > dados[j+1]:
                dados[j], dados[j+1] = dados[j+1], dados[j]

    for k in range(len(dados)):
        contador = 1 
        atual = dados[k]
        for t in range(k + 1, len(dados)):  
            if dados[t] == atual + 1:
                contador += 1
                atual = dados[t]
            if contador == 4:
                return 15
    return 0
