# Programming_assignment

class Fighter:
 def __init__(self, x, y):
    self.rect = pygame.Rect((x, y, 900 , 1500))


    # Create movements for the characters
def movement(self):
    movement_speed = 25
    dx = 0
    dy = 0

        # Get inputs from pressing keys (key-presses)
    key = pygame.key.get_pressed() 

        # Movements
    if key[pygame.K_a]:
        dx = -movement_speed
    if key[pygame.K_d]:
        dx = movement_speed 
     
        #ensure the chracters stay on the screen without going off
    if self.rect.left + dx < 0:
        dx = -self.rect.le 
    if self.rect.right + dx > screen_width:


        # Update players' movements from key-presses
     self.rect.x += dx
     self.rect.y += dy 

    # Draw rectangles for the characters' hit-boxes 
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)