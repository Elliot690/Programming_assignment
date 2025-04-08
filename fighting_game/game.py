import pygame 
from fighters import Fighter

pygame.init()

screen_width = 1000
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("FightingGame101")

#cap framerate
clock = pygame.time.Clock()
FPS =  60

#define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0 )
GREEN = (0, 255, 0)

#define chracter variable
Samurai_size = 88
Samurai_data = [Samurai_size]
Huntress_size = 88
Huntress_data = [Huntress_size]
#load background image
background_image = pygame.image.load("fighting_game/assets/images/background/background.jpg").convert_alpha()

#load sheets
samurai_sheet = pygame.image.load("fighting_game/assets/images/char_1(Samurai)/samurai.png").convert_alpha()
huntress_sheet = pygame.image.load("fighting_game/assets/images/char_2(brawler)/huntress.png").convert_alpha()

#define number of steps in each animation
Samurai_animation_steps =  [6, 6, 6, 4, 4, 8, 2]  
Huntress_animation_steps = [8, 8, 7, 5, 5, 8, 2, 2, 3]

#creating a function to draw a bacground
def draw_background():
    scaled_background = pygame.transform.scale(background_image,(screen_width, screen_height))
    screen.blit(scaled_background, (0, 0)) 

#function for drawing the characters' healthbars
def draw_healthbar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x- 1, y-1, 403, 33 ))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio , 30 ))
#create two chracters 
fighter_1 =  Fighter (200, 325, Samurai_data, samurai_sheet, Samurai_animation_steps)
fighter_2 = Fighter (700, 325, Huntress_data, huntress_sheet, Huntress_animation_steps )
 
#game loop
run = True
while run:
    clock.tick(FPS)  
#draw background
    draw_background()
#display character's healthbar
    draw_healthbar(fighter_1.health, 20, 20)
    draw_healthbar(fighter_2  .health, 580, 20)
#move the characters
    fighter_1.movement(screen_width, screen_height, screen, fighter_2)
    #fighter_2.movement()
     
#draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
 
