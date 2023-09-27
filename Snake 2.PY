import pygame
import sys 
from random import randint

#Cuando se ejecute una accion que cause el final del juego
def gameover():
    # Dibujar la imagen en la ventana
    ventana.blit(tablerogameover, (0,0))
    pygame.display.flip() #funciona igual que el .update()
    pygame.time.delay(2000)
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

#Creacion ventana
ancho = 650
alto = 650
ventana = pygame.display.set_mode((ancho, alto))
#color_azul = (255,0,0)
color_azul = (255,153,204)
#color_azul = (12,103,232)

# Colocarle titulo a la ventana:
pygame.display.set_caption("EDDSnake")

#Imagenes:
manzana = pygame.image.load("Manzana.png")
cabezaarriba = pygame.image.load("cabeza.png")
cabezaabajo = pygame.image.load("cabeza_abj.png")
cabezadrc = pygame.image.load("cabeza_drc.png")
cabezaizq = pygame.image.load("cabeza_izq.png")
fondo = pygame.image.load("TABLERO2.0.png")
tablerogameover = pygame.image.load("FONDOgameover.png")
cabeza = cabezaarriba

#cuerpo cuerpo cabeza (cabeza es siempre el [-1])
cuerpo = [[300,400],[300,350],[300,300]]
direccion = [0,-50]  


clock = pygame.time.Clock() 
speed = 11

posicionarManzana()

movimientos = 0
aparecemanzana = True
salirmanzana = None

while True: 
                    
    for evento in pygame.event.get():
        # Si se cierra el juego con la x, terminar el juego
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
            
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
            

    #Creacion de ventana

    ventana.blit(fondo,(0, 0))
    #Dibuja manzana
    if aparecemanzana:
        ventana.blit(manzana,manzanacoor)
    
    #MOVIMIENTO SERPIENTES
    cuerpo.append([cuerpo[-1][0] + direccion[0], cuerpo[-1][1] + direccion[1]])
    cuerpo.pop(0)

    # Dibuja el cuerpo con rectangulos con las coordenadas de la lista cuerpo
    for i in range(len(cuerpo)-1):
        pygame.draw.rect(ventana,color_azul,(cuerpo[i][0], cuerpo[i][1],50,50)) 

    # Pone imagen de la caebza en la ventana, en las coordenadas del ultimo
    ventana.blit(cabeza,cuerpo[-1])


    #Si no se come manzana en 10 movimientos se cambia de lugar
    '''if movimientos == 10:
        posicionarManzana()
        aparecemanzana = True
        movimientos=0'''


    #Comer la manzana
    if cuerpo[-1] == manzanacoor:     
        cuerpo.insert(0,[cuerpo[0][0] - direccion[0],cuerpo[0][1] - direccion[1]])
        if speed < 12.6:
            speed += 0.2
        posicionarManzana()
        salirmanzana = randint(0,10)
        aparecemanzana = False
        movimientos=0
    

    if movimientos == salirmanzana:
        movimientos=0
        aparecemanzana = True
    elif movimientos == 10:
        posicionarManzana()
        aparecemanzana = True
        movimientos=0
        
    #Colisiones
    if cuerpo[-1][0] < 0 or cuerpo[-1][0] >= ancho:
        gameover()
        
    if cuerpo[-1][1] < 0 or cuerpo[-1][1] >= alto:
        gameover()

    #Colision contra el cuerpo
    for parte in cuerpo[:-1]:
        if parte == cuerpo[-1]:
            gameover()

    # Se actualiza la imagen de la ventana
    pygame.display.flip()
    clock.tick(speed)
