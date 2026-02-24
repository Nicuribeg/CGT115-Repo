import pygame
import math
pygame.init()

screen = pygame.display.set_mode((800,600))

rect = pygame.Rect(325,250,125,50)
pygame.draw.rect(screen,(255,255,255),rect)

circle1 = pygame.draw.circle(screen,(255,255,255),(357,315),15)
circle2 = pygame.draw.circle(screen,(255,255,255),(417,315),15)

pygame.draw.arc(screen,(255,255,255),(342,225,90,50),0,math.pi)

pygame.display.update()

done = False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()