import pygame
import random

# VARIABLES TO TWEAK
screenw, screenh = (1156, 1000)
A = [578, 0]
B = [1155, 999]
C = [1, 999]


screen = pygame.display.set_mode((screenw, screenh))

points = [A, B, C]

pygame.draw.rect(screen, (255, 255, 255), (578, 0, 1, 1)) #A
pygame.draw.rect(screen, (255, 255, 255), (1155, 999, 1, 1)) #B
pygame.draw.rect(screen, (255, 255, 255), (1, 999, 1, 1)) #C
CurrentPoint = A
pygame.display.update()



Update = True
while Update is True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Update = False



    DestenationPoint = random.choice(points)

    CurrentPoint = [CurrentPoint[0] + round((DestenationPoint[0] - CurrentPoint[0])/2), CurrentPoint[1] + round((DestenationPoint[1] - CurrentPoint[1])/2)]

    rect = (CurrentPoint[0], CurrentPoint[1], 1, 1)

    pygame.draw.rect(screen, (255, 255, 255), (CurrentPoint[0], CurrentPoint[1], 1, 1))
    pygame.display.update()