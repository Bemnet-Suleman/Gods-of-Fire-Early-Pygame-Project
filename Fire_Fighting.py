import pygame
from pygame.locals import *
from sys import exit
from time import sleep,time
import datetime
import random
pygame.init()
Window_size=(1500,700)
screen=pygame.display.set_mode(Window_size,pygame.SCALED|pygame.FULLSCREEN)
pygame.display.set_caption("GodsOfFire")
pygame.display.set_icon(pygame.image.load(r"C:\Users\Bemnet\Documents\Documents\Pydroid3\Game\Images\Yonatan\Attacks\ei_1700659272295-removebg-preview.png"))
clock=pygame.time.Clock()
pygame.mixer.pre_init(44100,-16,2,512)
GameDir=r"C:\Users\Bemnet\Documents\Documents\Pydroid3\Game\\"
map1=GameDir+"Game_map.txt"
map2=GameDir+""
map3=GameDir+""
map4=GameDir+""
images=GameDir+"Images/"
Sounds=GameDir+"Sounds/"
Yon=images+"Yonatan/Walk/"
Yon_a=images+"Yonatan/Attacks/"
En1=images+"Enemy/Abel/Walk/"
En1_a=images+"Enemy/Abel/Attacks/"
En2=images+"Enemy/Sami/Walk/"
En2_a=images+"Enemy/Sami/Attacks/"
En3=images+"Enemy/Piter/Walk/"
En3_a=images+"Enemy/Piter/Attacks/"
bg=images+"Background/"
MENU=images+"Controls/Menu/"
buttons=images+"Controls/buttons/"

Yon=[pygame.image.load(Yon+"Standing.png").convert_alpha(),pygame.image.load(Yon+"W2.png").convert_alpha(),pygame.image.load(Yon+"W3.png").convert_alpha(),pygame.image.load(Yon+"W4.png").convert_alpha(),pygame.image.load(Yon+"W6.png").convert_alpha(),pygame.image.load(Yon+"W7.png").convert_alpha(),pygame.image.load(Yon+"W8.png").convert_alpha(),pygame.image.load(Yon+"W9.png").convert_alpha()]

BG=[pygame.image.load(bg+"Volcanic.jpg").convert_alpha(),pygame.image.load(bg+"Land1.jpg").convert_alpha(),pygame.image.load(bg+"Lava.jpg").convert_alpha(),pygame.image.load(bg+"Dark1.jpg").convert_alpha(),pygame.image.load(bg+"ground.png").convert_alpha(),pygame.image.load(bg+"Dirt1.png").convert_alpha(),pygame.image.load(bg+"Freezed.jpg").convert_alpha(),pygame.image.load(bg+"Mountains.jpg").convert_alpha(),pygame.image.load(bg+"Forest.jpg").convert_alpha(),pygame.image.load(bg+"Volcanic1.jpg").convert_alpha(),pygame.image.load(bg+"Water.jpg").convert_alpha(),pygame.transform.scale(pygame.image.load(bg+"ground.png").convert_alpha(),(120,90))]
OBJ=[pygame.image.load(bg+"Hazard.png").convert_alpha(),pygame.image.load(bg+"Beach.png").convert_alpha(),pygame.image.load(bg+"Pyramid.png").convert_alpha(),pygame.image.load(bg+"Tree.png").convert_alpha(),pygame.image.load(bg+"Volcano.png").convert_alpha(),pygame.image.load(bg+"Water.png").convert_alpha(),pygame.image.load(bg+"Crystal.png").convert_alpha(),pygame.image.load(bg+"Crystal1.png").convert_alpha(),pygame.image.load(bg+"Mountain.png").convert_alpha(),pygame.image.load(bg+'smoke.png').convert_alpha()]
MN=[pygame.image.load(MENU+"Tech.jpg").convert_alpha(),pygame.image.load(MENU+"Menubg.jpg").convert_alpha(), pygame.image.load(MENU+"Firebg.jpg"). convert_alpha(),pygame.image.load(MENU+"Sticker.png")]

bt=[pygame.image.load(images+"Controls/buttons/Button1.png").convert_alpha(),pygame.image.load(images+"Controls/buttons/Button2.png").convert_alpha(),pygame.image.load(buttons+"On.png").convert_alpha(),pygame.image.load(buttons+"Off.png").convert_alpha(),pygame.image.load(buttons+"Play.jpg").convert_alpha(),pygame.image.load(buttons+"Right.png").convert_alpha(),pygame.image.load(buttons+"Options.png").convert_alpha()]

BT=[]
x=0
for btn in bt:
    if x>2:
        BT.append(btn)
    else:
        BT.append(pygame.transform.scale(btn,(600,100)))
    x+=1
BGD=[pygame.image.load(bg+"Jungle.jpg").convert_alpha()]

WEnemy=[[pygame.image.load(En1+"Ft.png").convert_alpha(),pygame.image.load(En1+"St.png").convert_alpha(),pygame.image.load(En1+"W1.png").convert_alpha(),pygame.image.load(En1+"W2.png").convert_alpha(),pygame.image.load(En1+"W3.png").convert_alpha(),pygame.image.load(En1+"W4.png").convert_alpha(),pygame.image.load(En1+"W5.png").convert_alpha(),pygame.image.load(En1+"W6.png").convert_alpha(), pygame.image.load(En1+"W8.png").convert_alpha(),pygame.image.load(En1+"W9.png").convert_alpha()],[pygame.image.load(En1_a+"S1.png").convert_alpha(),pygame.image.load(En1_a+"S2.png").convert_alpha(),pygame.image.load(En1_a+"D.png").convert_alpha(),pygame.image.load(En1_a+"Hit.png").convert_alpha(),pygame.image.load(En1_a+"Hit.png").convert_alpha()],[pygame.image.load(En1_a+"P1.png").convert_alpha(),pygame.image.load(En1_a+"P2.png").convert_alpha(),pygame.image.load(En1_a +"P3.png").convert_alpha(),pygame.image.load(En1_a+"P4.png").convert_alpha()]]
WEnemy1=[[],[],[]]
WEnemy1L=[[],[],[]]
for enemy in WEnemy[0]:
    WEnemy1[0].append(enemy)
    WEnemy1[0].append(enemy)
