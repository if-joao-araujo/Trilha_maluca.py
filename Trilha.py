from random import choice, randint
from time import sleep

print("Bem-vindo à Trilha Maluca!\n")

# Configurações do jogo
posicao_jogador1 = 0
posicao_jogador2 = 0
passo = "Passo -->"
regresso = "Regresso <--"
caminho_tamanho = 16
armadilhas = [2,5,7,9,13]

# Banco de perguntas e respostas
questionamentos = {
    "questionamento1": {
        "pergunta": "print(2 + 3 * 4):",
        "opcoes": ["a) 20", "b) 14", "c) 24", "d) Erro"],
        "resposta": "b"
    },
    "questionamento2": {
        "pergunta": "Python é baseado em qual linguagem de programação?",
        "opcoes": ["a) Java", "b) C", "c) Assembly", "d) Ruby"],
        "resposta": "b"
    },
    "questionamento3": {
        "pergunta": "Qual sistema numérico o computador reconhece?",
        "opcoes": ["a) Decimal", "b) Binário", "c) Hexadecimal", "d) Octal"],
        "resposta": "b"
    },
    "questionamento4": {
        "pergunta": "Na operação lógica OR: 1 e 0 = ?",
        "opcoes": ["a) 0", "b) 1", "c) 10", "d) Nenhuma das anteriores"],
        "resposta": "b"
    },
    "questionamento5": {
        "pergunta": "Em qual ano o Python foi criado?",
        "opcoes": ["a) 1989", "b) 1995", "c) 2000", "d) 1991"],
        "resposta": "d"
    },
    "questionamento6": {
        "pergunta": "Python é uma linguagem...",
        "opcoes": ["a) Compilada", "b) Interpretada", "c) Híbrida", "d) Nenhuma das anteriores"],
        "resposta": "b"
    },
    "questionamento7": {
        "pergunta": "Qual biblioteca é usada na criação de jogos em Python?",
        "opcoes": ["a) Pandas", "b) Pygame", "c) TensorFlow", "d) Django"],
        "resposta": "b"
    }
}

def fazer_pergunta(jogador):
    questao = choice(list(questionamentos.values()))
    print(f"\nJogador {jogador}: {questao['pergunta']}")
    for opcao in questao['opcoes']:
        print(opcao)
    
    resposta = input("Sua resposta (a/b/c/d): ").lower()
    return resposta == questao['resposta']

while True:
    # Jogador 1
    print("\nVez do Jogador 1:")
    if fazer_pergunta(1):
        print("Resposta correta! Jogando o dado...")
        sleep(1)
        dado = randint(1, 6)
        print(f"Você jogou o dado e o número sorteado foi {dado}!")
        
        for _ in range(dado):
            print(passo)
            sleep(1)
            posicao_jogador1 += 1
        for pos1 in armadilhas:   
            if posicao_jogador1 == pos1:
               print(f"Armadilha na posição {posicao_jogador1}! Voltando 1 casa.")
               print(regresso)
               posicao_jogador1 -= 1
               sleep(1)
    else:
        print("Resposta errada! Perdeu a vez.")

 

    print(f"Posição atual do Jogador 1: {posicao_jogador1}\n")
    print("="*20)
    sleep(1)
    # Jogador 2
    print("\nVez do Jogador 2:")
    if fazer_pergunta(2):
        print("Resposta correta! Jogando o dado...")
        sleep(1)
        dado = randint(1, 6)
        print(f"Jogador 2 jogou o dado e o número sorteado foi {dado}!")
        
        for _ in range(dado):
            print(passo)
            sleep(1)
            posicao_jogador2 += 1
        for pos2 in armadilhas: 
            if posicao_jogador2 == pos2:
               print(f"Armadilha na posição {posicao_jogador1}! Voltando 1 casa.")
               print(regresso)
               posicao_jogador1 -= 1
               sleep(1)        
    else:
        print("Resposta errada! Perdeu a vez.")
        print("="*20)
    sleep(1)
    print(f"Posição atual do Jogador 2: {posicao_jogador2}\n")
    print("="*20)
    sleep(1)
 
    # Verificação de vitória Jogador 1
    if posicao_jogador1 >= caminho_tamanho:
        print("Jogador 1 venceu!")
        break
    # Verificação de vitória Jogador 2
    if posicao_jogador2 >= caminho_tamanho:
        print("Jogador 2 venceu!")
        break
    
    # Verificação de empate
    if posicao_jogador1 >= caminho_tamanho and posicao_jogador2 >= caminho_tamanho:
        print("Empate! Ambos chegaram ao final.")
        break

    print("Próxima rodada em 3 segundos...")
    sleep(3)