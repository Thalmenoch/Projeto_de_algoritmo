
# tem q modificar ainda 
# n tá no padrão desejado para o modelo de entrada 
def linha_montagem(tempos_estacoes, tempos_transferencia, tempo_entrada, tempo_saida):
    n = len(tempos_estacoes[0])  # número de estações de trabalho
    linha_atual = 0  # linha atual
    tempo_total = tempo_entrada  # tempo total inicial

    # Percorre cada estação de trabalho
    for i in range(n):
        # Escolhe a estação de trabalho mais rápida na linha atual
        if tempos_estacoes[linha_atual][i] + tempos_transferencia[linha_atual][i] <= tempos_estacoes[1-linha_atual][i] + tempos_transferencia[1-linha_atual][i]:
            tempo_total += tempos_estacoes[linha_atual][i]
        else:
            linha_atual = 1 - linha_atual  # Muda para a outra linha
            tempo_total += tempos_estacoes[linha_atual][i]

    tempo_total += tempo_saida  # Adiciona o tempo de saída

    return tempo_total


# Exemplo de uso
# tempos_estacoes = [[7, 9, 3], [8, 5, 6]]  # Tempos de montagem em cada estação
# tempos_transferencia = [[2, 3, 1], [2, 1, 2]]  # Tempos de transferência entre as estações
# tempo_entrada = 2  # Tempo de entrada na linha de montagem
# tempo_saida = 3  # Tempo de saída da linha de montagem

# tempo_total = linha_montagem(tempos_estacoes, tempos_transferencia, tempo_entrada, tempo_saida)
# print("Tempo total de montagem:", tempo_total)