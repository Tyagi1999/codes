import pygame
import time
import random
from pygame import mixer
pygame.init()
mixer.init()
#crash_sound=pygame.mixer.Sound("crash1.wav")
pygame.mixer.music.load("route.mp3")

display_height=650
display_width=600
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
green=(0,200,0)
blue=(0,0,255)
block_color=(53,115,255)
car_width=75
block_color_list=[black,red,green,blue,white]
image=pygame.image.load("mycar3.png")
my_car_list=['mycar1.png','mycar2.png','mycar3.png']
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("LET'S RACE")
clock=pygame.time.Clock()
carImg=pygame.image.load(random.choice(my_car_list))
pygame.display.set_icon(image)

pause=False
#crash=True

def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("SCORE: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    font1=pygame.font.SysFont(None,18)
    text1=font1.render("Pause the game by pressing key P",True,green)
    gameDisplay.blit(text1,(0,30))
    
    
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,random.choice(block_color_list),[thingx,thingy,thingw,thingh])
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    
def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
    
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def crash():
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)
    
    largeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect=text_objects("Crashed",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        
        button("Play again",150,450,110,50,green,bright_green,game_loop)
        button("QUIT!",365,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
    message_display("You are crashed!!")

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
           pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
           if click[0]==1 and action!=None:
               action()
               #if action=="play":
                #   game_loop()
               #elif action=="quit":
                #   pygame.quit()
                 #  quit()
               
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
    smallText=pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
            
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    

def paused():
    pygame.mixer.music.pause()
    largeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect=text_objects("Paused",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("QUIT!",365,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText=pygame.font.Font('freesansbold.ttf',50)
        TextSurf,TextRect=text_objects("LET'S  RACE",largeText)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("GO!",120,450,100,50,green,bright_green,game_loop)
        button("QUIT!",390,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        font2=pygame.font.SysFont(None,20)
        text2=font2.render("created by ADARSH TYAGI",True,red)
        gameDisplay.blit(text2,(20,15))
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=5
    thing_width=100
    thing_height=100
    thingCount=1
    dodged=0
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                
        x+=x_change            
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,random.choice(block_color_list))
        things(thing_startx,thing_starty,thing_width,thing_height,random.choice(block_color_list))
        thing_starty+=thing_speed
        car(x,y)
        things_dodged(dodged)
    
        if x>display_width-car_width or x<0:
            crash()
        
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            thing_speed+=1
            thing_width+=(dodged*1.05)
            
        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash()
                
        
        pygame.display.update()
        clock.tick(60)
game_intro()        
game_loop()    
pygame.quit()
quit()
    







