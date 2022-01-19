import pygame
import colorsys
import numpy as np

def generateColors(size = 5, mode = 'rgb'):
    randomColors = []
    for i in range(size):
        row = []
        for j in range(size):
            if mode == 'rgb':
                r = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                b = np.random.randint(0, 255)
                row.append(pygame.Color((r,g,b)))
            elif mode == 'hsv':
                h = np.random.randint(0, 360)
                s = np.random.randint(0, 100)
                v = np.random.randint(0, 100)
                color = pygame.Color((0,0,0))
                color.hsva = (h, s, v, 100)
                row.append(color)
            elif mode == 'hsl':
                h = np.random.randint(0, 360)
                s = np.random.randint(0, 100)
                v = np.random.randint(0, 100)
                color = pygame.Color((0,0,0))
                color.hsva = (h, s, v, 100)
                row.append(color)

        randomColors.append(row)
    return randomColors

if __name__ == '__main__':
    width, height = 500, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Random Color')

    size = 5
    mode = 'rgb'
    randomColors = generateColors(size, mode=mode)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                randomColors = generateColors(size, mode=mode)
        
        win.fill((255, 255, 255))
        squareSize = int((width - 50) / (size) - 10)
        for i in range(size):
            for j in range(size):
                pygame.draw.rect(win, randomColors[i][j], (30 + (squareSize + 10) * i, 30 + (squareSize + 10) * j, squareSize, squareSize), border_radius = 5)

        pygame.display.update()