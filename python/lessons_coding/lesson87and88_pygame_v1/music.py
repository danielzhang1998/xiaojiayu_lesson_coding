import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('/Users/zhanghanlin/Documents/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/bg_music.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

cat_sound = pygame.mixer.Sound('/Users/zhanghanlin/Documents/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/cat.wav')
cat_sound.set_volume(0.2)

dog_sound = pygame.mixer.Sound('/Users/zhanghanlin/Documents/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/dog.wav')
dog_sound.set_volume(0.2)

bg_size = width, height = 300, 200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Music Demo')

pause = False

pause_image = pygame.image.load('/Users/zhanghanlin/Documents/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/pause.png').convert_alpha()
unpause_image = pygame.image.load('/Users/zhanghanlin/Documents/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/unpause.png').convert_alpha()

pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cat_sound.play()
            if event.button == 3:
                dog_sound.play()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause

    screen.fill((255, 255, 255))

    if pause:
        screen.blit(pause_image, pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(unpause_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()

    clock.tick(30)