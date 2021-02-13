import pygame, sys, time

pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hello world!')
bg = (0, 0, 0)
position = 0


font = pygame.font.Font(None, 20)
line_height = font.get_linesize()
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        localtime = time.asctime( time.localtime(time.time()) )
        if 'KeyDown' in str(event): # get the user insert
            screen.blit(font.render(str(localtime) + ", event: " + str(event), True, (0, 255, 0)),(0, position)) # True 为消除锯齿
            position += line_height

        if position > height:
            position = 0
            screen.fill(bg)
    
    pygame.display.flip()