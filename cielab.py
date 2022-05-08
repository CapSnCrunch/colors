from matplotlib.pyplot import draw, grid
import pygame
import numpy as np
from colormath.color_objects import LabColor, sRGBColor, AdobeRGBColor
from colormath.color_conversions import convert_color

pygame.font.init()
font = pygame.font.SysFont('Roboto', 20)

N = 7
grid_node_radius = 3

sin, cos = np.sin, np.cos
theta = 0

def get_rgb_from_lab(L, a, b):
    lab = LabColor(L, a, b, observer='2', illuminant='d50')
    rgb = convert_color(lab, sRGBColor, target_illuminant='d50')
    rgb = rgb.get_upscaled_value_tuple()
    if rgb[0] < 1 or rgb[0] > 255 or rgb[1] < 1 or rgb[1] > 255 or rgb[2] < 1 or rgb[2] > 255:
        return None
    return rgb

def get_grid_colors(n = 7, transform = np.eye(3)):
    gridL = np.linspace(-128, 127, n)
    gridA = np.linspace(-128, 127, n)
    gridB = np.linspace(-128, 127, n)

    colors = []
    for L in gridL:
        for a in gridA:
            for b in gridB:
                rotated_L, rotated_a, rotated_b = transform @ np.array([L, a, b])
                color = get_rgb_from_lab(rotated_L, rotated_a, rotated_b)
                if color != None:
                    colors.append(color)
    return colors

def draw_layer(L, n = 30, transform = np.eye(3)):
    win.fill((214, 245, 174))

    a = np.linspace(-128, 127, n)
    b = np.linspace(-128, 127, n)

    # Draw the L layer color space
    for i in range(n):
        for j in range(n):
            color = get_rgb_from_lab(L, a[i], b[j])
            if color != None:
                pygame.draw.rect(win, color, (50 + i*(size-100)/n, size - 50 - j*(size-100)/n, (size-100)/n, (size-100)/n))
    
    # Draw the lattice points which intersect this layer
    gridL = np.linspace(-128, 127, N)
    gridA = np.linspace(-128, 127, N)
    gridB = np.linspace(-128, 127, N)

    LL, AA, BB = np.meshgrid(gridL, gridA, gridB, indexing='ij')

    indexLL = LL[np.where(abs(LL-L) < grid_node_radius)]
    indexAA = AA[np.where(abs(LL-L) < grid_node_radius)]
    indexBB = BB[np.where(abs(LL-L) < grid_node_radius)]

    for i in range(len(indexAA)):
        color = get_rgb_from_lab(L, indexAA[i], indexBB[i])
        if color != None:
            if L > 75:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)
            radius = (grid_node_radius**2 - abs(indexLL[i]-L)**2)**(1/2)
            diam = radius*2
            pygame.draw.ellipse(win, color, (50 + (indexAA[i]+128)/255 * (size-100) - diam/2, size - 50 - (indexBB[i]+128)/255 * (size-100) - diam/2, diam, diam), width=1)

    win.blit(font.render('L', False, (0, 0, 0)), (size/2, 10))
    win.blit(font.render('0', False, (0, 0, 0)), (50 + (size-100)*0.1 - 12, 24))
    win.blit(font.render('100', False, (0, 0, 0)), (size-75, 24))
    pygame.draw.rect(win, (0, 0, 0), (50+(size-100)*0.1, 29, 0.8*(size-100), 2))
    pygame.draw.rect(win, (0, 0, 0), (50+(size-100)*0.1, 27, 0.8*(size-100)*(L/100), 6))

    win.blit(font.render('a', False, (0, 0, 0)), (35, size-37))
    win.blit(font.render('-128', False, (0, 0, 0)), (50, size-20))
    win.blit(font.render('0', False, (0, 0, 0)), (size/2, size-20))
    win.blit(font.render('128', False, (0, 0, 0)), (size-70, size-20))
    pygame.draw.rect(win, (0, 0, 0), (30, 50, 2, size-100))

    win.blit(font.render('b', False, (0, 0, 0)), (27, 30))
    win.blit(font.render('-128', False, (0, 0, 0)), (2, 50))
    win.blit(font.render('0', False, (0, 0, 0)), (15, size/2))
    win.blit(font.render('128', False, (0, 0, 0)), (3, size-70))
    pygame.draw.rect(win, (0, 0, 0), (50, size-30, size-100, 2))

    pygame.display.update()

if __name__ == '__main__':
    size = 400
    win = pygame.display.set_mode((size, size))
    pygame.display.set_caption('CIE Lab')

    print(get_grid_colors(N))
    print(len(get_grid_colors(N)))

    scroll = 50
    draw_layer(scroll)

    # Save screenshots for gif
    # frames = np.linspace(0, 100, 150)
    # for i in range(len(frames)):
    #     draw_layer(frames[i])
    #     pygame.image.save(win, 'git/random-colors/gif3/frame' + str(i) + '.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: 
                    scroll = max(scroll - 1, 0)
                    draw_layer(scroll)
                if event.button == 5: 
                    scroll = min(scroll + 1, 100)
                    draw_layer(scroll)
                #print(scroll)