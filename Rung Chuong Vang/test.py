import datetime
from random import choice, randint
import pygame
from sys import exit


pygame.init()
screen=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
game_active=False
score=0
lagre_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',40) 
medium_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',20)
small_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',10)
start_time=0
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN=(124,252,0)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)
COLOR_A=BLACK
COLOR_B=BLACK
COLOR_C=BLACK
COLOR_D=BLACK
check=0

#ques list
class content:
    def __init__(self,ques,anwA,anwB,anwC,anwD,res) -> None:
        self.ques=ques
        self.anwA=anwA
        self.anwB=anwB
        self.anwC=anwC
        self.anwD=anwD
        self.res=res
ques_lst=[]
content1=content('What is 5*5 ?','A: 15','B: 20','C: 25','D: 30','C')
content2=content('What is 5*4 ?','A: 15','B: 20','C: 25','D: 30','B')
content3=content('Gió nào được gọi là gió bão?','A: Cấp 2','B: Cấp 3','C: Cấp 5','D: Cấp 9','D')
content4=content('Một kg bằng mấy lạng?','A: 8','B: 9','C: 10','D: 11 ','C')
content5=content('Quốc hiệu đầu tiên của nước ta?','A: Vạn Xuân','B: Đại Ngu','C: Đại Việt','D: Văn Lang','D')
content6=content('Một ngày kim giờ quay mấy vòng?','A: 24','B: 25','C: 22','D: 23','A')
content7=content('Ai là tác giả bài thơ “Lượm”?','A: Tố Hữu','B: Xuân Diệu','C: Huy Cận','D: Nguyễn Bính','A')
content8=content('Hà Nội có mấy cửa ô?','A: 2','B: 3','C: 4','D: 5','D')
content9=content('Bộ phận hô hấp của châu chấu?','A: Đàu','B: Bụng','C: Chân','D: Lưng','B')ng','B')
ques_lst.append(content1)
ques_lst.append(content2)
ques_lst.append(content3)
ques_lst.append(content4)
ques_lst.append(content5)
ques_lst.append(content6)
ques_lst.append(content7)
ques_lst.append(content9)
ques_lst.append(content8)

ques_index=0

        
#intro
dap_an = pygame.image.load('Millionair_Images/dapan.png').convert_alpha()
dap_an_rect = dap_an.get_rect(center=(600,270))
end = pygame.image.load('Millionair_Images/end.png').convert_alpha()
end_rect = end.get_rect(topleft=(0,0))
tiep = pygame.image.load('Millionair_Images/next.png').convert_alpha()
tiep_rect = tiep.get_rect(center=(600,320))
back_ground = pygame.image.load('Millionair_Images/background.jpg').convert_alpha()
back_ground_rect = back_ground.get_rect(center=(400,200))
logo_game=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.png').convert_alpha()
logo_game_rect=logo_game.get_rect(center=(400,150))
intro_mes=lagre_font.render('Ring the golden bell !!!',True,('#ffffff'))
intro_mes_rect=intro_mes.get_rect(center=(400,300))
play=medium_font.render('Press space to begin.',True,('#0066FF'),)
play_rect=intro_mes.get_rect(center=(510,350))
logoplay = pygame.image.load('Millionair_Images/play.png').convert_alpha()
logoplay_rect = logoplay.get_rect(center=(510,30))


#decor in game
decor=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.png').convert_alpha()
decor=pygame.transform.rotozoom(decor,0,0.2)
decor_rect=decor.get_rect(center=(60,60))

name_header=lagre_font.render('Ring the golden bell !',True,('red'))
name_header_rect=intro_mes.get_rect(center=(400,60))



#clock
timer=pygame.image.load('Millionair_Images/red-clock-png-alarm-0.png').convert_alpha()
timer=pygame.transform.rotozoom(timer,0,0.03)
timer_rect=timer.get_rect(center=(720,60))



def display_time():
    current_time=round(pygame.time.get_ticks()/1000)-start_time
    s=format(15-current_time, "0>2,d")
    clock_surf=medium_font.render(f'00:{s}',True,'blue')
    clock_rect=clock_surf.get_rect(center=(720,60))
    screen.blit(clock_surf,clock_rect)
    return int(s)

