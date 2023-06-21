import time
from simul import simulation 
import random

# Além disso, seu c ́odigo deve criar, aleatoriamente e adequadamente, entra-
# das para o problema. Para cada tamanho de entrada n, vocˆe deve criar m entradas de

# tamanho n e fazer uma m ́edia do tempo de execu ̧c ̃ao para entrada de tamanho n. Vocˆe

# deve comparar os algoritmos de forma justa, ent ̃ao vocˆe deve criar os tamanhos de en-
# trada e as entradas para executar os algoritmos levando isso em considera ̧c ̃ao.

# criar um rand entre um intervalo considerável pode ser uma boa ideia

rand_tamanho = random.randint(2, 10)
aux_tamanhos = rand_tamanho

tamanhos = []

for aux in range(aux_tamanhos):
    tamanhos.append(random.randint(1, 10000))

rand_num_execucoes = random.randint(1, 10)
num_execucoes = rand_num_execucoes

for tamanho in tamanhos:
    tempos_execucao = []
    for i in range(num_execucoes):
        entrada = [random.randint(1, 100) for i in range(tamanho)]  # Cria uma entrada de tamanho n com valores aleatórios
        
        inicio = time.time()
        simulation(entrada)  
        fim = time.time()
        
        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)
    
    media_tempo_execucao = sum(tempos_execucao) / len(tempos_execucao)
    print(f"Média do tempo de execução para tamanho {tamanho}: {media_tempo_execucao} segundos")
