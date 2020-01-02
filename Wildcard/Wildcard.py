import pygame,math,os,time,random
from pygame.locals import *

#Colours:
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
orange = (255,140,0)
greenyellow = (103,175,17)
green = (0,255,0)
darkgreen = (0,100,0)
cyan = (0,255,255)
blue = (0,0,255)
skyblue = (135,206,250)
navyblue = (0,0,128)
gray = (128,128,128)
lightgray = (211,211,211)



size=[700,400]

pygame.init()
pygame.font.init()

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Game")

clock=pygame.time.Clock()



crashed=False
screen_now="main-menu"
difficulty=1
user_entry=""
showhint=False
pygame.mixer.init(96000)
pygame.mixer.music.load('fluffing_a_duck.wav')
pygame.mixer.music.play(-1)



def updateFontSize():
    global comic_sans_p, arial_p, courier_p, comic_sans_h1, arial_h1, courier_h1, comic_sans_h2, arial_h2, courier_h2, comic_sans_h3, arial_h3, courier_h3
    comic_sans_p = pygame.font.SysFont('Comic Sans MS', 20)
    arial_p = pygame.font.SysFont('Arial', 20)
    courier_p = pygame.font.SysFont('Courier', 20)
    comic_sans_h1 = pygame.font.SysFont('Comic Sans MS', 50)
    arial_h1 = pygame.font.SysFont('Arial', 50)
    courier_h1 = pygame.font.SysFont('Courier', 50)
    comic_sans_h2 = pygame.font.SysFont('Comic Sans MS', 40)
    arial_h2 = pygame.font.SysFont('Arial', 40)
    courier_h2 = pygame.font.SysFont('Courier', 40)
    comic_sans_h3 = pygame.font.SysFont('Comic Sans MS', 34)
    arial_h3 = pygame.font.SysFont('Arial', 34)
    courier_h3 = pygame.font.SysFont('Courier', 34)

updateFontSize()






