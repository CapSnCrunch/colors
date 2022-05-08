import pygame

width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Color Curves')

if __name__ == '__main__':

    red = [0] * int((width - 100) / 4)
    green = [0] * int((width - 100) / 4)
    blue = [0] * int((width - 100) / 4)

    dragging = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

        if dragging:
            cursor = list(pygame.mouse.get_pos())
            # CHECK RED GRAPH
            if 50 < cursor[0] < width-50 and 50 < cursor[1] < 150:
                red[int((cursor[0]-50)/4)] = 255 - 255 * (cursor[1] - 50)/100

            # CHECK GREEN GRAPH
            if 50 < cursor[0] < width-50 and 200 < cursor[1] < 300:
                green[int((cursor[0]-50)/4)] = 255 - 255 * (cursor[1] - 200)/100

            # CHECK BLUE GRAPH
            if 50 < cursor[0] < width-50 and 350 < cursor[1] < 450:
                blue[int((cursor[0]-50)/4)] = 255 - 255 * (cursor[1] - 350)/100

        win.fill((255, 255, 255))

        # RED GRAPH
        pygame.draw.line(win, (0,0,0), (50, 50), (50, 150), 2)
        pygame.draw.line(win, (0,0,0), (50, 150), (width - 50, 150), 2)
        for i in range(len(red)-1):
            # pygame.draw.ellipse(win, (255,0,0), (50+i*4, 150-100*(red[i]/255), 4, 4))
            pygame.draw.line(win, (255,0,0), (50+i*4, 150-100*(red[i]/255)), (50+(i+1)*4, 150-100*(red[(i+1)]/255)))

        # GREEN GRAPH
        pygame.draw.line(win, (0,0,0), (50, 200), (50, 300), 2)
        pygame.draw.line(win, (0,0,0), (50, 300), (width - 50, 300), 2)
        for i in range(len(green)-1):
            # pygame.draw.ellipse(win, (0,255,0), (50+i*4, 300-100*(green[i]/255), 4, 4))
            pygame.draw.line(win, (0,255,0), (50+i*4, 300-100*(green[i]/255)), (50+(i+1)*4, 300-100*(green[(i+1)]/255)))

        # BLUE GRAPH
        pygame.draw.line(win, (0,0,0), (50, 350), (50, 450), 2)
        pygame.draw.line(win, (0,0,0), (50, 450), (width - 50, 450), 2)
        for i in range(len(blue)-1):
            # pygame.draw.ellipse(win, (0,0,255), (50+i*4, 450-100*(blue[i]/255), 4, 4))
            pygame.draw.line(win, (0,0,255), (50+i*4, 450-100*(blue[i]/255)), (50+(i+1)*4, 450-100*(blue[(i+1)]/255)))

        # DRAW GRADIENT
        for i in range(len(red)):
            pygame.draw.line(win, (red[i], green[i], blue[i]), (50+i*4, 500), (50+i*4, 550), 4)

        pygame.display.update()