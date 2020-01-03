import pygame, sys, numpy as np, pictureIT, AiKNN

size = width, height = 280, 280
screen = pygame.display.set_mode(size)
white = 255, 255, 255
black = 0, 0, 0
brush = None
screen.fill(black)


def pixelsToGreyscaleArray(px):
    rows = columns = range(28)
    image = [0]
    for row in rows:
        for col in columns:
            temp = px[col * 10:col * 10 + 10, row * 10:row * 10 + 10]
            temp_sum = 0
            for x in range(10):
                for y in range(10):
                    temp_sum += temp[x][y]
            image.append(int((temp_sum / 1677721500) * 255))
    pictureIT.save_picture(image)
    return image


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                brush = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                brush = None
        elif event.type == pygame.MOUSEMOTION:
            if brush:
                brush = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                px = pygame.surfarray.pixels2d(screen)
                AiKNN.useAI(pixelsToGreyscaleArray(px))
                screen.fill(black)
        if brush:
            pygame.draw.circle(screen, white, [brush[0], brush[1]], 7)
        pygame.display.flip()
