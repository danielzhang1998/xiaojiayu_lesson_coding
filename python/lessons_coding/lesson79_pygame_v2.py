import pygame, sys, time



pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hello world!')

f = open('test.txt','w')

while True:
    for event in pygame.event.get():
        localtime = time.asctime( time.localtime(time.time()) )
        if 'KeyDown' in str(event): # get the user insert
            f.write(str(localtime) + ", event: " + str(event) + '\n')
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()