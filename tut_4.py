import pygame 
pygame.init()
screen_W = 852
screen_H = 480
win = pygame.display.set_mode((screen_W,screen_H))
pygame.display.set_caption("Hello:")
############################################# vairibel ################################################
############################################# image ###################################################
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 64
height = 64
vel = 5
run = True
jump = False
jump_count = 10
left = False
right = False
walkCount = 0
##########################################################################################################
def redrawGameWin():
    global walkCount
    win.blit(bg,(0,0))
    if walkCount + 1 >= 27:
         walkCount = 0
    if left:
         win.blit(walkLeft[walkCount//3],(x,y))
         walkCount += 1 
    elif right:
         win.blit(walkRight[walkCount//3],(x,y))
         walkCount += 1
    else:
         win.blit(char,(x,y))
    pygame.display.update() 
########################################### GAME LOOP ###############################################################
while run:
    clock.tick(27) 
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
##########################################################  key input ###############################################
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x!=0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_W - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0 
    if not jump:    
        if keys[pygame.K_SPACE]:
            jump=True
            left = False
            right = False
            walkCount = 0
    else:
        if jump_count >= -10:   
            neg = 1
            if jump_count <0:
                neg = -1
            y -= (jump_count ** 2)*(0.5)*neg
            jump_count -= 1
        else:
            jump = False
            jump_count =10                    
###################################################################################################################
    redrawGameWin()
pygame.quit()            