def loadScreen(scr):
    global screen_now,difficulty,crashed,newround,starttime,correct,corr_answer,user_entry,timetaken,showhint,hint_line1,hint_line2,hint_line3,thing_index
    if scr=="main-menu":
        pygame.draw.polygon(screen, red, [(235,20),(229,24),(225,30),(225,130),(229,136),(235,140),(465,140),(471,136),(475,130),(475,30),(471,24),(465,20)])
        textsurface = comic_sans_h1.render('Wildcard', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 80
        screen.blit(textsurface,textbox)
        #Play button
        button = pygame.draw.rect(screen, white, (225,170,250,60))
        textsurface = comic_sans_h3.render('Play', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 197
        screen.blit(textsurface,textbox)
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (225,170,250,60))
            textsurface = comic_sans_h3.render('Play', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 197
            screen.blit(textsurface,textbox)
        #Settings button
        button = pygame.draw.rect(screen, white, (225,250,250,60))
        textsurface = comic_sans_h3.render('Credits', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 277
        screen.blit(textsurface,textbox)
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (225,250,250,60))
            textsurface = comic_sans_h3.render('Credits', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 277
            screen.blit(textsurface,textbox)
        #Quit button
        button = pygame.draw.rect(screen, white, (225,330,250,60))
        textsurface = comic_sans_h3.render('Quit', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 357
        screen.blit(textsurface,textbox)
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (225,330,250,60))
            textsurface = comic_sans_h3.render('Quit', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 357
            screen.blit(textsurface,textbox)
    elif scr=="play":
        if newround:
            starttime=round(time.time(),1)
            timeleft=20
            things_file=r"Cards/"+str(difficulty)+"/things.txt"
            hints_file=r"Cards/"+str(difficulty)+"/hints.txt"
            things_list = open(things_file,"r")
            things_list = things_list.read().split("\n")
            hints_list = open(hints_file,"r")
            hints_list = hints_list.read().split("\n")
            thing_index = random.randint(0,len(things_list)-1)
            hint = str(hints_list[thing_index]).split(" ")
            hint_line1 = ""
            hint_line2 = ""
            hint_line3 = ""
            curr_line=1
            for i in range(len(hint)):
                if len(hint_line1)<55 and len(hint_line1)+len(hint[i])<=55 and curr_line==1:
                    hint_line1+=str(hint[i])+" "
                elif len(hint_line2)<55 and len(hint_line2)+len(hint[i])<=55 and curr_line==2:
                    curr_line=2
                    hint_line2+=str(hint[i])+" "
                else:
                    hint_line3+=str(hint[i])+" "
            
            corr_answer=things_list[thing_index].upper()
            correct=False
            newround=False
            user_entry=""
        #Level
        textsurface = comic_sans_h3.render(('Level '+str(difficulty)), False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 30
        screen.blit(textsurface,textbox)
        #Hint button
        button = pygame.draw.rect(screen, white, (30,10,130,50))
        textsurface = comic_sans_h3.render("Hint", False, black)
        textbox = textsurface.get_rect()
        textbox.x = 78
        textbox.centery = 35
        screen.blit(textsurface,textbox)
        screen.blit(pygame.image.load(r"hint.png"), (35, 20))
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (30,10,130,50))
            textsurface = comic_sans_h3.render('Hint', False, black)
            textbox = textsurface.get_rect()
            textbox.x = 78
            textbox.centery = 35
            screen.blit(textsurface,textbox)
            screen.blit(pygame.image.load(r"hint.png"), (35, 20))
        #Hint box
        if showhint:
            pygame.draw.rect(screen,lightgray, (75,50,550,300))
            textsurface = comic_sans_h2.render('Hint', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 90
            screen.blit(textsurface,textbox)
            textsurface = comic_sans_p.render(hint_line1, False, black)
            textbox = textsurface.get_rect()
            textbox.x = 100
            textbox.centery = 150
            screen.blit(textsurface,textbox)
            textsurface = comic_sans_p.render(hint_line2, False, black)
            textbox = textsurface.get_rect()
            textbox.x = 100
            textbox.centery = 170
            screen.blit(textsurface,textbox)
            textsurface = comic_sans_p.render(hint_line3, False, black)
            textbox = textsurface.get_rect()
            textbox.x = 100
            textbox.centery = 190
            screen.blit(textsurface,textbox)
            textsurface = comic_sans_p.render("Click anywhere to close", False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 300
            screen.blit(textsurface,textbox)
        #Image
        if not showhint:
            path=r"Cards/"+str(difficulty)+"/"+str(thing_index)+".jpg"
            screen.blit(pygame.image.load(path), (212, 90))
        #User input
        if not showhint:
            pygame.draw.rect(screen, lightgray, (200,300,300,40))
            textsurface = comic_sans_p.render(user_entry, False, black)
            textbox = textsurface.get_rect()
            textbox.x = 210
            textbox.centery = 317
            screen.blit(textsurface,textbox)
        #Update Time (With color)
        timeleft = round(20-(round(time.time(),1)-starttime),1)
        timetaken = 20-timeleft
        if timeleft>15:
            timeleft_color=darkgreen
        elif timeleft>12:
            timeleft_color=greenyellow
        elif timeleft>8:
            timeleft_color=yellow
        elif timeleft>5:
            timeleft_color=orange
        elif timeleft>4.5:
            timeleft_color=red
        elif timeleft>4:
            timeleft_color=white
        elif timeleft>3.5:
            timeleft_color=red
        elif timeleft>3:
            timeleft_color=white
        elif timeleft>2.5:
            timeleft_color=red
        elif timeleft>2:
            timeleft_color=white
        elif timeleft>1.5:
            timeleft_color=red
        elif timeleft>1:
            timeleft_color=white
        else:
            timeleft_color=red
        textsurface = comic_sans_p.render(('Time left: '+str(timeleft)+"s"), False, timeleft_color)
        textbox = textsurface.get_rect()
        textbox.centerx = 550
        textbox.centery = 30
        screen.blit(textsurface,textbox)
        if user_entry==corr_answer:
            correct=True
        if correct:
            screen_now="correct"
        elif timeleft==0:
            print("Time is up!")
            screen_now="times_up"
    elif scr=="correct":
        textsurface = comic_sans_h2.render('You completed', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 50
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_h2.render(('Level '+str(difficulty)+"!"), False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 110
        screen.blit(textsurface,textbox)
        timetaken=round(timetaken,1)
        textsurface = comic_sans_p.render(('Time taken: '+str(timetaken)+"s"), False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 200
        screen.blit(textsurface,textbox)
        if difficulty!=10:
            button = pygame.draw.rect(screen, white, (225,290,250,60))
            textsurface = comic_sans_h3.render('Next Level', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 317
            screen.blit(textsurface,textbox)
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, lightgray, (225,290,250,60))
                textsurface = comic_sans_h3.render('Next Level', False, black)
                textbox = textsurface.get_rect()
                textbox.centerx = 350
                textbox.centery = 317
                screen.blit(textsurface,textbox)
        else:
            textsurface = comic_sans_h3.render("Congratulations on completing the game!", False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 250
            screen.blit(textsurface,textbox)
            button = pygame.draw.rect(screen, white, (225,290,250,60))
            textsurface = comic_sans_h3.render('Main Menu', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 317
            screen.blit(textsurface,textbox)
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, lightgray, (225,290,250,60))
                textsurface = comic_sans_h3.render('Main Menu', False, black)
                textbox = textsurface.get_rect()
                textbox.centerx = 350
                textbox.centery = 317
                screen.blit(textsurface,textbox)
    elif scr=="times_up":
        textsurface = comic_sans_h2.render('You ran out of time!', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 50
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_h2.render("Better luck next time...", False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 110
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_p.render("The correct answer was \""+corr_answer+"\"", False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 200
        screen.blit(textsurface,textbox)
        
        button = pygame.draw.rect(screen, white, (225,290,250,60))
        textsurface = comic_sans_h3.render('Main Menu', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 317
        screen.blit(textsurface,textbox)
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (225,290,250,60))
            textsurface = comic_sans_h3.render('Main Menu', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 317
            screen.blit(textsurface,textbox)
    elif scr=="credits":
        textsurface = comic_sans_h1.render('Credits', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 30
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_h3.render('Game Programming', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 90
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_p.render('YJJcoolcool', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 120
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_h3.render('Music', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 170
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_p.render('"Fluffing a Duck" by Kevin Macleod', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 200
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_p.render('All Images are taken from Google under', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 250
        screen.blit(textsurface,textbox)
        textsurface = comic_sans_p.render('the "Labelled for Reuse" filter.', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 275
        screen.blit(textsurface,textbox)
        button = pygame.draw.rect(screen, white, (225,320,250,60))
        textsurface = comic_sans_h3.render('Main Menu', False, black)
        textbox = textsurface.get_rect()
        textbox.centerx = 350
        textbox.centery = 347
        screen.blit(textsurface,textbox)
        if button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, lightgray, (225,320,250,60))
            textsurface = comic_sans_h3.render('Main Menu', False, black)
            textbox = textsurface.get_rect()
            textbox.centerx = 350
            textbox.centery = 347
            screen.blit(textsurface,textbox)
    else:
        screen_now="main-menu"
            

def click(mouse_x,mouse_y):
    global screen_now,difficulty,crashed,newround,showhint
    if screen_now=="main-menu":
        if 225<=mouse_x<=225+250 and 170<=mouse_y<=170+60:
            screen_now="play"
            difficulty=1
            newround=True
        elif 225<=mouse_x<=225+250 and 250<=mouse_y<=250+60:
            screen_now="credits"
        elif 225<=mouse_x<=225+250 and 330<=mouse_y<=330+60:
            crashed=True
    elif screen_now=="times_up":
        if 225<=mouse_x<=225+250 and 290<=mouse_y<=290+60:
            screen_now="main-menu"
    elif screen_now=="play":
        if 30<=mouse_x<=30+130 and 10<=mouse_y<=10+50:
            showhint=True
        else:
            if showhint:
                showhint=False
    elif screen_now=="correct":
        if 225<=mouse_x<=225+250 and 290<=mouse_y<=290+60 and difficulty!=10:
            screen_now="play"
            newround=True
            difficulty+=1
        elif 225<=mouse_x<=225+250 and 290<=mouse_y<=290+60:
            screen_now="main-menu"
    elif screen_now=="credits":
        if 225<=mouse_x<=225+250 and 290<=mouse_y<=290+60:
            screen_now="main-menu"

disallow_keys=["escape","tab","shift","return","space"]
def key_pressed(key):
    global screen_now,user_entry
    print(key)
    if screen_now=="play":
        if key.isalpha() and not(key in disallow_keys):
            if key=="backspace":
                user_entry=user_entry[:-1]
            else:
                user_entry+=str(key).upper()
        if key=="space":
            user_entry+=" "
        print("User answer: "+user_entry)
        







while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            mouse_x = int(mouse[0])
            mouse_y = int(mouse[1])
            click(mouse_x,mouse_y)
        if event.type == pygame.KEYDOWN:
            key_pressed(pygame.key.name(event.key))
    loadScreen(screen_now)
    
    clock.tick(20)
    pygame.display.update()
    updateFontSize()
    screen.fill(skyblue)
pygame.quit()
print("Program ended. Goodbye!")
os._exit(0)
