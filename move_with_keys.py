import pygame, sys, random, math

class Square(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super(Square, self).__init__()
        self.image = pygame.Surface((100,100), pygame.SRCALPHA, 32)
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x,y))
    
    def move(self, deltax, deltay):
        if self.rect.left < 0 or self.rect.right>1200:
            deltax *= -3
        if self.rect.top < 0 or self.rect.bottom > 600:
            deltay *= -3

        self.rect.centerx += deltax
        self.rect.centery += deltay
# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agario")

# Create clock to later control frame rate
clock = pygame.time.Clock()

sq1 = Square(1100,300,"red")
sq2 = Square(100,300,"pink")
squares = pygame.sprite.Group()
squares.add(sq1)
squares.add(sq2)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

        # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update rectangle position based on key presses
    # if keys[pygame.K_LEFT]:
    #     sq.rect.x -= 2
    # if keys[pygame.K_RIGHT]:
    #     sq.rect.x += 2
    # if keys[pygame.K_UP]:
    #     sq.rect.y -= 2
    # if keys[pygame.K_DOWN]:
    #     sq.rect.y += 2
    
    if keys[pygame.K_LEFT]:
        sq1.move(-2,0)
    if keys[pygame.K_RIGHT]:
        sq1.move(2,0)
    if keys[pygame.K_UP]:
        sq1.move(0,-2)
    if keys[pygame.K_DOWN]:
        sq1.move(0,2)
    
    if keys[pygame.K_a]:
        sq2.move(-2,0)
    if keys[pygame.K_d]:
        sq2.move(2,0)
    if keys[pygame.K_w]:
        sq2.move(0,-2)
    if keys[pygame.K_s]:
        sq2.move(0,2)

    squares.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()





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





