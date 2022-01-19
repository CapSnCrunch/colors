import pygame
import math

width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('ParaColor')

curve = []
speed = 3
precision = 10

def redraw_window(win, point, scroll):

    tracing_curve = False

    # Fill background with current function value
    try:
        color = list(pygame.mouse.get_pos()) + [scroll]
        color[0], color[1] = 255 * (color[0] - 10) / 150, 255 * (color[1] - 10) / 150
        win.fill(color)
    except:
        try:
            color = (int(point[0]), int(point[1]), int(point[2]))
            win.fill(color)
            tracing_curve = True
        except:
            win.fill((0, 0, 0))

    # Draw the current cross section of the color cube
    pygame.draw.rect(win, (0, 0, 0), (8, 8, 150, 150))
    for i in range(int(255 / precision) + 1):
        for j in range(int(255 / precision) + 1):
            pygame.draw.rect(win, (i * precision, j * precision, scroll), (10 + 136 * (i / int(255/precision)), 
                10 + 136 * (j / int(255/precision)), precision, precision))
    
    # Draw full color cube in R3
    pygame.draw.rect(win, (0, 0, 0), (170, 8, 150, 150))

    # Draw Axes
    pygame.draw.line(win, (255, 0, 0), (230, 100), (315, 100), 2)
    pygame.draw.line(win, (0, 255, 0), (230, 100), (175, 155), 2)
    pygame.draw.line(win, (0, 0, 255), (230, 100), (230, 10), 2)

    # Draw Cross Section in R3
    pygame.draw.aalines(win, (255, 255, 255), True, [(175, 155 - scroll * (90/255)), 
        (270, 155 - scroll * (90/255)), (315, 100 - scroll * (90/255)), 
        (230, 100 - scroll * (90/255))], 2)
    
    # Draw Curve
    for i in range(len(curve)):
        p = curve[i]
        point_x = int(230+(90*p[0])/255 - 55*p[1]/255)
        point_y = int(100-(90*p[2])/255 + 55*p[1]/255)
        pygame.draw.circle(win, (255, 255, 255), (point_x, point_y), 2)
        
        if len(curve) >= 2:
            q = curve[(i+1) % len(curve)]
            pointq_x = int(230+(90*q[0])/255 - 55*q[1]/255)
            pointq_y = int(100-(90*q[2])/255 + 55*q[1]/255)
            pygame.draw.line(win, (255, 255, 255), (point_x, point_y), (pointq_x, pointq_y))

    if tracing_curve:
        point_x = int(230+(90*point[0])/255 - 55*point[1]/255)
        point_y = int(100-(90*point[2])/255 + 55*point[1]/255)
        pygame.draw.circle(win, (color), (point_x, point_y), 4)

    pygame.display.update()

def main():

    t = 0
    reverse = False
    clock = pygame.time.Clock()

    scroll = 0

    current_point = [None]

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor = list(pygame.mouse.get_pos())
                if 10 < cursor[0] < 158 and 10 < cursor[1] < 158:
                    if event.button == 1: 
                        curve.append([255*(cursor[0]-10)/148, 255*(cursor[1]-10)/148, scroll])
                        current_point = [curve[0], 0]
                    if event.button == 4: scroll = max(scroll - 10, 0)
                    if event.button == 5: scroll = min(scroll + 10, 255)

        '''
        # Check if time needs to reverse (happens when the function exists the color cube)
        point = function(t + 1 - 2 * reverse)
        if point[0] < 0 or point[0] > 255 or point[1] < 0 or point[1] > 255 or point[2] < 0 or point[0] > 255:
            reverse = not reverse

        # Step through the parametric
        t += 1 - 2 * reverse
        '''

        if len(curve) >= 2:
            p = curve[current_point[1]]
            q = curve[(current_point[1] + 1) % len(curve)]
            step = [q[0]-p[0], q[1]-p[1], q[2]-p[2]]
            dist = max((step[0]**2 + step[1]**2 + step[2]**2)**(1/2), 0.001)
            current_point[0] = [current_point[0][0] + step[0]*speed/dist, current_point[0][1]+step[1]*speed/dist, current_point[0][2]+step[2]*speed/dist]
            if ((current_point[0][0] - q[0])**2 + (current_point[0][1] - q[1])**2 + (current_point[0][2] - q[2])**2 )**(1/2) <= 4:
                current_point[1] = (current_point[1] + 1) % len(curve)
        redraw_window(win, current_point[0], scroll)
    
main()