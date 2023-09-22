import pygame
import sys
from random import randint

# Comando necesario antes de usar cualquier metodo de pygame
pygame.init()

# Como abrir una venntana: (anchura, altura)px
ancho = 650
alto = 650
ventana = pygame.display.set_mode((ancho, alto))

# Colocarle titulo a la ventana:
pygame.display.set_caption("Ventana de pruebas")

# Una ventana de pygame se comporta como una matriz, asi q se pueden
# usar las coordenadas para viajar por ellas.

# Sirve para los valores iniciales del juego:

# Para dibujar algo, se usa: ventana, color, coordenadasInicio, coordenadasFinal
# ancho
color_salmon = (237, 111, 102)
color_x = (12,103,232)
pygame.draw.line(ventana, color_salmon, (0,80), (80,0), 10)

# Para dibujar cualquier figura geometrica:
# Circulo
#pygame.draw.circle(ventana, color_x, (325, 150), 30)
manzana = pygame.image.load("Manzana.png")
cabezaarriba = pygame.image.load("cabeza.png")
cabezaabajo = pygame.image.load("cabeza_abj.png")
cabezadrc = pygame.image.load("cabeza_drc.png")
cabezaizq = pygame.image.load("cabeza_izq.png")
fondo = pygame.image.load("TABLER SNAKE.png")
cuerpo = pygame.image.load("cuerpo.png")
gameover = pygame.image.load("Gam.png")

cabeza = cabezaarriba

cuerpo = [[200,300],[250,300],[300,300]]
direccion = [0,-50]

actualizacionpantalla = pygame.USEREVENT
pygame.time.set_timer(actualizacionpantalla,120)
clock = pygame.time.Clock()
mx,my = 550,150
manzanacoor = [mx,my]

while True:
    
    for evento in pygame.event.get():
        # Si se cierra el juego con la x, terminar el juego
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        if evento.type == actualizacionpantalla:
            cuerpo.append([cuerpo[-1][0] + direccion[0], cuerpo[-1][1] + direccion[1]])
            cuerpo.pop(0)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion[1] != 50:
                direccion = [0,-50]
                cabeza = cabezaarriba
            if evento.key == pygame.K_DOWN and direccion[1] != -50:
                direccion = [0,50]
                cabeza = cabezaabajo
            if evento.key == pygame.K_LEFT and direccion[0] != 50:
                direccion = [-50,0]
                cabeza = cabezaizq
            if evento.key == pygame.K_RIGHT and direccion[0] != -50:
                direccion = [50,0]
                cabeza = cabezadrc
            
            
    # Rectangulo/cuadrado
    ventana.blit(fondo,(0, 0))
    ventana.blit(manzana,manzanacoor)    

    if cuerpo[-1] == manzanacoor:
        cuerpo.append([cuerpo[-1][0] + direccion[0],cuerpo[-1][1] + direccion[1]])
        while True:
            mx = randint(0,12) * 50
            my = randint(0,12) * 50
            if [mx,my] not in cuerpo:
                manzanacoor = [mx,my]
                break

    for i in range(len(cuerpo)):
        pygame.draw.rect(ventana,color_x,(cuerpo[i][0], cuerpo[i][1],50,50)) 

    ventana.blit(cabeza,cuerpo[-1])
    
    if cuerpo[-1][0] < 0 or cuerpo[-1][0] >= 650:
        ventana.blit(gameover,(alto//2,ancho//2))
        pygame.display.flip()
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()
    if cuerpo[-1][1] < 0 or cuerpo[-1][1] >= 650:
        ventana.blit(gameover,(alto//2,ancho//2))
        pygame.display.flip()
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    for parte in cuerpo[:-1]:
        if parte == cuerpo[-1]:
            ventana.blit(gameover,(alto//2,ancho//2))
            pygame.display.flip()
            pygame.time.delay(1000)
            pygame.quit()
            sys.exit()
    # Se actualiza la imagen de la ventana
    pygame.display.flip()
    clock.tick(60)