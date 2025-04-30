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
    for dado in dados_rolados:
        if dado not in dados:
            dados.append(dado)
    for i in range(len(dados)):
        for j in range(0, len(dados)-i-1):
            if dados[j] > dados[j+1]:
                dados[j], dados[j+1] = dados[j+1], dados[j]
    for i in range(len(dados)):
        contador = 1 
        atual = dados[i]
        for j in range(i + 1, len(dados)):  
            if dados[j] == atual + 1:
                contador += 1
                atual = dados[j]
            if contador == 4:
                return 15
    return 0


# EXERCÍCIO 7
def calcula_pontos_sequencia_alta(dados_rolados):
    dados = []
    for dado in dados_rolados:
        if dado not in dados:
            dados.append(dado)
    for i in range(len(dados)):
        for j in range(0, len(dados)-i-1):
            if dados[j] > dados[j+1]:
                dados[j], dados[j+1] = dados[j+1], dados[j]
    for i in range(len(dados)):
        contador = 1 
        atual = dados[i]
        for j in range(i + 1, len(dados)):  
            if dados[j] == atual + 1:
                contador += 1
                atual = dados[j]
            if contador == 5:
                return 30
    return 0


# EXERCÍCIO 8
def calcula_pontos_full_house(dados_rolados):
    for i in range(len(dados_rolados)):
        for j in range(0, len(dados_rolados)-i-1):
            if dados_rolados[j] > dados_rolados[j+1]:
                dados_rolados[j], dados_rolados[j+1] = dados_rolados[j+1], dados_rolados[j]
    soma = 0
    c1 = dados_rolados[0] == dados_rolados[1]
    c2 = dados_rolados[2] == dados_rolados[3] == dados_rolados[4]
    c3 = dados_rolados[1] != dados_rolados[2]
    c4 = dados_rolados[0] == dados_rolados[1] == dados_rolados[2]
    c5 = dados_rolados[3] == dados_rolados[4]
    c6 = dados_rolados[2] != dados_rolados[3]   
    if (c1 and c2 and c3)  or (c4 and c5 and c6):
       for i in range(len(dados_rolados)):            
            soma += dados_rolados[i]
    return soma


# EXERCÍCIO 9
def calcula_pontos_quadra(dados_rolados):
    for i in range(len(dados_rolados)):
        for j in range(0, len(dados_rolados)-i-1):
            if dados_rolados[j] > dados_rolados[j+1]:
                dados_rolados[j], dados_rolados[j+1] = dados_rolados[j+1], dados_rolados[j]
    soma = 0
    c1 = dados_rolados[0] == dados_rolados[1] == dados_rolados[2] == dados_rolados[3]
    c2 = dados_rolados[3] != dados_rolados[4]
    c3 = dados_rolados[1] == dados_rolados[2] == dados_rolados[3] == dados_rolados[4]
    c4 = dados_rolados[0] != dados_rolados[1]
    if (c1 and c2)  or (c3 and c4):
       for i in range(len(dados_rolados)):           
            soma += dados_rolados[i]
    return soma