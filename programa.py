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
rodadas = 0
while -1 in cartela_de_pontos['regra_simples'].values() and rodadas != 12 or -1 in cartela_de_pontos['regra_avancada'].values() and rodadas != 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    reroladas = 0
    rodada_em_andamento = True
    rodadas +=1
    invalido = False
    while rodada_em_andamento:
        if invalido == False:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            jogada = input(("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
        invalido = False
        if jogada == '1':
            dado_para_guardar = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, dado_para_guardar)

        elif jogada == '2':
            dado_para_remover = int(input("Digite o índice do dado a ser removido (0 a 4):"))
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, dado_para_remover)

        elif jogada == '3':
            if reroladas < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                reroladas += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif jogada == '4':
            imprime_cartela(cartela_de_pontos)

        elif jogada == '0':
            categoria = input("Digite a combinação desejada:")
            jogada_feita = False
            while not jogada_feita:
                if categoria.isdigit():
                    categoria_int = int(categoria)
                else:
                    categoria_int = None
                if categoria_int in cartela_de_pontos['regra_simples']:
                    if cartela_de_pontos['regra_simples'][int(categoria)] == -1:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela_de_pontos)
                        jogada_feita = True
                    else:
                        print("Essa combinação já foi utilizada.")
                elif categoria in cartela_de_pontos['regra_avancada']:
                    if cartela_de_pontos['regra_avancada'][categoria] == -1:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela_de_pontos)
                        jogada_feita = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            rodada_em_andamento = False

total_simples = 0
for pontos in cartela_de_pontos['regra_simples'].values():
    if pontos != -1:
        total_simples += pontos

total_avancada = 0
for pontos in cartela_de_pontos['regra_avancada'].values():
    if pontos != -1:
        total_avancada += pontos

bonus = 35 if total_simples >= 63 else 0

imprime_cartela(cartela_de_pontos)
total = total_simples + total_avancada + bonus
print(f"Pontuação total: {total}")

