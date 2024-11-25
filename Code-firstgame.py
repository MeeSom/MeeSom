import pygame
import random
#ประกาศใช้งานเกม
pygame.init()
#หัวข้อเกม
pygame . display . set_caption("Meesom Game")
#ตั้งค่าสี
WHITE  = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,141,161 )
#ขนาดหน้าจอเกม
SCREEN_W =1200
SCREEN_H =600
screen = pygame . display .set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(PINK)
#การออกแบบรูปทรง
import pygame
#ประกาศใช้งานเกม
pygame.init()
#หัวข้อเกม
pygame . display . set_caption("Meesom Game")
#ตั้งค่าสี
WHITE  = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,141,161 )
PINKEY = (255,150,161)
GAY = (105,105,105)
OR = ( 255,165,0)
BK = (0,0,0)
YELLO = (255,255,0)
#ความเร็วการเคลื่อนที่
speed = 10
som_speed =2
FPS =60
clock = pygame.time.Clock()
#ขนาดหน้าจอเกม
SCREEN_W =1480
SCREEN_H =800
screen = pygame . display .set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม
screen.fill(PINK)
som = pygame.image.load("som.png")
som = pygame.transform.scale(som,(150,150))
som_rect = som.get_rect()
som_rect.x=random.randint(10,SCREEN_W-50)
som_rect.y=0

mee = pygame.image.load("mee.png")
mee = pygame.transform.scale(mee,(450,300))
mee_rect = mee.get_rect()
mee_rect.centerx = SCREEN_W // 2
mee_rect.centery = 650
#คะแนน
score = 0

#ตัวอักษรข้อความ
sys_font = pygame . font .SysFont("arial",40)
sys_font2 = pygame . font .SysFont("arial",30)
merssage_text = sys_font2.render("UWU",True,WHITE)
title_text = sys_font.render("Welcome to Meesom game",True,WHITE)
description_text = sys_font2.render("This is my first game",True,WHITE)
description2_text = sys_font2.render("I know it not the best but i try my best",True,WHITE)


wellcome_rect= title_text.get_rect()
wellcome_rect.topright=(1470,5)

font = pygame.font.Font("coiny.ttf",60)
top_text=font.render("Score : "+str(score),True,WHITE)
score_rect= top_text.get_rect()
score_rect.topleft=(10,10)
"""
fonts = pygame . font . get_fonts()
for front in fonts : 
    print(front)
    """
#แสดงผลรูปแบบต่างๆ
running=True
while running:
    for event in pygame . event.get():
        if event . type == pygame . QUIT :
            running=False
    #การชน
    if mee_rect.colliderect(som_rect):
        score+=10
        top_text=font.render("Score : "+str(score),True,WHITE)
        som_rect.x=random.randint(3,SCREEN_W-100)
        som_rect.y=0
        if event . type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event . pos[0]
            mouse_y = event . pos[1]
            mee_rect.centerx=mouse_x
            mee_rect.centery=mouse_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]and mee_rect.left>0:
        mee_rect.x-=speed
    if keys[pygame.K_d]and mee_rect.right<1480:
        mee_rect.x+=speed   

    #เคลื่อนที่ส้ม
    if som_rect.y< SCREEN_H:
         som_rect.y+=som_speed
    else:#ทะลุจอ
        som_rect.x=random.randint(5,SCREEN_W-50)
        som_rect.y=0
    screen.fill(PINK)
    screen.blit(mee,(mee_rect))
    screen.blit(som,(som_rect))
    screen . blit(title_text,wellcome_rect)
    screen . blit(description_text,(1150,50))
    screen . blit(description2_text,(1050,90))
    screen . blit(merssage_text,(1240,130))
    screen . blit(top_text,score_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
