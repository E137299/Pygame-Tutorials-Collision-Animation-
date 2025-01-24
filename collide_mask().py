import pygame, sys, random, math, time

class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super(Raindrop, self).__init__()
        self.image = pygame.image.load("graphics/raindrop.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(center = (random.randint(20,1180),random.randint(-550,800)))
    
    def fall(self):
            if self.rect.bottom>700:
                self.rect = self.image.get_rect(center = (random.randint(20,1180),random.randint(-550,800)))
            self.rect.centery += 4



class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        self.image = pygame.image.load("graphics/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center = (random.randint(20,1180),random.randint(-550,-20)))
        self.exploded = False
        self.explode_count = 0
    
    def fall(self):
        if not self.exploded:
            if self.rect.bottom>700:
                self.rect = self.image.get_rect(center = (random.randint(20,1180),random.randint(-550,-20)))
            self.rect.centery += 4
        else:
            if self.explode_count < 10:
                self.explode_count += 1
            else:
                self.kill()
    
    def pop(self):
        self.image = pygame.image.load("graphics/explode.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.exploded = True





class Head(pygame.sprite.Sprite):
    def __init__(self):
        super(Head, self).__init__()
        self.image = pygame.image.load("graphics/newton.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center = (600,500))

    def move(self, deltax):
        if self.rect.left<0:
            deltax=0
            self.rect.centerx = 55
        if self.rect.right>1200:
            deltax=0
            self.rect.centerx = 1145
        self.rect.centerx += deltax
    



# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agario")

# Create clock to later control frame rate
clock = pygame.time.Clock()

apples = pygame.sprite.Group()
for i in range(10):
    apples.add(Apple())

rain = pygame.sprite.Group()
for i in range(100):
    rain.add(Raindrop())

head = Head()
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        head.move(-5)
    if keys[pygame.K_RIGHT]:
        head.move(5)


    screen.fill((0,0,0))


    for apple in apples:
        apple.fall()
        '''
        obj1.rect.colliderect(obj2.rect) - detects when the rects of two objects collide        
        '''
        if apple.rect.colliderect(head.rect):
            apple.pop()
        '''
        pygame.sprite.collide_mask(obj1, obj2) - detects collision when the actual images collide 
        and not their transparent backgrounds collide
        '''
        # if pygame.sprite.collide_mask(apple,head):
        #     apple.pop()
    
    for drop in rain:
        drop.fall()
        '''
        pygame.sprite.collide(obj,group, kill) -detects when the object's rect collides 
                                                with any of the rects of the objects in the group
        '''
        # pygame.sprite.spritecollide(head,rain,True)

        '''
        pygame.sprite.collide(obj, group, kill, collide = pygame.sprite.collide_mask(obj1, group object))
        '''
        pygame.sprite.spritecollide(head,rain,True, collided = pygame.sprite.collide_mask(head, drop))

    apples.draw(screen)
    rain.draw(screen)
    screen.blit(head.image, head.rect.topleft)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()





