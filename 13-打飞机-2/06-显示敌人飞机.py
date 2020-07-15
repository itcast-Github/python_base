#coding=utf-8
import pygame
from pygame.locals import *


#接下来要做的任务：
#1. 实现飞机在你想要的位置显示
#2. 实现按键控制飞机移动
#3. 实现按下空格键的时候，显示一颗子弹


class HeroPlane(object):

    def __init__(self,screen):

        #设置飞机默认的位置
        self.x = 230
        self.y = 600
        
        #设置要显示内容的窗口
        self.screen = screen


        self.imageName = "./feiji/hero.gif"

        self.image = pygame.image.load(self.imageName).convert()

        #用来存储英雄飞机发射的所有子弹
        self.bulletList = []


    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()



        #修改所有子弹的位置
        # for bullet in self.bulletList:
        #     bullet.y -= 2



    def moveLeft(self):
        self.x -= 10


    def moveRight(self):
        self.x += 10


    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)


class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()

    def move(self):
        self.y -= 2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))


class EnemyPlane(object):

    def __init__(self,screen):

        #设置飞机默认的位置
        self.x = 0
        self.y = 0
        
        #设置要显示内容的窗口
        self.screen = screen


        self.imageName = "./feiji/enemy-1.gif"

        self.image = pygame.image.load(self.imageName).convert()

        #用来存储敌人飞机发射的所有子弹
        self.bulletList = []


    def display(self):
        self.screen.blit(self.image,(self.x,self.y))


if __name__ == "__main__":

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,890),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()


    #3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    #4. 创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    #3. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))

        heroPlane.display()
        enemyPlane.display()

        #判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                    #控制飞机让其向左移动
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    print("space")
                    heroPlane.sheBullet()

        pygame.display.update()