for enemy in WEnemy[1]:
    WEnemy1[1].append(enemy)
    WEnemy1[1].append(enemy)
    WEnemy1[1].append(enemy)
for enemy in WEnemy[2]:
    WEnemy1[2].append(enemy)
    WEnemy1[2].append(enemy)
    WEnemy1[2].append(enemy)
for img in WEnemy1[0]:
    WEnemy1L[0].append(pygame.transform.flip(img,True,False))
for img in WEnemy1[1]:
    WEnemy1L[1].append(pygame.transform.flip(img,True,False))
for img in WEnemy1[2]:
    WEnemy1L[2].append(pygame.transform.flip(img,True,False))
WEnemy2=[[pygame.image.load(En2+"W1.png").convert_alpha(),pygame.image.load(En2+"W2.png").convert_alpha(),pygame.image.load(En2+"W3.png").convert_alpha(),pygame.image.load(En2+"W4.png").convert_alpha(),pygame.image.load(En2+"W5.png").convert_alpha(),pygame.image.load(En2+"W6.png").convert_alpha(),pygame.image.load(En2+"W7.png").convert_alpha(),pygame.image.load(En2+"W8.png").convert_alpha()],[]]

WEnemy2L=[[]]
for img in WEnemy2[0]:
    WEnemy2L[0].append(pygame.transform.flip(img,True,False))
WEnemy3=[[pygame.image.load(En3+"W1.png").convert_alpha(),pygame.image.load(En3+"W2.png").convert_alpha(),pygame.image.load(En3+"W3.png").convert_alpha(),pygame.image.load(En3+"W4.png").convert_alpha(),pygame.image.load(En3+"W5.png").convert_alpha(),pygame.image.load(En3+"W6.png").convert_alpha(),pygame.image.load(En3+"W7.png").convert_alpha(),pygame.image.load(En3+"W8.png").convert_alpha(), pygame.image.load(En3+"W9.png").convert_alpha(),pygame.image.load(En3+"W10.png").convert_alpha()],[]]

WEnemy3L=[[]]
for img in WEnemy3[0]:
    WEnemy3L[0].append(pygame.transform.flip(img,True,False))

Control_imgs=[pygame.image.load(images+"Controls/buttons/circle3.png").convert_alpha(),pygame.image.load(images+"Controls/buttons/But1.png").convert_alpha(),pygame.image.load(images+"Controls/buttons/Right.png").convert_alpha(),pygame.image.load(images+"Controls/buttons/Jump.png").convert_alpha(),pygame.image.load(images+"Controls/buttons/Circle2.png").convert_alpha(), pygame.transform.scale(pygame.image.load(images+"Controls/buttons/fireball.png"),(100,100)).convert_alpha(),pygame.transform.scale(pygame.image.load (images+"Controls/buttons/But2.png"),(100,100)).convert_alpha(),pygame.transform.scale(pygame.image.load (images+"Controls/buttons/Circle.png"),(100,100)).convert_alpha(),pygame.image.load (images+"Controls/buttons/Circle6.jpg").convert_alpha(),pygame.image.load(images+"Controls/buttons/Settings.png").convert_alpha()]
def load_map(level):
   Game_map=[]
   with open(level,"r") as map:
      for row in map.read().split("\n"):
        Game_map.append(list(row))
   return Game_map