c = 1

done_yet=0
while True:
    
    screen.fill('white')
    
    if ques_index==len(ques_lst):
        break  
    #question
    question=lagre_font.render(f'Câu {ques_index+1}: '+ques_lst[ques_index].ques,True,('red'))
    question_rect=question.get_rect(center=(400,150))
    #answer
    answer_A=medium_font.render(ques_lst[ques_index].anwA,True,COLOR_A)
    answer_B=medium_font.render(ques_lst[ques_index].anwB,True,COLOR_B)
    answer_C=medium_font.render(ques_lst[ques_index].anwC,True,COLOR_C)
    answer_D=medium_font.render(ques_lst[ques_index].anwD,True,COLOR_D)
    answer_A_rect=answer_A.get_rect(center=(350,200))
    answer_B_rect=answer_B.get_rect(center=(350,250))
    answer_C_rect=answer_C.get_rect(center=(350,300))
    answer_D_rect=answer_D.get_rect(center=(350,350))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if game_active==False and done_yet == 0:
            screen.blit(back_ground,back_ground_rect)
            screen.blit(logo_game,logo_game_rect)
            screen.blit(intro_mes,intro_mes_rect)
            screen.blit(play,play_rect) 
            pygame.display.update() 
            if event.type == pygame.KEYDOWN :
                    if event.key== pygame.K_SPACE:
                        game_active=True
                        done_yet = 1
                        score=0
                        ques_index=0
                        start_time=round(pygame.time.get_ticks()/1000)
                        COLOR_A=BLACK
                        COLOR_B=BLACK
                        COLOR_C=BLACK
                        COLOR_D=BLACK
        if game_active==False and done_yet==1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if dap_an_rect.collidepoint(event.pos):
                        start_time = round(pygame.time.get_ticks()/1000) -15
                        c = 0
                        game_active=True
                        COLOR_A=RED
                        COLOR_B=RED
                        COLOR_C=RED
                        COLOR_D=RED
                        if ques_lst[ques_index].res=='A':
                            COLOR_A=GREEN
                        if ques_lst[ques_index].res=='B':
                            COLOR_B=GREEN
                        if ques_lst[ques_index].res=='C':
                            COLOR_C=GREEN
                        if ques_lst[ques_index].res=='D':
                            COLOR_D=GREEN
                        answer_A=medium_font.render(ques_lst[ques_index].anwA,True,COLOR_A)
                        answer_B=medium_font.render(ques_lst[ques_index].anwB,True,COLOR_B)
                        answer_C=medium_font.render(ques_lst[ques_index].anwC,True,COLOR_C)
                        answer_D=medium_font.render(ques_lst[ques_index].anwD,True,COLOR_D)
            if event.type == pygame.MOUSEBUTTONDOWN and c == 0:
                    if tiep_rect.collidepoint(event.pos):
                        c = 1
                        game_active=True
                        start_time=round(pygame.time.get_ticks()/1000)
                        ques_index+=1
                        COLOR_A=BLACK
                        COLOR_B=BLACK
                        COLOR_C=BLACK
                        COLOR_D=BLACK
    if game_active :    
        
        screen.fill('white') 
        screen.blit(back_ground,back_ground_rect)
        pygame.draw.rect(screen,'white',pygame.Rect(20,100,760,5),0,10)
        pygame.draw.rect(screen,'red',pygame.Rect(10,10,780,380),6,20)
        screen.blit(tiep,tiep_rect)
        screen.blit(dap_an,dap_an_rect) 
        screen.blit(decor,decor_rect)
        screen.blit(name_header,name_header_rect)
        screen.blit(timer,timer_rect)
        screen.blit(question,question_rect)
        screen.blit(answer_A,answer_A_rect)
        screen.blit(answer_B,answer_B_rect)
        screen.blit(answer_C,answer_C_rect)
        screen.blit(answer_D,answer_D_rect)
        if display_time()<=0:
            
            game_active = False
            
            

        pygame.display.update() 
        clock.tick(60)
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('white') 
    screen.blit(end,end_rect) 

    pygame.display.update()
