import pygame
import sys
from random import randint

#Cuando se ejecute una accion que cause el final del juego
def gameover():
    rectangulo_avisogameover = avisogameover.get_rect()

    # Centrar el rectángulo en la ventana
    rectangulo_avisogameover.center = (ancho // 2, alto // 2)

    # Dibujar la imagen en la ventana
    ventana.blit(avisogameover, rectangulo_avisogameover)
    pygame.display.flip()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()


#Posiciona la manzana en una coordenada aleatoria, diferente a la posicion del snake
def posicionarManzana():
    while True:
        global mx,my, manzanacoor
    
        mx = randint(0,12) * 50
        my = randint(0,12) * 50
        if [mx,my] not in cuerpo:
            manzanacoor = [mx,my]
            break


# Comando necesario antes de usar cualquier metodo de pygame
pygame.init()

# Como abrir una venntana: (anchura, altura)px
ancho = 650
alto = 650
ventana = pygame.display.set_mode((ancho, alto))

# Colocarle titulo a la ventana:
pygame.display.set_caption("EDDSnake")


color_azul = (12,103,232)


#Imagenes:
manzana = pygame.image.load("Manzana.png")
cabezaarriba = pygame.image.load("cabeza.png")
cabezaabajo = pygame.image.load("cabeza_abj.png")
cabezadrc = pygame.image.load("cabeza_drc.png")
cabezaizq = pygame.image.load("cabeza_izq.png")
fondo = pygame.image.load("TABLER SNAKE.png")
#cuerpo = pygame.image.load("cuerpo.png")
avisogameover = pygame.image.load("Gam.png")

cabeza = cabezaarriba

cuerpo = [[200,300],[250,300],[300,300]]
direccion = [0,-50]  

actualizacionpantalla = pygame.USEREVENT
velocidad = 110
pygame.time.set_timer(actualizacionpantalla,velocidad)
clock = pygame.time.Clock()  

posicionarManzana()

movimientos = 0

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
            movimientos += 1
            #Para cuando se mueve la flecha hacia arriba o w
            if evento.key == pygame.K_UP and direccion[1] != 50:
                direccion = [0,-50]
    
                cabeza = cabezaarriba
            if evento.key == pygame.K_w and direccion[1] != 50:
                direccion = [0,-50]
                cabeza = cabezaarriba
            #Para cuando se mueve la flecha hacia abajo o s
            if evento.key == pygame.K_DOWN and direccion[1] != -50:
                direccion = [0,50]
                cabeza = cabezaabajo
            if evento.key == pygame.K_s and direccion[1] != -50:
                direccion = [0,50]
                cabeza = cabezaabajo
            #Para cuando se mueve la flecha hacia la izquierda o a
            if evento.key == pygame.K_LEFT and direccion[0] != 50:
                direccion = [-50,0]
                cabeza = cabezaizq
            if evento.key == pygame.K_a and direccion[0] != 50:
                direccion = [-50,0]
                cabeza = cabezaizq
            #Para cuando se mueve la flecha hacia la derecha o d
            if evento.key == pygame.K_RIGHT and direccion[0] != -50:
                direccion = [50,0]
                cabeza = cabezadrc
            if evento.key == pygame.K_d and direccion[0] != -50:
                direccion = [50,0]
                cabeza = cabezadrc
            

    # Rectangulo/cuadrado
    ventana.blit(fondo,(0, 0))
    ventana.blit(manzana,manzanacoor)

    if movimientos == 10:
        posicionarManzana()
        movimientos=0
        
    if cuerpo[-1] == manzanacoor:     
        cuerpo.append([cuerpo[-1][0] + direccion[0],cuerpo[-1][1] + direccion[1]])
        velocidad -= 8
        velocidad -= 5
        pygame.time.set_timer(actualizacionpantalla,velocidad)
        posicionarManzana()
        movimientos=0
        
        
    # Dibuja el cuerpo con rectangulos con las coordenadas de la lista cuerpo
    for i in range(len(cuerpo)-1):
        pygame.draw.rect(ventana,color_azul,(cuerpo[i][0], cuerpo[i][1],50,50)) 

    # Pone imagen de la caebza en la ventana, en las coordenadas del ultimo
    ventana.blit(cabeza,cuerpo[-1])
    
    if cuerpo[-1][0] < 0 or cuerpo[-1][0] >= 650:
        gameover()
        
    if cuerpo[-1][1] < 0 or cuerpo[-1][1] >= 650:
        gameover()

    for parte in cuerpo[:-1]:
        if parte == cuerpo[-1]:
            gameover()
            
    # Se actualiza la imagen de la ventana
    pygame.display.flip()
    clock.tick(60)