
import pygame.draw
import pygame
import sys


pygame.init()


LARGURA = 1200
ALTURA = 700


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("trilha maluca") 

objeto_pos = [400, 300]

while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    janela.fill(PRETO)
    
    objeto_pos = list(pygame.mouse.get_pos())


    pygame.draw.rect(janela,AZUL,(1010,100,100,100))
    pygame.draw.rect(janela,VERMELHO,(980,100,100,100))
    pygame.draw.rect(janela,VERMELHO,(870,100,100,100))
    pygame.draw.rect(janela,BRANCO,(760,100,100,100))
    pygame.draw.rect(janela,BRANCO,(650,100,100,100))
    pygame.draw.rect(janela,VERMELHO,(540,100,100,100))
    pygame.draw.rect(janela,BRANCO,(430,100,100,100))
    pygame.draw.rect(janela,VERMELHO,(320,100,100,100))
    pygame.draw.rect(janela,BRANCO,(210,100,100,100))
   
    pygame.draw.rect(janela,VERMELHO,(100,100,100,100))
    pygame.draw.rect(janela,BRANCO,(100,210,100,100))
    pygame.draw.rect(janela,BRANCO,(100,320,100,100))
    pygame.draw.rect(janela,VERMELHO,(100,430,100,100))
    pygame.draw.rect(janela,BRANCO,(100,540,100,100))
 
 #posição dos meus objetos
    x1 = 120
    y1 = 650
    pygame.draw.circle(janela, AZUL,(x1,y1),20)
    
    x2 = 180
    y2 = 650
    pygame.draw.circle(janela, VERDE,(x2,y2),20)
   
    
    #janela com o questionario
    pygame.draw.rect( janela,BRANCO,(210,210,1100,900))
    
    
    pygame.display.update()