#EXERCICIO 1
import random
def rolar_dados(n):
    lista = []
    i = 0
    while i < n:
        s = random.randint(1,6)
        lista.append(s)

        i+=1

    return lista

#EXERCÍCIO 2
def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    lista = []
    lista.append(dados_no_estoque)
    lista.append(dados_rolados)
    return lista



