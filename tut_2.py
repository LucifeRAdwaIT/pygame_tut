import pygame 
pygame.init()
screen_W = 900
screen_H = 600
win = pygame.display.set_mode((screen_W,screen_H))
pygame.display.set_caption("Hello:")
############################################# vairibel ################################################
x = 10
y = 10
width = 20
height = 30
vel = 0.5
run = True
jump = False
jump_count = 3
##########################################################################################################
########################################### GAME LOOP ###############################################################
while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    #################################################  key input ###############################################
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x!=0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_W - width:
        x += vel
    if not jump:    
        if keys[pygame.K_UP] and y!=0:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_H - height:
            y += vel    
        if keys[pygame.K_SPACE]:
            jump=True
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
    win.fill((0,0,0))    
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))    
    pygame.display.update()    

pygame.quit()            
