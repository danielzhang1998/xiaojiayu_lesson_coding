import pygame, sys

pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)    # 背景颜色为白色

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)  # 对话框大小

pygame.display.set_caption("Hello world!")  # title

cat = pygame.image.load('/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')   # 运动主体的图像

position = cat.get_rect()   # 创建长方形

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()

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