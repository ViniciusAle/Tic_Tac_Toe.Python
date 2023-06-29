import numpy as np
import tkinter as tk

# Funções de verificação
def verificar_vitoria(matriz):
    # Verificador das linhas
    for i in range(3):
        if matriz[i, 0] == matriz[i, 1] == matriz[i, 2] != "":
            return matriz[i, 0]
    # Verificador das colunas
    for j in range(3):
        if matriz[0, j] == matriz[1, j] == matriz[2, j] != "":
            return matriz[0, j]
    # Verificador das diagonais
    if matriz[0, 0] == matriz[1, 1] == matriz[2, 2] != "":
        return matriz[0, 0]
    elif matriz[0, 2] == matriz[1, 1] == matriz[2, 0] != "":
        return matriz[0, 2]
    # Empate
    return ""

# Atualizar a matriz/tabuleiro
def atualizar_matriz(i, j):
    global jogador_atual, matriz, botoes, pontos_x, pontos_o, empates
# Posicionamento do jogador na matriz
    if matriz[i, j] == "":
        matriz[i, j] = jogador_atual
        botoes[i][j].config(text=jogador_atual, state=tk.DISABLED)
# Utilizar a função de verificarção e  atribuir a pontuação
        vencedor = verificar_vitoria(matriz)
        if vencedor != "":
            if vencedor == "X":
                pontos_x += 1
            else:
                pontos_o += 1
            reiniciar()
        elif np.count_nonzero(matriz) == 9:
            empates += 1
            reiniciar()
# Alternar os jogadores
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

# Reiniciar o jogo
def reiniciar():
    global jogador_atual, matriz, botoes
    jogador_atual = "O" if jogador_atual == "X" else "X"
    matriz = np.empty((3, 3), dtype=str)
    matriz.fill("")
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text='', state=tk.NORMAL)
    atualizar_pontos()

# Exibir os pontos
def atualizar_pontos():
    pontos_label.config(text=f"X: {pontos_x}    O: {pontos_o}    Empates: {empates}")

# Exibição do Tkinter
root = tk.Tk()
root.title("Jogo da Velha")

jogador_atual = "X"
matriz = np.empty((3, 3), dtype=str)
matriz.fill("")
botoes = []

pontos_x = 0
pontos_o = 0
empates = 0

for i in range(3):
    linha = []
    for j in range(3):
        botao = tk.Button(root, width=20, height=10, command=lambda x=i, y=j: atualizar_matriz(x, y))
        botao.grid(row=i, column=j)
        linha.append(botao)
    botoes.append(linha)
#Botao de reinicia teste/lembra de remover/ou deixar sei la e legal 
reiniciar_button = tk.Button(root, text="Reiniciar", command=reiniciar)
reiniciar_button.grid(row=3, column=0, columnspan=3)

pontos_label = tk.Label(root, text="X: 0    O: 0    Empates: 0")
pontos_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
