import time
from simul import simulation 

tamanhos = [10, 100, 1000]  
num_execucoes = 5  

for tamanho in tamanhos:
    tempos_execucao = []
    for _ in range(num_execucoes):
        entrada = [1] * tamanho  
        
        inicio = time.time()
        simulation(entrada)  
        fim = time.time()
        
        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)
    
    media_tempo_execucao = sum(tempos_execucao) / len(tempos_execucao)
    print(f"Média do tempo de execução para tamanho {tamanho}: {media_tempo_execucao} segundos")
