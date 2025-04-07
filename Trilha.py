from random import randint
from time import sleep

print("Bem-vindo à Trilha Maluca!\n")

# Jogadores
posicao_jogador1 = 0
posicao_jogador2 = 0

passo = "Passo -->"
regresso = "Regresso <--"

caminho_tamanho = 17
armadilhas = [3, 6, 9, 12, 15]

loop = True
while loop == True:
    sortear = str(input("deseja sortear o dado? [s] [n]: ")).lower()
    if sortear == "s":
        print("sorteando dado...")
        sleep(1)
        loop = False
    elif sortear == "n":
        print("Não seja chato!!, digite sim[s]")
    else:
        print("digite [s] ou [n]")

    while loop == False:
        # Jogador 1
        dado = randint(1, 6)
        print(f"O jogador 1 jogou o dado e o número sorteado foi {dado}!")
        print(f"Você se deslocou {dado} casas \n")
    
        for deslocamento1 in range(dado):
            print(passo)
            sleep(1.5)
            posicao_jogador1 += 1
    
        if posicao_jogador1 in armadilhas:
           print(f"o jogador1 está na posição {posicao_jogador1}  e será punido!")
           print(regresso)
           sleep(1.5)
           posicao_jogador1 -= 1
        print(f" sua posição atual é {posicao_jogador1} \n" )
        print("=|="*10)
       
        # Jogador 2
        dado2 = randint(1, 6)
        print(f"O jogador 2 jogou o dado e o número sorteado foi {dado2}\n")
        print(f"O jogador 2 se deslocou {dado2} posições.")
        for deslocamento2 in range(dado2):
            print(passo)
            sleep(1.5)
            posicao_jogador2 += 1
    
        if posicao_jogador2 in armadilhas:
           print(f"o jogador2 está na posição {posicao_jogador2}  e será punido!")
           print(regresso)
           posicao_jogador2 -= 1
        print(f"a posição do jogador 2 atual é {posicao_jogador2} \n")
        print("=|="*10)
        # Condições de vitória
        if posicao_jogador1 > caminho_tamanho:
            print("Você ganhou!")
            sleep(2)
            break
    
        elif posicao_jogador2 > caminho_tamanho:
            print("A máquina venceu!")
            sleep(2)
            break
        elif posicao_jogador1 and posicao_jogador2  > caminho_tamanho:
             print("Aconteceu um empate, ambos jogadores passaram da linha de chegada")
        else:
            print("vamos para a proxima rodade!\n")
            print(f"a posição atual do jogador 1 é {posicao_jogador1}\n posição atual do jogador 2 é {posicao_jogador2}\n ")
            sleep(0.5)
            print("......")
            sleep(0.5)
            loop = True
    
