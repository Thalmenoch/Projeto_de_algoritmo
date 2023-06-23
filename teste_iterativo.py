def linha_de_montagem(tempo, troca, entrada, saida):
    estacao = len(tempo[0])  # número de estações na linha de montagem
    tempo_total = [[0] * estacao for _ in range(2)]  # matriz para armazenar os tempos totais
    caminho_otimo = [[0] * estacao for _ in range(2)]  # matriz para rastrear o caminho ótimo

    # Definir tempos iniciais
    tempo_total[0][0] = entrada[0] + tempo[0][0]
    tempo_total[1][0] = entrada[1] + tempo[1][0]

    # Preencher a matriz de tempos totais e rastrear o caminho ótimo
    for i in range(1, estacao):
        if tempo_total[0][i-1] + tempo[0][i] <= tempo_total[1][i-1] + tempo[0][i] + troca[1][i-1]:
            tempo_total[0][i] = tempo_total[0][i-1] + tempo[0][i]
            caminho_otimo[0][i] = 0
        else:
            tempo_total[0][i] = tempo_total[1][i-1] + tempo[0][i] + troca[1][i-1]
            caminho_otimo[0][i] = 1

        if tempo_total[1][i-1] + tempo[1][i] <= tempo_total[0][i-1] + tempo[1][i] + troca[0][i-1]:
            tempo_total[1][i] = tempo_total[1][i-1] + tempo[1][i]
            caminho_otimo[1][i] = 1
        else:
            tempo_total[1][i] = tempo_total[0][i-1] + tempo[1][i] + troca[0][i-1]
            caminho_otimo[1][i] = 0

    # Calcular o tempo total mínimo de montagem
    tempo_minimo = min(tempo_total[0][estacao-1] + saida[0], tempo_total[1][estacao-1] + saida[1])

    # Recuperar o caminho ótimo
    caminho = []
    linha = 0 if tempo_total[0][estacao-1] + saida[0] < tempo_total[1][estacao-1] + saida[1] else 1
    caminho.append(linha + 1)

    for i in range(estacao - 2, -1, -1):
        linha = caminho_otimo[linha][i]
        caminho.append(linha + 1)

    caminho.reverse()

    return tempo_minimo, caminho


# Exemplo de uso
# tempos = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
# trocas = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
# entrada = [2, 4]
# saida = [3, 2]

# tempo_min, caminho_otimo = linha_de_montagem(tempos, trocas, entrada, saida)
# print("Tempo mínimo de montagem:", tempo_min)
# print("Caminho ótimo:", caminho_otimo)
