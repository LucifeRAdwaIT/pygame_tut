import pygame 
pygame.init()

win = pygame.display.set_mode((500,600))
pygame.display.set_caption("Hello:")

x = 50
y = 50
width = 50
height = 60
vel = 0.1

run = True
while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
#################################################  key input ###############################################
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    win.fill((0,0,0))    
    pygame.draw.rect(win,(0,255,0),(x,y,width,height))    
    pygame.display.update()    

pygame.quit()            
