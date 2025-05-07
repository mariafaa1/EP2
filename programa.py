elif opcao == '0':
    print("Digite a combinação desejada:")
    jogada_feita = False
    while not jogada_feita:
        resposta = input()
        if resposta.isdigit():
            resposta_int = int(resposta)
        else:
            resposta_int = None
        if resposta_int in cartela['regra_simples']:
            if cartela['regra_simples'][resposta_int] == -1:
                f.faz_jogada(dados_rolados + dados_guardados, resposta, cartela)
                jogada_feita = True
            else:
                print("Essa combinação já foi utilizada.")
        elif resposta in cartela['regra_avancada']:
            if cartela['regra_avancada'][resposta] == -1:
                f.faz_jogada(dados_rolados + dados_guardados, resposta, cartela)
                jogada_feita = True
            else:
                print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
    rodada_em_andamento = False
