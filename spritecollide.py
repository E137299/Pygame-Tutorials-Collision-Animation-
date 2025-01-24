import pygame, sys, random, math

class Rectangle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Rectangle, self).__init__()
        self.image = pygame.Surface((50,50), pygame.SRCALPHA, 32)
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (x,y))


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.image = pygame.Surface((100,100), pygame.SRCALPHA, 32)
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (600,300))
    
    def move(self, deltax, deltay):
        if self.rect.left < 0 or self.rect.right>1200:
            deltax *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            deltay *= -1

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


rectangles = pygame.sprite.Group()
rectangles.add(Rectangle(150,150))
rectangles.add(Rectangle(150,450))
rectangles.add(Rectangle(1050,150))
rectangles.add(Rectangle(1050,450))

sq = Square()

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
        sq.move(-2,0)
    if keys[pygame.K_RIGHT]:
        sq.move(2,0)
    if keys[pygame.K_UP]:
        sq.move(0,-2)
    if keys[pygame.K_DOWN]:
        sq.move(0,2)

    get_hit = pygame.sprite.spritecollide(sq,rectangles, False)
    if get_hit:
        screen.fill("pink")

    # get_hit = pygame.sprite.spritecollide(sq,rectangles, True)
    # if get_hit:
    #     screen.fill("pink")

    rectangles.draw(screen)
    screen.blit(sq.image, sq.rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()










