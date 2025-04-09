import pygame

class Fighter:
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1] 
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0 
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 100, 190))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking =  False
        self.attack_type = 0
        self.health = 100

#extract images from spritesheet
    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y,  animation in enumerate(animation_steps):
            temp_img_lists = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size , self.size, self.size)
                temp_img_lists.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_lists)
        return animation_list  
        

    # Create movements for the characters
    def movement(self, screen_width, screen_height, surface, target):
        movement_speed = 8
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False

        # Get inputs from pressing keys (key-presses)
        key = pygame.key.get_pressed()

        #Can only perform other actions if not currently attacking  
        if self.attacking == False:
            # Movements (move left and right)   
            if key[pygame.K_a]:
                dx = -movement_speed
                self.running = True
            if key[pygame.K_d]:
                dx = movement_speed 
                self.running = True
            #Jumping
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            #add attacking
            if key[pygame.K_x] or key[pygame.K_c]:
                self.attack(surface, target)
            #determine which type of attack is being used
                if key[pygame.K_r]:
                    self.attack_type = 1
                if  key[pygame.K_t]:
                    self.attack_type = 2
        
        #Apply gravity
        self.vel_y += GRAVITY  
        dy += self.vel_y 
         
        # Ensure the characters stay on the screen without going off
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 95:
            self.vel_y = 0
            self.jump = False 
            dy = screen_height - 95 - self.rect.bottom
        
        #Ensure characters face each others
        if target.rect.centerx > self.rect.centerx :
            self.flip = False 
        else:
             self.flip = True

        # Update players' movements from key-presses
        self.rect.x += dx
        self.rect.y += dy 

#handle animations' updates
    def update(self):
#check what action the player is performing
        if self.jump == True:
            self.update_action(2)
        if self.running == True:
            self.update_action(1)
        else:
            self.update_action(1)

        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if the animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


            
    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 1.5 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 7.5  
    
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_action(self, new_action):
    #check if the new action ius different ot previous one
        if new_action != self.action:
            self.action = new_action 
    #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    

    # Draw rectangles for the characters' hit-boxes 
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
