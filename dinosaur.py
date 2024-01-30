import pygame
import os
import random

pygame.init()
Screenheight=800
screenwidth=1400

screen=pygame.display.set_mode((screenwidth,Screenheight))

#images
RUNNING =[pygame.image.load(os.path.join('Dino','DinoRun1.png')),
pygame.image.load(os.path.join("Dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Dino", "DinoJump.png"))

LEFTMOV=[pygame.image.load(os.path.join('Dino','DinoRun2.png')),
pygame.image.load(os.path.join("Dino", "DinoRun1.png")),pygame.image.load(os.path.join('Dino','DinoRun2.png')),pygame.image.load(os.path.join("Dino", "DinoRun1.png"))]

DUCKING = [pygame.image.load(os.path.join("Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Other", "Cloud.png"))
SPECIAL = pygame.image.load(os.path.join("Other", "special.png"))
BG = pygame.image.load(os.path.join("Other", "Track.png"))

class model:
    X_POS=700
    Y_POS=310
    Y_POS_DUCK= 340
    JUMP_VEL =8.5

    def __init__(self):
        self.duck_img=DUCKING
        self.run_img=RUNNING
        self.jump_img=JUMPING
        self.left_img=LEFTMOV
        self.special=SPECIAL

        self.dino_duck=False
        self.dino_run=True
        self.dino_jump=False
        self.dino_left=False

        self.step_index=0
        self.jump_vel=self.JUMP_VEL
        self.image=self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_left:
            self.left()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            self.dino_left=False
        elif userInput[pygame.K_LEFT] and not self.dino_jump and not self.dino_left and not userInput[pygame.K_DOWN]:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = False
            self.dino_left=True

        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            if userInput[pygame.K_LEFT]:
                 self.dino_left=True
            else:
                self.dino_left=False

        elif not (self.dino_jump or userInput[pygame.K_DOWN] or userInput[pygame.K_LEFT]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_left=False
            



    def run(self):
        
        self.image= self.run_img[self.step_index // 5] # choose picture for dinosaur to animate
        self.dino_rect=self.image.get_rect()
        if (self.X_POS<700):
            self.X_POS+=1

        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index+=1

    def left(self):
        print(self.step_index)
        if(self.dino_duck or self.dino_jump):
            pass
            
        else:
            self.image= self.left_img[self.step_index // 5] # choose picture for dinosaur to animate
        self.dino_rect=self.image.get_rect()
        if self.X_POS>80:
            self.X_POS-=8
        self.dino_rect.x=self.X_POS
        if not self.dino_duck:
            self.dino_rect.y=self.Y_POS
            print('not duck', self.dino_rect.y)
        else:
            self.dino_rect.y= self.Y_POS_DUCK
        self.step_index+=1

    def duck(self):
        if (self.X_POS<700 and not self.dino_left):
            self.X_POS+=1
        self.image= self.duck_img[self.step_index // 5] # choose picture for dinosaur to animate
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS_DUCK
        self.step_index+=1
        
    def jump(self):
        if (self.X_POS<700 and not self.dino_left):
            self.X_POS+=1
        self.image= self.jump_img # choose picture for dinosaur to animate
        if self.dino_jump: # jumpvel to decide when will dinosaur move down
            
            self.dino_rect.y -= self.jump_vel *4 
            self.jump_vel-=0.8 
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump= False
            self.jump_vel=self.JUMP_VEL
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x,self.dino_rect.y))




class Cloud():
    def __init__(self):
        self.x = screenwidth + random.randint(100, 200)
        self.y = random.randint(20, 120)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screenwidth + random.randint(100, 200)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class specialcloud():
    def __init__(self):
        self.image=SPECIAL
        self.rect = self.image.get_rect()
        self.rect.x= random.randint(80,600)
        self.rect.y=Screenheight+ random.randint(100, 200)
        
    def update(self):
        if self.rect.y<0:
            specialhere=False
        self.rect.y-=2
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screenwidth

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 259
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1



def main():
    global game_speed, x_posbg,y_posbg, points, obstacles,specialhere
    x_posbg=0
    y_posbg=380
    game_speed= 14
    points=0
    font = pygame.font.Font('freesansbold.ttf',20)
    cloud= Cloud()
    run=True
    clock = pygame.time.Clock()
    player = model()
    obstacles=[]
    death_count=0
    specialhere=False
    def score():
        global points, game_speed
        points+=1
        if points %100 ==0:
            game_speed+=1
        text = font.render("Points: " + str(points), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (1300, 40)
        screen.blit(text, textRect)


    def background():
        global x_posbg, y_posbg
        image_width = BG.get_width()
        screen.blit(BG, (x_posbg, y_posbg))
        screen.blit(BG, (image_width + x_posbg, y_posbg))
        if x_posbg <= -image_width:
            screen.blit(BG, (image_width + x_posbg, y_posbg))
            x_posbg = 0
        x_posbg -= game_speed

    while run:
        for e in pygame.event.get():#to use x to leave game
            if e.type == pygame.QUIT:
                run= False
        screen.fill((255,255,255))
        userinput=pygame.key.get_pressed()
        #print(userinput)
        player.draw(screen)
        player.update(userinput)
        cloud.draw(screen)
        background()

        special_random= random.randint(0,100)
        if(special_random==7 and not specialhere):
            extra=specialcloud()
            specialhere=True
        if(specialhere):
            extra.draw(screen)
            extra.update()
            if player.dino_rect.colliderect(extra.rect):
                specialhere=False
                #reward+=2


        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(200)
                death_count += 1
                reset(death_count)

        score()
        cloud.update()
        clock.tick(20)
        pygame.display.update()

def reset (death_count):
    global points
    run=True
   
    main()
    while run:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

      
      
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

reset(death_count=0)