# Open world map - two surfaces

import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

done = False

# Colours
RED = (100, 0, 0)
BLUE = (0, 0, 100)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

food = []

# top surface
topDest = pygame.Rect(0, 0, WIDTH, HEIGHT)
topSurface = pygame.Surface((WIDTH, HEIGHT))
topSurface = topSurface.convert()
topSurface.fill(RED)

# bottom surface
bottomDest = pygame.Rect(0, 0, WIDTH, HEIGHT)
bottomSurface = pygame.Surface((WIDTH, HEIGHT))
bottomSurface = topSurface.convert()
bottomSurface.fill(BLUE)

class Food:
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour

    def addFood(food):
        food.append(Food(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(3, 10), WHITE))

    def drawFood(self):
        pygame.draw.circle(topSurface, self.colour, (self.x, self.y), self.r)


def main():
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(topSurface, topDest)
                screen.blit(bottomSurface, bottomDest)
                
                for i in range(0, 10):
                    Food.addFood(food)
                print(food)

                for i in range(len(food)):
                    Food.drawFood(food[i])

        pygame.display.flip()


main()