Yon_as=[[pygame.image.load(Yon_a+"P6.png").convert_alpha(),pygame.image.load(Yon_a+"P7.png").convert_alpha(),pygame.image.load(Yon_a+"P12.png").convert_alpha(),pygame.image.load(Yon_a+"P12.png").convert_alpha(),pygame.image.load(Yon_a+"Leg5.png").convert_alpha()],[pygame.image.load(Yon_a+"Leg5.png").convert_alpha(),pygame.image.load(Yon_a+"Leg4.png").convert_alpha(),pygame.image.load(Yon_a+"Leg3.png").convert_alpha(),pygame.image.load(Yon_a+"Leg2.png").convert_alpha()],[pygame.image.load(Yon_a+"Blast1.png").convert_alpha(),pygame.image.load(Yon_a+"Blast2.png").convert_alpha(),pygame.image.load(Yon_a+"Blast3.png").convert_alpha(),pygame.image.load(Yon_a+"Blast4.png").convert_alpha(),pygame.image.load(Yon_a+"Blast5.png").convert_alpha(),pygame.image.load(Yon_a+"Blast6.png").convert_alpha()],[pygame.image.load(Yon_a+"Big1.png").convert_alpha(),pygame.image.load(Yon_a+"Big2.png").convert_alpha(),pygame.image.load(Yon_a+"Big3.png").convert_alpha(),pygame.image.load(Yon_a+"Big4.png").convert_alpha(),pygame.image.load(Yon_a+"Big5.png").convert_alpha()],[pygame.image.load(Yon_a+"Leg5.png")],[pygame.image.load(Yon_a+"Trans.png").convert_alpha(),pygame.image.load(Yon_a+"Trans.png").convert_alpha(),pygame.image.load(Yon_a+"Trans.png").convert_alpha(),pygame.image.load(Yon_a+"Trans.png").convert_alpha(),pygame.image.load(Yon_a+"Trans.png").convert_alpha()]]
sound_effects=[[pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bomb.wav"),pygame.mixer.Sound(Sounds+"dramatic.mp3"),pygame.mixer.Sound(Sounds+"mission.mp3")],[pygame.mixer.Sound(Sounds+"fire_whoosh.wav"),pygame.mixer.Sound(Sounds+"fireball.mp3"),pygame.mixer.Sound(Sounds+"fireballspell.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav")],[pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav")],[pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav"),pygame.mixer.Sound(Sounds+"bonus.wav")]]
En_attacks=[]
controls=[]
YON_R=[]
for img in Yon:
    YON_R.append(img)
    YON_R.append (img)
YON_L=[]

for img in YON_R:
   YON_L.append(pygame.transform.flip(img,True,False))
Yon_attacks=[]
Yon_attacks1=[]
Yon_attacks2=[]
Yon_attacks3=[]
Yon_attacks4=[]
Yon_attacks1L=[]
Yon_attacks2L=[]
Yon_attacks3L=[]
Yon_attacks4L=[]
Yon_attacksL=[]
for yon in Yon_as[0]:
   Yon_attacks.append(yon)
   Yon_attacksL.append(pygame. transform.flip(yon,True,False))
for yon in Yon_as[1]:
   Yon_attacks1.append(yon)
   Yon_attacks1.append(yon)
   Yon_attacks1L.append(pygame. transform.flip(yon,True,False))
   Yon_attacks1L.append(pygame. transform.flip(yon,True,False))
for yon in Yon_as[2]:
   Yon_attacks2.append(yon)
   Yon_attacks2.append(yon)
   Yon_attacks2L.append(pygame. transform.flip(yon,True,False))
   Yon_attacks2L.append(pygame. transform.flip(yon,True,False))
for yon in Yon_as[3]:
   Yon_attacks3.append(yon)
   Yon_attacks3L.append(pygame. transform.flip(yon,True,False))
   Yon_attacks3.append(yon)
   Yon_attacks3L.append(pygame. transform.flip(yon,True,False))
for yon in Yon_as[4]:
   Yon_attacks4.append(yon)
   Yon_attacks4L.append(pygame. transform.flip(yon,True,False))
class StartMenu(pygame.sprite.Sprite):
   def __init__(self,width, height):
      super().__init__()
      self.width=width
      self.height=height
      self.win=pygame.Surface((1500,700))
      self.image=self.win
      self.rect=self.image.get_rect()
      self.play=False
      self.Welcome()
   def Welcome(self):
     self.sounds=[pygame.mixer.music.load(Sounds+"50.mp3"),pygame.mixer.Sound(Sounds+"bonus.wav")]
     self.sounds[1].set_volume(0.01)
     pygame.mixer.music.play(-1)
     blue=(0,150,200)
     red=(205,0,0)
     self.load=pygame.Rect((self.rect.left,self.rect.bottom-20),(100,20))
     font=pygame.font.SysFont("impact",110)
     text1=font.render("Gods of Fire",True,red)
     text2=font.render("Touch anywhere to start !",True,red)
     textRect=text1.get_rect()
     textRect2=text2.get_rect()
     textRect.center,textRect2.centerx,textRect2.bottom=self.rect.center,self.rect.centerx,self.rect.bottom-self.rect.height*0.1
     textIcon=pygame.image.load(MENU+"Bifire.jpg")
     textIcon1=pygame.image.load(MENU+"Icon.jpg")
     textIcon2=pygame.image.load(MENU+"BfireBlast.png")
     IconRect=textIcon.get_rect()
     textIc1=textIcon1.get_rect()
     textIc2=textIcon2.get_rect()
     IconRect.centerx,textIc1.topleft,textIc2.topright=self.rect.centerx,self.rect.topleft,self.rect.topright
     self.win.blit(text1,textRect)
     self.win.blit(text2,textRect2)
     self.win.blit(textIcon,IconRect)
     self.win.blit(textIcon1,textIc1)
     self.win.blit(textIcon2,textIc2)
class MainMenu(pygame.sprite.Sprite):
   def __init__(self,width,height):
      super().__init__()
      self.width=width
      self.height=height
      self.image=pygame.transform.scale(BG[6],(self.width, self.height))
      self.csurface=pygame.transform.scale(MN[0],(round(self.width*0.7), round(self.height*0.7)))
      self.rect=self.image.get_rect()
      self.loading=sound_effects[0][random.randint(2,3)]
   def Menu(self):
      bar1=pygame.transform.scale(MN[1],(400,80))
      bar2=BT[0]#bt1
      bar3=BT[1]#bt2
      bar4=BT[2]#on
      bar5=BT[3]#off
      bar6=BT[4]#play
      bar7=BT[5]#r
      bar8=BT [6]#opt
      bar_rect1=bar1.get_rect()
      bar_rect1.center=(self.rect.center[0],20)
      self.textRect1=bar1.get_rect()
      self.textRect2=bar7.get_rect()
      self.textRect3=bar3.get_rect()
      self.textRect4=bar4.get_rect()
      self.textRect5=bar1.get_rect()
      self.textRect6=bar1.get_rect()
      self.textRect7=bar1.get_rect()
      self.textRect8=bar1.get_rect()
      self.font=pygame.font.SysFont("Impact",80)
      text1=self.font.render("MainMenu",True,(255,0,0))
      text2=self.font.render("Exit",True,(255,0,0) )
      text3=self.font.render("Settings",True,(255,0,0))
      text4=self.font.render("Play",True,(255,0,0))
      text5=self.font.render("About",True,(255,0,0))
      text6=self.font.render("Combat",True,(255,0,0))
      text7=self.font.render("Train",True,(255,0,0))
      text8=self.font.render("Multi-player",True,(255,0,0))
      self.textRect1.center=(bar_rect1.center[0]+75,bar_rect1.center[1]+10)
      self.textRect2.topright=self.rect.topright
      self.textRect3.center=(self.rect.center[0]-100,self.rect.center[1]-100)
      self.textRect4.bottomleft=(0,650)
      self.textRect5.bottomleft=(1300,650)
      self.textRect6.bottomleft=self.textRect3.topleft
      self.textRect7.topleft=self.textRect3.bottomleft
      self.textRect8.topleft=self.textRect7.bottomleft
      csurf_rect=self.csurface.get_rect()
      csurf_rect.center=(bar_rect1.center[0],bar_rect1.bottom+self.height*0.7//2)
      self.image.blit(self.csurface,csurf_rect)
      self.image.blit(bar1,bar_rect1)
      self.image.blit(bar7,self.textRect2)
      self.image.blit(bar2,(self.textRect3[0]-80,self.textRect3[1]-20))
      self.image.blit(bar6,(self.textRect4[0]+120,self.textRect4[1]))
      self.image.blit(bar2,(self.textRect6[0]-80,self.textRect6[1]-20))
      self.image.blit(bar2,(self.textRect7[0]-80,self.textRect7[1]-20))
      self.image.blit(bar2,(self.textRect8[0]-80,self.textRect8[1]-20))
      self.image.blit(text1,self.textRect1)
      self.image.blit(text2,(self.textRect2[0]-110,self.textRect2[1]+10))
      self.image.blit(text3,self.textRect3)
      self.image.blit(text4,self.textRect4)
      self.image.blit(text5,self.textRect5)
      self.image.blit(text6,self.textRect6)
      self.image.blit(text7,self.textRect7)
      self.image.blit(text8,self.textRect8)
class Fire(pygame.sprite.Sprite):
    def __init__(self,pos,image,direction):
        super().__init__()
        self.pos=pos
        self.image=image
        self.direction=direction
        self.rect=self.image.get_rect()
    def update(self):
        if self.rect[0]<Game.width and not self.rect[0]<-Game.width:
           screen.blit(self.image,self.rect)
    def draw(self):
           self.pos[0]+=80*self.direction
           self.rect.center=self.pos
    def check_hit(self,rect):
        if self.rect[0] in range(Game.width):
         if self.rect.colliderect(rect):
             self.kill()
             self.remove()
             return True
         return False 
class MainGame():
   def __init__(self,width,height):
      super().__init__()
      self.scroll=[0,0]
      self.width=width
      self.height=height
      self.music=pygame.mixer.Sound(Sounds+"bomb.wav")
      self.menu=MainMenu(int(1500*0.9),int(700*0.9))
      self.t=time()
      self.tiles=[]
      self.wtiles=[]
      self.image=pygame.Surface((self.width,self.height))
      self.rect=self.image.get_rect()
      self.Generate_bg ()
      self.gameover=False   
   def FPS(self):
      self.dt=time()-self.t
      self.dt*=30
      self.t=time()
      font=pygame.font.SysFont("Impact",50)
      text=font.render(f"{int(clock.get_fps())}"+"FPS",True, (255,0,0))
      text_rect=text.get_rect()
      screen.blit(text,text_rect)
   def timer(self,sec,function):
       ctime_in_sec=datetime.datetime.now().second
       if  ctime_in_sec!=10:
           function()   
   def swap(self,surf,col):
       back=pygame.Surface(surf.get_size())
       back.fill(col)
       surf.set_alpha(100)
       back.blit(surf,(0,0))
       return back
   def Anime(self,img,img_dur=5,loop=True):
       done=False
       frame=0
       if loop:
           frame=(frame+1)%(img_dur*len(img))
       else:
           frame=min(frame+1,img_dur*len(img)-1)
           if frame>=img_dur*len(img)-1:
               done=True
           if done:
              frame=0
       self.cur_anime=pygame.transform.scale(img[frame//img_dur],(img[frame//img_dur].get_width(),img[frame//img_dur]. get_height()+random.randint(0,20)))
       return self.cur_anime
   def Generate_bg(self):
           self.image.blit(pygame.transform.scale(BGD[0],(self.width,self.height)),(0,0))
   def env(self,map):
      self.tiles=[]
      y=0
      for row in map:
         x=0
         for tile in row:
              if x*200-self.scroll[0]<Game.width and not x*200-self.scroll[0]<-Game.width:
                loc=(x*200-self.scroll[0],y*64-self.scroll[1])
                rectloc=(x*200,y*64,200,64)
                if tile=="b":
                   screen.blit(BG[5],loc)
                   self.tiles.append(pygame.Rect(rectloc))
                if tile=="c":
                   screen.blit(BG[4],loc)
                if tile=="d":
                    screen.blit(BG[-1],(loc[0]+100,loc[1]-200))
                    self.tiles.append(pygame.Rect(x*200+100,y*64-200,120,120))
                if tile=="w":
                    BG[10].set_alpha(110)
                    screen.blit(BG[10],loc)
                    self.wtiles.append(pygame.Rect(rectloc))
              x+=1
         y+=1
   def collission_test(self,rect,tiles):
       collided=[]
       for tile in tiles:
          if rect.colliderect(tile):
              collided.append(tile)
       return collided
   def move(self,rect,tiles,mvnt):
      collission_types={"top":False,"bottom":False,"left":False,"right":False}
      rect.x+=mvnt[0]
      hit_list=self.collission_test(rect,tiles)
      for tile in hit_list:
               if mvnt[0] > 0:
                  rect.right=tile.left
                  collission_types["right"]=True
                  collission_types["left"]=False
               if mvnt[0] < 0:
                  rect.left=tile.right
                  collission_types["left"]=True
                  collission_types["right"]=False
      rect.y+=mvnt[1]
      hit_list=self.collission_test(rect,tiles)
      for tile in hit_list:
               if mvnt[1] >0:
                  mvnt[1]=0
                  rect.bottom=tile.top
                  collission_types["bottom"]=True
               if mvnt[1] <0:
                  rect.top=tile.bottom
                  collission_types["top"]=True
      return rect ,collission_types
   def GameOver(self):
       surface=pygame.Rect((200,100),(900,500))
       font=pygame.font.SysFont("Impact ",120)
       font1=pygame.font.SysFont("Impact ",70)
       text1=font.render("Game Over !",True, (0,0,0))
       text2=font.render("You have dead",True, (0,0,91))
       text3=font1.render("Restart",True,(0,255,0),(0,0,0))
       text4=font1.render("MainMenu",True,(255,0,0),(0,0,91))
       textRect1=text1.get_rect()
       textRect2=text2.get_rect()
       self.textRect3=text3.get_rect()
       self.textRect4=text4.get_rect()
       textRect1.bottomleft=surface.topleft
       textRect2.center=surface.center
       self.textRect4.bottomright=surface.bottomright
       self.textRect3.bottomleft=surface.bottomleft
       pygame.draw.rect(screen,(200,200,200),surface)
       screen.blit(pygame.transform.scale (MN[3],(500,200)),(textRect2.center[0]-250,textRect2.top-75))
       screen.blit(text1,textRect1)
       screen.blit(text2,textRect2)
       screen.blit(text3,self.textRect3 )
       screen.blit(text4,self.textRect4)
class Controls(object):
    def __init__(self,surf):
      self.surf=surf
      self.showmenu=False
      self.circle1=Control_imgs[0]
      self.cslide=Control_imgs[1]
      self.cjump=Control_imgs[3]
      self.life=pygame.rect.Rect(0,0,500,50)
      self.power=pygame.rect.Rect(0,50,400,50)
      self.fist=Control_imgs[4]
      self.attack1=Control_imgs[5]
      self.attack2=Control_imgs[6]
      self.attack3=Control_imgs[7]
      self.mbtn=Control_imgs[9]
      self.crect1=self.circle1.get_rect()
      self.cslide_rect=self.cslide.get_rect()
      self.cjump_rect=self.cjump.get_rect()
      self.fist_rect=self.fist.get_rect()
      self.mbtn_rect=self.mbtn.get_rect()
      self.at1=self.attack1.get_rect()
      self.at2=self.attack2.get_rect()
      self.at3=self.attack3.get_rect()
      self.mbtn_rect.center=(1400,30)
      self.slide_area=pygame.Rect((0,260),Window_size)
      self.crect1.top,self.crect1.left=420,50
      self.cslide_rect.center=self.crect1.center
      self.topb=pygame.Rect(self.crect1.left,self.crect1.top-100,self.crect1.width+20,20)
      self.bottomb=pygame.Rect(self.crect1.left,self.crect1.bottom+50,self.crect1.width+20,20)
      self.rightb=pygame.Rect(self.crect1.right,self.crect1.top,20,self.crect1.height)
      self.leftb=pygame.Rect(self.crect1.left,self.crect1.top,20,self.crect1.height)
      self.fist_rect.center=(1350,550)
      self.at1.center=(self.fist_rect.center[0],self.fist_rect.top-50)
      self.at2.center=(self.fist_rect.left-40,self.fist_rect.top+15)
      self.at3.center=(self.fist_rect.left-50,600)
      self.cjump_rect.center=(self.at3.left-50,self.at3.y+20)
    def draw(self,surf):
      surf.blit(self.circle1 ,self.crect1)
      surf.blit(self.cslide,self.cslide_rect)
      surf.blit(self.cjump,self.cjump_rect)
      surf.blit(self.fist,self.fist_rect)
      surf.blit(self.attack1,self.at1)
      surf.blit(self.attack2, self.at2)
      surf.blit(self.attack3,self.at3)
      surf.blit(self.mbtn,self.mbtn_rect)
Game=MainGame(1500,700)
class Player():
   def __init__(self,width,height):
      super().__init__()
      self.width=width
      self.height=height
      self.right, self.left,self.wright,self.wleft,self.at,self.at1,self.at2,self.at3,self.in_water=False,False, False,False,False,False,False,False,False
      self.life=600
      self.power=400
      self.vel=25
      self.gravity=9.8
      self.count=1
      self.jump_count=0
      self.pos=[500,250]
      self.mvnt=[0,0]
      self.yon=YON_R[self.count]
      self.YON_Rect=pygame.Rect(self.pos[0],self.pos[1],self.yon.get_width(),self.yon.get_height())
      self.fireballs=pygame.sprite.Group()
   def get_rect(self):
      self.player_rect,self.collissions=Game.move(self.YON_Rect,Game.tiles,self.mvnt)
      self.hit_rect=pygame.Rect(self.player_rect.x-Game.scroll[0],self.player_rect.y-Game.scroll[1],self.yon.get_width(),self.yon.get_height())
      self.life_outrect=pygame.Rect(110,5,605,30)
      self.life_inrect=pygame.Rect(112,10,600,20)
      self.power_outrect=pygame.Rect(110,40,405,20)
      self.power_inrect=pygame.Rect(112,45,400,10)
      if self.wleft:
          player.hit_rect.x=player.player_rect.left-Game.scroll[0]-50
      if self.wright:
          player.hit_rect.x=player.player_rect.right-Game.scroll[0]
   def update(self):
       self.in_water=False
       self.yon.set_alpha(255)
       self.life_inrect.width=self.life
       self.power_inrect.width=self.power
       pygame.draw.rect(screen,(0,255,0),self.power_outrect,width=4)
       pygame.draw.rect(screen,(255,255,0),self.power_inrect)
       pygame.draw.rect(screen,(0,0,0),self.life_outrect,width=4)
       pygame.draw.rect(screen,(255,0,0),self.life_inrect)
       for ball in self.fireballs:
                 ball.draw()
                 ball.update()
                 ball.rect.y=ball.rect.y+Game.scroll[1]
       if self.life<=0:
           Game.gameover=True
       if self.collissions["bottom"]:
           self.gravity=0
           self.jump_count=0
       else:
           self.gravity+=0.5
       for water in Game.wtiles:
          if self.player_rect.colliderect(water):
              self.life-=0.0025
              self.in_water=True
              self.yon.set_alpha(100)
       screen.blit(self.yon,[self.player_rect.x-Game.scroll[0],self.player_rect.y-Game.scroll[1]])
      
   def walk(self):
      self.mvnt[0]=0
      self.mvnt[1]+=self.gravity
      if  self.right :
         if not self.in_water:
             self.count+=1
             if self.count>=len(YON_R):
                self.count=2
             self.mvnt[0]+=self.vel*Game.dt
             self.yon=YON_R[self.count]
         if self.in_water:
             self.yon=pygame.transform.rotate(YON_R[0],-90)
             self.mvnt[0]+=self.vel*Game.dt
         self.hit_rect.x=self.player_rect.right-Game.scroll[0]
      if self.left:
         if not self.in_water:
             self.count+=1
             if self.count>=len(YON_L):
                self.count=2
             self.mvnt[0]-=self.vel*Game.dt
             self.yon=YON_L[self.count]
         if self.in_water:
             self.yon=pygame.transform.rotate(YON_L[0],90)
             self.mvnt[0]-=self.vel*Game.dt
         self.hit_rect.x=self.player_rect.left-Game.scroll[0]-50
   def jump(self):
        if self.jump_count<3:
            start.sounds[1].play()
            self.mvnt[1]-=self.mvnt[1]+60
            if self.right:
                self.mvnt[0]+=2
            if self.left:
                self.mvnt[0]-=2
        else:
            self.mvnt[1]=0
   def attack(self):
       self.power-=10
       self.at=True
       self.count+=1
       if self.count>=len(Yon_attacks):
          self.count=0
       if self.wright:
          self.yon=Yon_attacks[self.count]
       if self.wleft:
           self.yon=Yon_attacksL[self.count]
   def attack1(self):
         if self.at1:
             self.count+=1
             if self.count<len(Yon_attacks1):
               if self.wright:
                  if self.count==5:
                      self.fireballs.add(Fire([self.player_rect.right-Game.scroll[0],self.player_rect.centery-Game.scroll[1]],Yon_as[5][0],1))
                      self.power-=25
                  self.yon=Yon_attacks1[self.count]
               if self.wleft:
                  self.yon=Yon_attacks1L[self.count]
                  if self.count==5:
                      self.fireballs.add(Fire([self.player_rect.left-Game.scroll[0],self.player_rect.centery-Game.scroll[1]],pygame.transform.flip(Yon_as[5][0],True,False),-1))
                      self.power-=25
             else:
                 self.at1=False
                 self.count=0
                 if self.wright:
                      self.yon=YON_R[0]
                 if self.wleft:
                      self.yon=YON_L[0]
   def attack2(self):
       pass
   def attack3(self):
       pass
class Enemy1(pygame.sprite.Sprite):
        def __init__(self,pos,size,level,player):
            super().__init__()
            self.player=player
            self.pos=pos
            self.size=size
            self.level=level
            self.walking=1
            self.left,self.right,self.stand,self.span=False,False,False,True
            self.count=4
            self.fire_hit,self.fist_hit,self.mid_hit,self.hd_hit=10,5,25,50
            self.vel=10
            self.mvnt=[0,0]
            self.image=WEnemy1L[0][self.count]
            self.idle=[WEnemy1L[0][4] for _ in range(40)]
            self.rect=pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
            self.life=100
        def update(self):
          self.rect,self.collissions=Game.move(self.rect,Game.tiles, self.mvnt)
          self.hit_rect=pygame.Rect(self.rect[0]-Game.scroll[0],self.rect.centery-Game.scroll[1],50,50)
          self.span_rect=pygame.Rect(self.rect[0]-625-Game.scroll[0],self.rect.centery-40-Game.scroll[1],1250,50)
          self.life_rect=pygame.Rect(self.rect[0]-Game.scroll[0],self.rect.top-20-Game.scroll[1],self.life,10)
          if self.rect[0]<Game.width+Game.scroll[0]and self.rect[1]<Game.height+Game.scroll[1]:
            pygame.draw.rect(screen,(255,0,0),self.life_rect)
            self.mvnt[1]+=5
            spp=pygame.Rect(self.player.player_rect.x-Game.scroll[0],self.player.player_rect.y-300-Game.scroll[1],self.player.yon.get_width(),600)
            if spp.colliderect(self.span_rect):
                if self.walking:
                    self.stand=False 
                    if self.rect[0]<self.player.player_rect.x-50:
                        self.right=True
                        self.left=False
                    if self.rect[0]>self.player.player_rect.x+50:
                        self.left=True
                        self.right=False
                    self.walking=max(0,self.walking-1)
                    if self.left:
                        self.rect[0]-=self.vel 
                        self.hit_rect.x=self.rect.left-Game.scroll[0]
                        self.span_rect.x=self.rect.left-800-Game.scroll[0]
                    if self.right:
                         self.rect[0]+=self.vel 
                         self.hit_rect.x=self.rect.right-Game.scroll[0]
                         self.span_rect.x=self.rect.right+20-Game.scroll[0]
            if random.random()<0.1 and not self.walking:
                        self.count+=1 
                        self.walking=random.randint(120,240)
                        self.stand=True 
            if not spp.colliderect(self.span_rect):
                    if self.collissions["left"]:
                        self.right=True
                        self.left=False
                    if self.collissions["right"]:
                        self.left=True
                        self.right=False
                    self.walking=max(0,self.walking-1)
                    if self.left:
                        self.rect[0]-=self.vel 
                        self.hit_rect.x=self.rect.left-Game.scroll[0]
                        self.span_rect.x=self.rect.left-800-Game.scroll[0]
                    if self.right:
                         self.rect[0]+=self.vel 
                         self.hit_rect.x=self.rect.right-Game.scroll[0]
                         self.span_rect.x=self.rect.right+20-Game.scroll[0]
            if self.collissions["right"]:
                self.rect[1]-=60
                self.mvnt[0]=self.mvnt[0]+2
            if not self.collissions["right"]:
                self.mvnt[0]=self.mvnt[0]
                self.mvnt[1]=self.mvnt[1]
            if self.collissions["left"]:
                self.rect[1]-=60
                self.mvnt[0]=self.mvnt[0]-2
            for fire in player.fireballs:
                if fire.check_hit(pygame.Rect(self.rect[0]-Game.scroll[0],self.rect[1],self.rect.width,self.rect.height)):
                   self.image=Game.swap(self.image,(255,0,0))
                   self.life-=self.fire_hit
            if self.life>25 and self.life<=50:
                        self.image.set_alpha(250)
                        self.fire_hit,self.fist_hit,self.mid_hit,self.hd_hit=5,2,10,25
                        self.count=0
                        if self.left:
                            self.image=WEnemy1L[1][-7]
                        if self.right:
                            self.image=WEnemy1[1][-7]
            if self.life>0 and self.life<=25:
                self.image.set_alpha(100)
            else:
                self.image.set_alpha(255)
            if self.life<=0:
                        self.count+=1
                        if self.left:
                          if self.count>=len(WEnemy1L[1][-6:]):
                              self.count=-6
                          self.image=WEnemy1L[1][self.count]
                        if self.right:
                           if self.count>=len(WEnemy1[1][-6:]):
                              self.count=-6
                           self.image=WEnemy1[1][self.count]
                        self.kill()
                        self.remove()
            screen.blit(self.image,(self.rect[0]-Game.scroll[0],self.rect[1]-Game.scroll[1]))
        def walk(self):
           if self.count==len(WEnemy1L[0]):
               self.image=WEnemy1L[0][0]
           sp=pygame.Rect(self.player.player_rect.x-Game.scroll[0],self.player.player_rect.y-Game.scroll[1],self.player.yon.get_width(),self.player.yon.get_height())
           if self.span:
               self.count+=1
               if self.left:
                      if self.count>=len(WEnemy1L[0]):
                          self.count=4
                      self.image=WEnemy1L[0][self.count]
               if self.right:
                       if self.count>=len(WEnemy1[0]):
                          self.count=4
                       self.image=WEnemy1[0][self.count]
           if self.walking and not self.span:
                    self.count+=1
                    if self.left:
                      if self.count>=len(WEnemy1L[0]):
                          self.count=4
                      self.image=WEnemy1L[0][self.count]
                    if self.right:
                       if self.count>=len(WEnemy1[0]):
                          self.count=4
                       self.image=WEnemy1[0][self.count]
           if self.stand:
                     if self.count>=20:
                          self.count=0
                     self.image=pygame.transform.scale(self.idle[self.count ],(self.idle[self.count ]. get_width()+random.randint (0,0),self.idle[self.count].get_height()-random.randint (20,40)))
           if self.hit_rect.colliderect(sp)and self.span_rect.colliderect(self.player.hit_rect):
               self.walking,self.stand=False, False
               if self.life>0 and self.life<=25:
                    self.image.set_alpha(100)
                    self.fire_hit,self.fist_hit,self.mid_hit,self.hd_hit=10,5,25,50
                    self.count+=1
                    if self.left:
                              if self.count>=len(WEnemy1L[2]):
                                  self.count=0
                                  self.player.life-=2
                              self.image=WEnemy1L[2][self.count]
                    if self.right:
                               if self.count>=len(WEnemy1[2]):
                                  self.count=0
                                  self.player.life-=2
                               self.image=WEnemy1[2][self.count]
               if self.life>50:
                   self.image.set_alpha(255)
                   self.count+=1
                   if self.left:
                          if self.count>=len(WEnemy1L[1][0:6]):
                              self.count=0
                              self.player.life-=5
                          self.image=pygame.transform.scale(WEnemy1L[1][self.count],(WEnemy1L[1][self.count].get_width(),203))
                   if self.right:
                           if self.count>=len(WEnemy1[1][0:6]):
                              self.count=0
                              self.player.life-=5
                           self.image=pygame.transform.scale(WEnemy1[1][self.count],(WEnemy1[1][self.count].get_width(),203)) 
        def get_hit(self):
            self.hitten_rect=pygame.Rect(self.rect.x-Game.scroll[0],self.rect.y-Game.scroll[1],self.image.get_width(),self.image.get_height())
            if self.hitten_rect.colliderect(self.player.hit_rect) and self.player.at:
                        self.life-=self.fist_hit
class Enemy2(object):
        def __init__(self,pos,size,level):
            self.pos=pos
            self.size=size
            self.level=level
            self.count=0
            self.vel=50
            self.mvnt=[0,0]
            self.image=WEnemy2L[self.count]
            self.rect=pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
        def update(self):
            screen.blit()
class Enemy3(object):
        def __init__(self,pos,size,level):
            self.pos=pos
            self.size=size
            self.level=level
            self.count=0
            self.vel=50
            self.mvnt=[0,0]
            self.image=WEnemy3L[self.count]
            self.rect=pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
            
        def update(self):
            screen.blit()
class Objects(pygame.sprite.Sprite):
   def __init__ (self,pos,size):
       super().__init__()
       self.pos=pos
       self.size=size
       self.image=OBJ[random.randint(0,8)]
       self.rect=self.image.get_rect()
       self.mvnt=[0,0]
   def draw(self,surf,scroll):
       surf.blit(pygame.transform.scale(self.image,self.size),(self.pos[0]-scroll[0]+self.mvnt[0],self.pos[1]-scroll[1]+self.mvnt[1]))
   def get_rect(self):
        return pygame.Rect(self.pos[0]+self.mvnt[0],self.pos[1]+self.mvnt[1],self.size[0],self.size[1])
   def collission_test(self,rect):
       object_rect=self.get_rect()
       return object_rect.colliderect(rect)
   def move(self):
           self.mvnt[random.randint(0,1)]+=random.choice([0,0,0])
   def effect(self):
       self.kill()
objs=pygame.sprite.Group()
obj_pos=[9,900,1800,2700,3600,4500,5400,6300,7200,8100,9000]
for I in range(10):
      objs.add(Objects([obj_pos[I],600],(128,158)))
class Enemies(pygame.sprite.Sprite):
   pass
class Boss():
   pass
UiGroup=pygame.sprite.Group()
start=StartMenu(1500,650)
mainmenu=MainMenu(1500,700)
player=Player(500,500)
enemies=pygame.sprite.Group()
locs=[random.randint(100,800) for _ in range(20)]
for I in locs:
   enemies.add(Enemy1([I+random.randint(200,500),600],20,1,player))
controls=Controls(screen)
UiGroup.add(start)
fingers={}
exit_=False
playing=False
while not (exit_):
   player.get_rect()
   if  playing==False:
     UiGroup.draw(screen)
     start.load.x+=2
     pygame.draw.rect(start.win,(0,150,200),start.load)
     if start.load.width>=150:
         start.play=True
   for event in pygame.event.get():
      if event.type==QUIT:
         exit_=True
      if event.type==MOUSEBUTTONDOWN and start.alive():
         start.sounds[1].play()
         start.kill()
         UiGroup.add(mainmenu)
         mainmenu.Menu()
      if event.type==KEYDOWN:
          if event.key==K_UP:
            player.jump()
            player.jump_count+=1
          if event.key==K_RIGHT:
            player.mvnt[0]=0
            player.right=True
            player.wleft=False 
            player.left=False
            player.wright=True
          if event.key==K_LEFT:
            player.mvnt[0]=0
            player.right=False
            player.wleft=True
            player.left=True
            player.wright=False
          if event.key==K_s:
              player.attack()
          if event.key==K_z:
              player.at1=True
          if event.key==K_x:
              player.at2=True
      if event.type==KEYUP:
          if event.key==K_RIGHT:
            player.right=False
          if event.key==K_LEFT:
            player.left=False
          if event.key==K_s:
              player.at=False
          if event.key==K_z:
              player.at1=False
              player.count=0
          if event.key==K_x:
              player.at2=False
              player.count=0
          if player.wright:
                 player.yon=YON_R[0]
          if player.wleft:
                  player.yon=YON_L[0]
      elif event.type==MOUSEBUTTONDOWN and mainmenu.alive():
        pos=event.pos
        #pos=(round(event.x*mainmenu.rect.width),round(event.y*mainmenu.rect.height))
        if mainmenu.textRect2.collidepoint(pos):
            exit_=True
        if mainmenu.textRect4.collidepoint(pos):
           pygame.mixer.music.stop()
           mainmenu.loading.play()
           sleep(10)
           mainmenu.kill()
           playing=True
           Game.music.play()
      if event.type==MOUSEMOTION and not mainmenu.alive():
          pos=event.pos
          #pos=(round(event.x*Game.width),round(event.y*Game.height))
          #fingers[event.finger_id]=pos
          if controls.cslide_rect.collidepoint(pos):
                controls.cslide_rect.centerx=pos[0]
                if controls.cslide_rect.colliderect(controls.rightb):
                     controls.cslide_rect.right=controls.rightb.left-5
                     player.mvnt[0]=0
                     player.right=True
                     player.wleft=False 
                     player.left=False
                     player.wright=True
                if controls.cslide_rect.colliderect(controls.leftb):
                     controls.cslide_rect.left=controls.leftb.right+5
                     player.mvnt[0]=0
                     player.right=False 
                     player.wleft=True
                     player.left=True 
                     player.wright=False
                if controls.cslide_rect.colliderect(controls.topb):
                     controls.cslide_rect.top=controls.topb.bottom+5
                     player.jump()
                if controls.cslide_rect.colliderect(controls. bottomb):
                     controls.cslide_rect.bottom=controls.bottomb.top-5
                if not controls.slide_area.collidepoint(pos) and len(fingers)==1:
                     controls.cslide_rect.center=controls.crect1.center
                     player.mvnt[0]=0
                     player.right=False
                     player.left=False
      elif event.type ==MOUSEBUTTONDOWN and not mainmenu.alive():
         pos=event.pos
         #pos=(round(event.x*Game.width),round(event.y*Game.height))
         #fingers[event.finger_id]=pos
         if controls.cjump_rect.collidepoint(pos):
              player.jump()
              player.jump_count=5
         if controls.mbtn_rect.collidepoint(pos):
            start.sounds[1].play()
            controls.showmenu=True
         if controls.fist_rect.collidepoint(pos):
             player.attack()
         if controls.at1.collidepoint(pos):
            sound_effects[1][0].play()
            player.at1=True
         if controls.at2.collidepoint(pos):
            player.at2=True     
         if controls.at3.collidepoint(pos):
            player.at3=True
      elif event.type ==MOUSEBUTTONUP  and not mainmenu.alive() and not start.alive():
          pos=event.pos
          #pos=(round(event.x*Game.width),round(event.y*Game.height))
          if controls.slide_area.collidepoint(pos):
             player.mvnt[0]=0
             player.right=False
             player.left=False 
             player.yon=YON_R[0]
             controls.cslide_rect.center=controls.crect1.center
          if controls.cjump_rect.collidepoint(pos):
                player.mvnt[1]=0
          if controls.fist_rect.collidepoint(pos):
             player.at=False
          if player.wright:
                 player.yon=YON_R[0]
          if player.wleft:
                  player.yon=YON_L[0]
          if controls.at2.collidepoint(pos):
            player.count=0
            player.at2=False  
          if controls.at3.collidepoint(pos):
            player.count=0
            player.at3=False
          #fingers.pop(event.finger_id,None)
   if Game.gameover:
            playing=False
            Game.GameOver()
            for event in pygame.event.get():
                 if event.type == MOUSEBUTTONDOWN:
                   if Game.textRect3.collidepoint(event.pos):
                       Game.scroll=[0,0]
                       for enemy in enemies:
                        enemy.update()
                        enemy.walk()
                        enemy.get_hit()
                       player.player_rect.center=(500,200)
                       player.life,player.power=600,400
                       playing=True
                       Game.gameover=False
                       
   if  playing:
       player.gravity+=0.2
       screen.blit (Game.image,(0,0))
       Game.FPS()
       Game.scroll[0]+=(player.player_rect.x-Game.scroll[0]-400)//20*Game.dt
       Game.scroll[1]+=(player.player_rect.y-Game.scroll[1]-400)//10*Game.dt
       if Game.scroll[0]<-10:
           Game.scroll[0]=-10
       Game.env(load_map(map1))
       player.update()
       player.walk()
       player.attack1()
       player.attack2()
       player.attack3()
       for enemy in enemies:
          enemy.update()
          enemy.walk()
          enemy.get_hit()
       for obj in objs:
         if obj.pos[0]-Game.scroll[0]<Game.width and obj.pos[1]-Game.scroll[1]<Game.height:
           obj.move()
           obj.draw(screen,Game.scroll)
           if obj.collission_test(player.player_rect):
               if player.power <=400:
                     player.power+=10
               obj.effect()
       controls.draw(controls.surf )
       if controls.showmenu:
         screen.blit(Game.menu.image,(75,0))
         for event in pygame.event.get():
             if event.type == MOUSEBUTTONDOWN:
                if  not controls.mbtn_rect.collidepoint((event.x*Game.width, event.y*Game.height)):
                 start.sounds[1].play()
                 controls.showmenu=False
   clock.tick(45)
   pygame.display.update()
pygame.quit()