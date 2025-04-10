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

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000 

#define chracter variable
Samurai_size = 162
Samurai_scale = 4
Samurai_offset = [68, 55]
Samurai_data = [Samurai_size, Samurai_scale, Samurai_offset]
Huntress_size = 250
Huntress_scale = 3.43 
Huntress_offset = [109, 112]
Huntress_data = [Huntress_size, Huntress_scale, Huntress_offset] 
#load background image
background_image = pygame.image.load("fighting_game/assets/images/background/background.jpg").convert_alpha()

#load sheets
samurai_sheet = pygame.image.load("fighting_game/assets/images/char_1(Samurai)/warrior.png").convert_alpha()
huntress_sheet = pygame.image.load("fighting_game/assets/images/char_2(brawler)/wizard.png").convert_alpha()

#define number of steps in each animation
Samurai_animation_steps =  [10, 8, 1, 7, 7, 3, 7]  
Huntress_animation_steps = [8, 8, 1, 8, 8, 3, 7]

#define fonts
count_font = pygame.font.Font("fighting_game/assets/fonts/font.ttf", 80)
score_font = pygame.font.Font("fighting_game/assets/fonts/font.ttf", 30)

#function fir frawing text 
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#creating a function to draw a background
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
fighter_1 =  Fighter (1, 200, 325, False, Samurai_data, samurai_sheet, Samurai_animation_steps)
fighter_2 = Fighter (2, 700, 320, True, Huntress_data, huntress_sheet, Huntress_animation_steps)
 
#game loop
run = True
while run:
    clock.tick(FPS)  

#draw background
    draw_background()

#display character's healthbar 
    draw_healthbar(fighter_1.health, 20, 20)
    draw_healthbar(fighter_2.health, 580, 20)

#update countdown
    if intro_count <= 0:
        #move the characters
      fighter_1.movement(screen_width, screen_height, screen, fighter_2) 
      fighter_2.movement(screen_width, screen_height, screen, fighter_1)
    else:
        #display countdown
        draw_text(str(intro_count), count_font, RED, screen_width / 2, screen_height / 3)
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()      
    
#update the characters
    fighter_1.update()
    fighter_2.update()

#draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

#check if the chracter dies
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
