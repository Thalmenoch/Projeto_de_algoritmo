import random
import time
import matplotlib.pyplot as plt
from teste_guloso import linha_de_montagem_guloso
from teste_iterativo import linha_de_montagem

def gerar_entrada_aleatoria(n):
    # Gerar tempos de montagem aleatórios
    tempos = [[random.randint(1, 10) for _ in range(n)] for _ in range(2)]

    # Gerar tempos de troca aleatórios
    trocas = [[random.randint(1, 5) for _ in range(n-1)] for _ in range(2)]

    # Gerar entradas e saídas aleatórias
    entrada = [random.randint(1, 10) for _ in range(2)]
    saida = [random.randint(1, 10) for _ in range(2)]

    return tempos, trocas, entrada, saida

# Definir tamanhos de entrada
tamanhos = [10, 20, 30, 40, 50]

# Definir quantidade de entradas aleatórias
m = 5

tempos_guloso = []
tempos_iterativo = []

# Gerar e avaliar entradas aleatórias
for n in tamanhos:
    tempos_totais_guloso = 0
    tempos_totais_iterativo = 0

    for _ in range(m):
        # Gerar entrada aleatória
        tempos, trocas, entrada, saida = gerar_entrada_aleatoria(n)

        # Executar algoritmo guloso
        inicio = time.time()
        _, _ = linha_de_montagem_guloso(tempos, trocas, entrada, saida)
        fim = time.time()
        tempo_guloso = fim - inicio
        tempos_totais_guloso += tempo_guloso

        # Executar algoritmo iterativo
        inicio = time.time()
        _, _ = linha_de_montagem(tempos, trocas, entrada, saida)
        fim = time.time()
        tempo_iterativo = fim - inicio
        tempos_totais_iterativo += tempo_iterativo

    # Calcular médias dos tempos de execução
    media_guloso = tempos_totais_guloso / m
    media_iterativo = tempos_totais_iterativo / m

    tempos_guloso.append(media_guloso)
    tempos_iterativo.append(media_iterativo)

# Plotar gráfico
plt.plot(tamanhos, tempos_guloso, label="Guloso")
plt.plot(tamanhos, tempos_iterativo, label="Iterativo")
plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo de execução (s)")
plt.title("Comparação de tempo de execução")
plt.legend()
plt.show()
