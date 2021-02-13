import pygame, sys

from pygame.locals import *

pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)    # 背景颜色为白色

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size, RESIZABLE)  # 对话框大小

pygame.display.set_caption("Hello world!")  # title

old_cat = pygame.image.load('/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')   # 运动主体的图像
cat = old_cat

old_cat_rect = old_cat.get_rect()

position = cat_rect = old_cat_rect   # 创建长方形

list_mode = pygame.display.list_modes()  # 获得可使用的分辨率，以列表包含元组的形式，每一个元组里面的数字为可使用的分辨率，列表从高到低排序

l_head = cat    # 头的左右朝向
r_head = pygame.transform.flip(cat, True, False)

fullscreen = False  # 是否全屏

ratio = 1.0 # 图片的缩放比例

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                speed = [-1, 0]
                cat = l_head
            if event.key == K_RIGHT or event.key == K_d:
                speed = [1, 0]            
                cat = r_head
            if event.key == K_UP or event.key == K_w:
                speed = [0, -1]
            if event.key == K_DOWN or event.key == K_s:
                speed = [0, 1]

            # F11 全屏， F11 或者 ESC 退出全屏
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(list_mode[0], FULLSCREEN | HWSURFACE)
                    width, height = list_mode[0][0], list_mode[0][1]
                else:
                    screen = pygame.display.set_mode(size)

            if event.key == K_ESCAPE and fullscreen == True:
                fullscreen = False
                screen = pygame.display.set_mode(size)

            # 对图片进行放大，缩小，恢复原状
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                cat = pygame.transform.smoothscale(old_cat, (int(old_cat_rect.width * ratio), int(old_cat_rect.height * ratio)))
                l_head = cat
                r_head = pygame.transform.flip(cat, True, False)
        '''
        # 用户调整页面尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)
        '''


    position = position.move(speed)

    if position.left < 0 or position.right > width: # 撞墙
        cat = pygame.transform.flip(cat, True, False)   #   对象，左右翻转，上下颠倒
        speed[0] = -speed[0]    # 左右翻转

    if position.top < 0 or position.bottom > height:
        cat = pygame.transform.flip(cat, True, False)
        speed[1] = -speed[1]    # 上下翻转

    screen.fill(bg) # 背景颜色填充
    screen.blit(cat, position)  # 将图片放置在长方形上
    pygame.display.flip()   # 刷新
    #pygame.time.delay(10)   # 延迟
    clock.tick(1000)    # 每秒不高于 x 帧