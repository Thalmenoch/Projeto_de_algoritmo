import random
from arquivos.teste_guloso import linha_de_montagem_guloso
from arquivos.teste_iterativo import linha_de_montagem
from arquivos.grafico import grafico_da_entrada, grafico_da_saida

def comparacoes():
    estacoes = random.randint(1, 10) # foi diminuido para que o gráfico visualizável de maneira adequada

    tamanho = random.randint(1, 1000)
    num_execucoes = random.randint(1, 5) # foi diminuido para que o gráfico visualizável de maneira adequada

    # lista que vão ser inseridas no gráfico
    tamanho_entrada_guloso = []
    tamanho_entrada_iterativo = []

    tamanho_saida_guloso = []
    tamanho_saida_iterativo = []

    media_tempo_execucao_guloso = []
    media_tempo_execucao_iterativo = []

    for i in range(num_execucoes):
        tempos_execucao_guloso = []
        tempos_execucao_iterativo = []
        
        tempo = [[random.randint(1, 100) for rep in range(estacoes)] for r in range(2)]

        trocas = [[random.randint(1, 100) for rep in range(estacoes)] for r in range(2)]
        
        entrada1 = [random.randint(1, tamanho) for r in range(2)]
        tamanho_entrada_guloso.append(entrada1)
        
        entrada2 = [random.randint(1, tamanho) for r in range(2)]
        tamanho_entrada_iterativo.append(entrada2)
            
        saida1 = [random.randint(1,tamanho) for r in range(2)]
        tamanho_saida_guloso.append(saida1)

        saida2 = [random.randint(1,tamanho) for r in range(2)]
        tamanho_saida_iterativo.append(saida2)

        tempo_min_guloso, caminho_guloso = linha_de_montagem_guloso(tempo, trocas, entrada1, saida1)
        
        tempos_execucao_guloso.append(tempo_min_guloso)

        tempo_min_iterativo, caminho_otimo = linha_de_montagem(tempo, trocas, entrada2, saida2)
        
        tempos_execucao_iterativo.append(tempo_min_iterativo)

        print("Tempo mínimo de montagem (guloso):", tempo_min_guloso)
        print("Caminho encontrado (guloso):", caminho_guloso)
        print()
        print("Tempo mínimo de montagem (iterativo):", tempo_min_iterativo)
        print("Caminho encontrado (iterativo):", caminho_otimo)
        print()

        media_tempo_execucao_guloso.append(sum(tempos_execucao_guloso) / len(tempos_execucao_guloso))
        media_tempo_execucao_iterativo.append(sum(tempos_execucao_iterativo) / len(tempos_execucao_iterativo))

    media_guloso = sum(media_tempo_execucao_guloso) / len(media_tempo_execucao_guloso)
    media_iterativo = sum(media_tempo_execucao_iterativo) / len(media_tempo_execucao_iterativo)

    # print(media_tempo_execucao_guloso)
    # print(media_tempo_execucao_iterativo)
    # print(tamanho_entrada_guloso)
    # print(tamanho_entrada_iterativo)
    # print(tamanho_saida_guloso)
    # print(tamanho_saida_iterativo)

    print(f"Média do tempo de execução guloso {media_guloso:.2f} segundos")
    print(f"Média do tempo de execução iterativo {media_iterativo:.2f} segundos")
    dif = media_iterativo - media_guloso
    print(f'Diferença de tempo entre o iterativo e o guloso é em segundos: {dif:.2f}')

    gr_entrada = grafico_da_entrada(tamanho_entrada_guloso, tamanho_entrada_iterativo, media_tempo_execucao_guloso, media_tempo_execucao_iterativo)
    gr_saida = grafico_da_saida(tamanho_saida_guloso, tamanho_saida_iterativo, media_tempo_execucao_guloso, media_tempo_execucao_iterativo)
    print(gr_entrada)
    print(gr_saida)

