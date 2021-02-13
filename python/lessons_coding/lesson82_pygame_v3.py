import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 600, 400
speed = [5, 0]
bg = (255, 255, 255)    # 背景颜色为白色




screen = pygame.display.set_mode(size)  # 对话框大小

pygame.display.set_caption("Hello world!")  # title

cat = pygame.image.load('/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')   # 运动主体的图像

cat_right = pygame.transform.rotate(cat, 90)
cat_top = pygame.transform.rotate(cat, 180)
cat_left = pygame.transform.rotate(cat, 270)
cat_bottom = cat
cat = cat_top

position = cat.get_rect()   # 创建长方形

list_mode = pygame.display.list_modes()  # 获得可使用的分辨率，以列表包含元组的形式，每一个元组里面的数字为可使用的分辨率，列表从高到低排序

l_head = cat
r_head = pygame.transform.flip(cat, True, False)

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()

        if event.type == KEYDOWN:
            #   全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(list_mode[0], FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)

            if event.key == K_ESCAPE and fullscreen == True:
                fullscreen = False
                screen = pygame.display.set_mode(size)

    position = position.move(speed)

    if position.right > width: # 撞墙
        cat = cat_right
        position = cat_rect = cat.get_rect()
        position.left = width - cat_rect.width
        speed = [0, 5]

    if position.bottom > height: # 撞墙
        cat = cat_bottom
        position = cat_rect = cat.get_rect()
        position.left = width - cat_rect.width
        position.top = height - cat_rect.height
        speed = [-5, 0]

    if position.left < 0: # 撞墙
        cat = cat_left
        position = cat_rect = cat.get_rect()
        position.top = height - cat_rect.height
        speed = [0, -5]

    if position.top < 0: # 撞墙
        cat = cat_top
        position = cat_rect = cat.get_rect()
        speed = [5, 0]

    screen.fill(bg) # 背景颜色填充
    screen.blit(cat, position)  # 将图片放置在长方形上
    pygame.display.flip()   # 刷新
    pygame.time.delay(10)   # 延迟