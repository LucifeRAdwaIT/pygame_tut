import pygame
pygame.init()
##############################################################################################################################################
win = pygame.display.set_mode((852,480))

pygame.display.set_caption("First Game")
##############################################################################################################################################
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft  = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

##############################################################################################################################################
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x,self.y))
            else:
                win.blit(walkRight[0], (self.x,self.y))    
##############################################################################################################################################                
class Projectile(object):
    def __init__(self,x,y,color,radius,facing):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.facing = facing
        self.vel = 10*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius) 
##############################################################################################################################################
class Enemy(object):
    walkRight = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    walkLeft =  [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]           
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.path = [self.x ,  self.end]
        self.vel = 5
        self.left = True
        self.right = False
    def draw(self,win):
          if self.walkCount +1 >=33:
               self.walkCount = 0
          if self.left:
               win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
               self.walkCount += 1
               if self.x < 10:
                    self.right = True
                    self.left = False
          if self.right:
               win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))   
               self.walkCount += 1
               if self.x > 800:
                    self.left = True
                    self.right = False
                
##############################################################################################################################################

##############################################################################################################################################     
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    enemy.draw(win)    
    pygame.display.update()
##############################################################################################################################################
#mainloop
man = player(200, 410, 64,64)
enemy = Enemy(100,410,64,64,500)
bullets = []
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 852 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    if enemy.left:
        enemy.x -= enemy.vel
          
    if enemy.right:
        enemy.x += enemy.vel             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1     
        if len(bullets) < 1510:                      ############################ Number of Bullet
            bullets.append(Projectile(round(man.x + man.width //2),round(man.y + man.height //2),(73,56,34),3,facing))
    if keys[pygame.K_LEFT] and man.x !=0 :
        man.x -= man.vel
        man.standing = False
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x <= 852 - man.width:
        man.x += man.vel
        man.standing = False
        man.right = True
        man.left = False
    else:
        man.standing = True
        man.walkCount = 0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.standing = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) //2 * neg  
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
       
    redrawGameWindow()
pygame.quit()