import pygame

class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 190))

    # Create movements for the characters
    def movement(self, screen_width):
        movement_speed = 10
        dx = 0
        dy = 0

        # Get inputs from pressing keys (key-presses)
        key = pygame.key.get_pressed()

        # Movements
        if key[pygame.K_a]:
            dx = -movement_speed
        if key[pygame.K_d]:
            dx = movement_speed 
        
        # Ensure the characters stay on the screen without going off
        if self.rect.left + dx < 0:
            dx = 0

        # Update players' movements from key-presses
        self.rect.x += dx
        self.rect.y += dy 

    # Draw rectangles for the characters' hit-boxes 
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
