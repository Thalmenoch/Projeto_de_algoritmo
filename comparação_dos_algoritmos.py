import random
from teste_guloso import linha_de_montagem_guloso
from teste_iterativo import linha_de_montagem

# Além disso, seu c ́odigo deve criar, aleatoriamente e adequadamente, entra-
# das para o problema. Para cada tamanho de entrada n, vocˆe deve criar m entradas de

# tamanho n e fazer uma m ́edia do tempo de execu ̧c ̃ao para entrada de tamanho n. Vocˆe

# deve comparar os algoritmos de forma justa, ent ̃ao vocˆe deve criar os tamanhos de en-
# trada e as entradas para executar os algoritmos levando isso em considera ̧c ̃ao.

# criar um rand entre um intervalo considerável pode ser uma boa ideia

repeticoes = random.randint(1, 10)


num_execucoes = [random.randint(1, 10) for r in range(3)]
print()

media_tempo_execucao_guloso = []
media_tempo_execucao_iterativo = []

for execs in num_execucoes:
    tempos_execucao_guloso = []
    tempos_execucao_iterativo = []
    
    tempo = [[random.randint(1, 1000) for rep in range(repeticoes)] for r in range(2)]

    trocas = [[random.randint(1, 1000) for rep in range(repeticoes)] for r in range(2)]
        
    entrada = [random.randint(1,100) for r in range(2)]
    
    saida = [random.randint(1,100) for r in range(2)]

    for repeticoes in range(execs):

        tempo_min_guloso, caminho_guloso = linha_de_montagem_guloso(tempo, trocas, entrada, saida)
        
        tempos_execucao_guloso.append(tempo_min_guloso)

        tempo_min_iterativo, caminho_otimo = linha_de_montagem(tempo, trocas, entrada, saida)
        
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

print(f"Média do tempo de execução {media_guloso:.2f} segundos")
print(f"Média do tempo de execução {media_iterativo:.2f} segundos")
