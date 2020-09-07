import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption(" PUBG ")

icon = pygame.image.load(os.path.join(".","PUBG\Images\pubg.png"))
pygame.display.set_icon(icon)

hand_shoot = pygame.image.load(os.path.join(".","PUBG\Images\shoot.png"))
shootx = 350
shooty = 470
shoot_change = 0

def shooter(x, y):
    screen.blit(hand_shoot,(x, y))

running = True
while running:
    screen.fill((0, 75, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shoot_change = -0.3
            if event.key == pygame.K_RIGHT:
                shoot_change = 0.3
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shoot_change = 0              

    shootx += shoot_change              

    # if(shootx > 0 and shootx < 747):
    #     shooter(shootx, shooty)
    # else: 
    #     if shootx <= 0:
    #         shooter(0,shooty)
    #         shootx = 0
    #     else:
    #         shooter(746,shooty)
    #         shootx = 746

    if shootx <= 0:
        shootx = 0
    elif shootx >= 736:
        shootx = 736

    shooter(shootx, shooty)  

    pygame.display.update()