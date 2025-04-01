import pygame
pygame.init()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("FightingGame101")

#load background image
background_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()
#creating a function to draw a bacground
def draw_background():
    scaled_background = pygame.transform.scale(background_image,(screen_width, screen_height))
    screen.blit(scaled_background, (0, 0)) 
#game loop
run = True
while run:
    draw_background()
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
