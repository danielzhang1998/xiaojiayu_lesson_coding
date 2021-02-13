import pygame, sys, traceback
from pygame.locals import *
from random import *

# 球类继承自Spirte类
class Ball(pygame.sprite.Sprite):
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        # 将小球放在指定位置
        self.rect.left, self.rect.top = position
        self.side = [choice([-1, 1]), choice([-1, 1])]
        self.speed = speed
        self.collide = False
        self.target = target
        self.control = False
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2

    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move((self.side[0] * self.speed[0], self.side[1] * self.speed[1]))

        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
        # 这样便实现了从左边进入，右边出来的效果
        if self.rect.right <= 0:
            self.rect.left = self.width

        elif self.rect.left >= self.width:
            self.rect.right = 0

        elif self.rect.bottom <= 0:
            self.rect.top = self.height

        elif self.rect.top >= self.height:
            self.rect.bottom = 0

    def check(self, motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False

# 最下方的玻璃面板
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.glass_image =pygame.image.load(glass_image).convert_alpha()
        self.glass_image.set_alpha(180)
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) //2, (bg_size[1] - self.glass_rect.height)
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top
        pygame.mouse.set_visible(False)

def main():
    pygame.init()

    grayball_image = "/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/gray_ball.png"
    greenball_image = "/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/green_ball.png"
    bg_image = "/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/background.png"
    glass_image = "/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/glass.png"
    mouse_image = "/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/hand.png"

    running = True

    # 添加魔性的背景音乐
    pygame.mixer.music.load("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/bg_music.ogg")
    pygame.mixer.music.play()

    # 添加音效
    loser_sound = pygame.mixer.Sound("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/loser.wav")
    laugh_sound = pygame.mixer.Sound("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/laugh.wav")
    winner_sound = pygame.mixer.Sound("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/winner.wav")
    hole_sound = pygame.mixer.Sound("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/hole.wav")

    # 音乐播放完时游戏结束
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)

    # 根据背景图片指定游戏界面尺寸
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - FishC Demo")

    background = pygame.image.load(bg_image).convert_alpha()

    # 黑洞
    hole = [
    (117, 119, 199, 201),
    (225, 227, 390, 392), 
    (503, 505, 320, 322),
    (698, 700, 192, 194),
    (906, 908, 419, 421)
    ]

    # 打印的消息的列表
    msgs = []

    # 用来存放小球对象的列表
    balls = []
    group = pygame.sprite.Group()

    # 创建五个小球
    for i in range(5):
        # 位置随机，速度随机
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(1, 10), randint(1, 10)]
        ball = Ball( grayball_image, greenball_image, position, speed, bg_size, target = 5 * (i + 1))
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
        balls.append(ball)
        group.add(ball)

    glass = Glass(glass_image, mouse_image, bg_size)

    motion = 0

    # 设置自定义事件

    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1 * 1000)

    pygame.key.set_repeat(100, 100)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                laugh_sound.play()
                pygame.time.delay(2500)
                running = False

            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0

            elif event.type == MOUSEMOTION:
                motion += 1

            # 响应玩家的键盘输入 WASD 上下左右

            elif event.type == KEYDOWN and (event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d or event.key == K_SPACE):
                for each in group:
                    if each.control:
                        if event.key == K_w:
                            each.speed[1] -= 1
                        if event.key == K_s:
                            each.speed[1] += 1
                        if event.key == K_a:
                            each.speed[0] -= 1
                        if event.key == K_d:
                            each.speed[0] += 1
                        if event.key == K_SPACE:
                            for i in hole:
                                if i[0] - 8 <= each.rect.left <= i[1] + 8 and i[2] - 8 <= each.rect.top <= i[3] + 8:
                                    hole_sound.play()
                                    each.speed = [0, 0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0, temp)
                                    hole.remove(i)

                            if not hole:
                                pygame.mixer.music.stop()
                                winner_sound.play()
                                pygame.time.delay(3000)
                                msg = pygame.image.load("/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/lesson87and88_pygame_v1/win.png").convert_alpha()
                                msg_pos = (width - msg.get_width()) // 2, (height - msg.get_height()) // 2
                                msgs.append((msg, msg_pos))
                                pygame.time.delay(3000)
                                laugh_sound.play()
                                pygame.time.delay(3000)
                    
        screen.blit(background, (0, 0))
        screen.blit(glass.glass_image, glass.glass_rect)

        # 获得鼠标所在的位置
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
           glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
           glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height          

        screen.blit(glass.mouse_image, glass.mouse_rect)

        for each in balls:
            each.move()
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False
            if each.control:
                # 画一个绿色的小球
                screen.blit(each.greenball_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)

        for each in group:
            group.remove(each)

            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.side[0] = - each.side[0]
                each.side[1] = - each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False

            group.add(each)

        for msg in msgs:
            screen.blit(msg[0], msg[1])

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except:
        traceback.print_exc()
        pygame.quit()
        input()