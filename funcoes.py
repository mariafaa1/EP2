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
        contador = 0
        for j in range(len(dados_rolados)):
            if dados_rolados[j] == dados_rolados[i]:
                contador += 1
        if contador >= 4:
            soma = 0
            for valor in dados_rolados:
                soma += valor
            return soma
    return 0


# EXERCÍCIO 10
def calcula_pontos_quina(dados_rolados):
    for i in range(len(dados_rolados)):
        contador = 0
        for j in range(len(dados_rolados)):
            if dados_rolados[j] == dados_rolados[i]:
                contador += 1
        if contador >= 5:
            return 50
    return 0


# EXERCÍCIO 11
def calcula_pontos_regra_avancada(dados_rolados):
    pontos = {"cinco_iguais": calcula_pontos_quina(dados_rolados), "full_house": calcula_pontos_full_house(dados_rolados), "quadra": calcula_pontos_quadra(dados_rolados), "sem_combinacao": calcula_pontos_soma(dados_rolados), "sequencia_alta": calcula_pontos_sequencia_alta(dados_rolados), "sequencia_baixa": calcula_pontos_sequencia_baixa(dados_rolados)}   
    return pontos


# EXERCÍCIO 12
def faz_jogada(dados_rolados, categoria, cartela_de_pontos):
    if categoria in ["1", "2", "3", "4", "5", "6"]:
        categoria_int = int(categoria)
        pontos_simples = calcula_pontos_regra_simples(dados_rolados)
        cartela_de_pontos['regra_simples'][categoria_int] = pontos_simples[categoria_int]
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados_rolados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    return cartela_de_pontos


# EXERCÍCIO 13
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)