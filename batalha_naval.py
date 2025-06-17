import random

# Tamanho do tabuleiro
TAMANHO = 5
NUM_NAVIOS = 3
TENTATIVAS = 10

# Cria o tabuleiro visível e oculta onde estão os navios
tabuleiro = [['~' for _ in range(TAMANHO)] for _ in range(TAMANHO)]
navios = []

# Gera posições únicas para os navios
while len(navios) < NUM_NAVIOS:
    linha = random.randint(0, TAMANHO - 1)
    coluna = random.randint(0, TAMANHO - 1)
    if (linha, coluna) not in navios:
        navios.append((linha, coluna))

def exibir_tabuleiro():
    print("\n  " + " ".join([str(i) for i in range(TAMANHO)]))
    for i, linha in enumerate(tabuleiro):
        print(f"{i} " + " ".join(linha))

def jogar():
    acertos = 0
    tentativas_restantes = TENTATIVAS

    print("🚢 Bem-vindo à Batalha Naval!")
    print(f"Você tem {TENTATIVAS} tentativas para encontrar {NUM_NAVIOS} navios.")
    
    while tentativas_restantes > 0 and acertos < NUM_NAVIOS:
        exibir_tabuleiro()
        try:
            linha = int(input("Digite a linha (0 a 4): "))
            coluna = int(input("Digite a coluna (0 a 4): "))
        except ValueError:
            print("⚠️ Entrada inválida. Digite números inteiros entre 0 e 4.")
            continue

        if not (0 <= linha < TAMANHO and 0 <= coluna < TAMANHO):
            print("⚠️ Fora dos limites do tabuleiro!")
            continue

        if tabuleiro[linha][coluna] != '~':
            print("⛔ Você já jogou nessa posição!")
            continue

        if (linha, coluna) in navios:
            print("💥 Acertou um navio!")
            tabuleiro[linha][coluna] = 'X'
            acertos += 1
        else:
            print("🌊 Água...")
            tabuleiro[linha][coluna] = 'O'

        tentativas_restantes -= 1
        print(f"🎯 Tentativas restantes: {tentativas_restantes}")

    exibir_tabuleiro()
    if acertos == NUM_NAVIOS:
        print("🏆 Parabéns! Você afundou todos os navios!")
    else:
        print("💀 Fim de jogo! Você não encontrou todos os navios.")
        print(f"Os navios estavam em: {navios}")

# Inicia o jogo
jogar()
