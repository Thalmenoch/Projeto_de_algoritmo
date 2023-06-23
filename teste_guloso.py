def linha_de_montagem_guloso(tempo, troca, entrada, saida):
    estacao = len(tempo[0])  # número de estações na linha de montagem
    tempo_total = [[0] * estacao for _ in range(2)]  # matriz para armazenar os tempos totais

    # Definir tempos iniciais
    tempo_total[0][0] = entrada[0] + tempo[0][0]
    tempo_total[1][0] = entrada[1] + tempo[1][0]

    # Preencher a matriz de tempos totais
    for i in range(1, estacao):
        tempo_total[0][i] = min(tempo_total[0][i-1] + tempo[0][i], tempo_total[1][i-1] + tempo[0][i] + troca[1][i-1])
        tempo_total[1][i] = min(tempo_total[1][i-1] + tempo[1][i], tempo_total[0][i-1] + tempo[1][i] + troca[0][i-1])

    # Calcular o tempo total mínimo de montagem, ou seja,
    # escolhe a proxima estacao, linha 1 ou linha 2, com base no menor custo local
    tempo_minimo = min(tempo_total[0][estacao-1] + saida[0], tempo_total[1][estacao-1] + saida[1])

    # Recuperar a solução encontrada
    caminho = []
    linha = 0 if tempo_total[0][estacao-1] + saida[0] < tempo_total[1][estacao-1] + saida[1] else 1
    caminho.append(linha + 1)

    for i in range(estacao - 2, -1, -1):
        if linha == 0:
            linha = 0 if tempo_total[0][i] + tempo[0][i] <= tempo_total[1][i] + tempo[0][i] + troca[1][i] else 1
        else:
            linha = 1 if tempo_total[1][i] + tempo[1][i] <= tempo_total[0][i] + tempo[1][i] + troca[0][i] else 0
        caminho.append(linha + 1)

    caminho.reverse()

    return tempo_minimo, caminho


# Exemplo de uso
# tempos = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
# trocas = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
# entrada = [2, 4]
# saida = [3, 2]

# tempo_min, caminho_guloso = linha_de_montagem_guloso(tempos, trocas, entrada, saida)
# print("Tempo mínimo de montagem (guloso):", tempo_min)
# print("Caminho encontrado (guloso):", caminho_guloso)
