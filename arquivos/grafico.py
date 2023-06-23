import matplotlib.pyplot as plt

def grafico_da_entrada(tamanho_entrada_guloso, tamanho_entrada_iterativo, tempo_exec_guloso, tempo_exec_iterativo):
    
    x_guloso = [max(elemento) for elemento in tamanho_entrada_guloso]
    x_iterativo = [max(elemento) for elemento in tamanho_entrada_iterativo]
  
    plt.plot(x_guloso, tempo_exec_guloso, 'bo-', label='Tempo de Execução do Guloso')
    plt.plot(x_iterativo, tempo_exec_iterativo, 'ro-', label='Tempo de Execução do Iterativo')

    plt.xlabel('Tamanho n(x)')
    plt.ylabel('Tempo de Execução (y)')
    plt.title('Gráfico de Tamanho da Entrada')

    plt.legend()

    return plt.show()

def grafico_da_saida(tamanho_saida_guloso, tamanho_saida_iterativo, tempo_exec_guloso, tempo_exec_iterativo):

    x_guloso = [min(elemento) for elemento in tamanho_saida_guloso]
    x_iterativo = [min(elemento) for elemento in tamanho_saida_iterativo]
  
    plt.plot(x_guloso, tempo_exec_guloso, 'bo-', label='Tempo de Execução do Guloso')
    plt.plot(x_iterativo, tempo_exec_iterativo, 'ro-', label='Tempo de Execução do Iterativo')

    plt.xlabel('Tamanho n(x)')
    plt.ylabel('Tempo de Execução (y)')
    plt.title('Gráfico de Tamanho da Saida')

    plt.legend()

    return plt.show()

# if __name__ == '__main__':
#     tamanho1 = [[70, 109], [11, 94], [397, 853], [745, 290]]  
#     tamanho2 = [[218, 286], [43, 295], [588, 426], [167, 392]]
#     tempo_guloso = [3611.0, 3849.0, 4342.0, 4140.0]
#     tempo_iterativo = [3599.0, 4184.0, 4337.0, 4164.0]

#     gr1 = grafico_da_entrada(tamanho1, tamanho2, tempo_guloso, tempo_iterativo)
#     gr2 = grafico_da_saida(tamanho1, tamanho2, tempo_guloso, tempo_iterativo)

#     print(gr1)
#     print(gr2)