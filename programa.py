import random
from funcoes import *
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela_de_pontos)

n = 5
dados_rolados = rolar_dados(n)
dados_no_estoque = []
rerrolagens = 0
rodadas = 0

while rodadas < 12:
    jogada_concluida = False 

    while not jogada_concluida:
        print(f"\nDados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_no_estoque}")
        jogada = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")

        if jogada == "1":
            dado_para_guardar = int(input("Digite o índice do dado a ser guardado (0 a 4): "))
            guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar)

        elif jogada == "2":
            dado_para_guardar = int(input("Digite o índice do dado a ser removido (0 a 4): "))
            remover_dado(dados_rolados, dados_no_estoque, dado_para_guardar)
        elif jogada == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(n)
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif jogada == "4":
            imprime_cartela(cartela_de_pontos)

        
        elif jogada == "0":
            categoria = input("Digite a combinação desejada: ")

            categorias_validas = ["1", "2", "3", "4", "5", "6","cinco_iguais", "full_house", "quadra","sem_combinacao", "sequencia_alta", "sequencia_baixa"]

            if categoria in categorias_validas:
                if categoria in cartela_de_pontos and cartela_de_pontos[categoria] == -1:
                    faz_jogada(dados_rolados + dados_no_estoque, categoria, cartela_de_pontos)
                    jogada_concluida = True
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    dados_rolados = rolar_dados(n)
    dados_no_estoque = []
    rerrolagens = 0
    rodadas += 1

pontos_simples = calcula_pontos_regra_simples(cartela_de_pontos)
pontos_avancados = calcula_pontos_regra_avancada(cartela_de_pontos)
if pontos_simples >= 63:
    bonus = 35 
else: 
    bonus = 0
pontuacao_final = pontos_simples + pontos_avancados + bonus

print(f"\nPontuação total: {pontuacao_final}")