from math import ceil
import cielab
import pygame

if __name__ == '__main__':
    screen_size = 500
    win = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption('Evenly Spaced Colors')

    colors = cielab.get_grid_colors(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        win.fill((255, 255, 255))

        grid_size = ceil(len(colors)**(1/2))
        square_size = int((screen_size - 50) / (grid_size) - 10)
        
        for i in range(grid_size):
            for j in range(grid_size):
                if i + grid_size*j < len(colors):
                    color = colors[i + grid_size*j]
                    pygame.draw.rect(win, color, (30 + (square_size + 10) * i, 30 + (square_size + 10) * j, square_size, square_size), border_radius = 5)

        pygame.display.update()