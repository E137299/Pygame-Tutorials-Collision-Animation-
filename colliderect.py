import pygame, sys, random, math

class Square(pygame.sprite.Sprite):
    def __init__(self,size,x,y, color, velocity):
        super(Square, self).__init__()
        self.image = pygame.Surface((50,50), pygame.SRCALPHA, 32)
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
        self.deltax = velocity


    def move(self):
        if self.rect.left <0 or self.rect.right > 1200:
            self.deltax *= -1
        self.rect.centerx += self.deltax




# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agario")

# Create clock to later control frame rate
clock = pygame.time.Clock()

boxes = pygame.sprite.Group()
boxes.add(Square(100,50,300,"red",2))
boxes.add(Square(50,550,300,"blue",-2))


# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))


    for box in boxes:
        box.move()
        for other in boxes:
            if box != other and box.rect.colliderect(other.rect):
                screen.fill((255,255,255))

    boxes.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()





