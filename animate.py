# Import the pygame library
from pygame import mixer
import pygame, random

from sys import exit

# Necessary Step! Initiates all of the parts of the Pygame library.
pygame.init()

# Create Screen - a display surface
screen_width = 800
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))

# Add a label to the pygame window
pygame.display.set_caption("Intro to Pygame: Platform Game")

# Create Clock object - responsible for controlling the games frame rate
clock = pygame.time.Clock() # create a clock object


class Background(pygame.sprite.Sprite):
	def __init__(self, image_path, x, y, speed):
		super().__init__()
		self.x = x
		self.y = y
		self.speed = speed
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

	def move_right(self):
		if self.rect.centerx > 1200:
			self.x = -400
			self.rect.centerx = self.x
		self.x += self.speed
		self.rect.centerx = self.x

	def move_left(self):
		if self.rect.centerx < -400:
			self.x = 1200
			self.rect.center = (self.x,self.y)
		self.x -= self.speed
		self.rect.center = (self.x,self.y)

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Player,self).__init__()
		self.moveY = 0
		self.x = x
		self.y = y
		self.index = 0
		self.direction = "right"
		self.jump_count = 0
		self.right_jump_image = pygame.image.load("graphics/jump.png").convert_alpha()
		self.right_files = ["graphics/player_walk_1.png", "graphics/player_walk_2.png"]
		self.right_images = [pygame.image.load(filename).convert_alpha() for filename in self.right_files]
		self.pics = [[pygame.image.load("graphics/player_stand.png")],[pygame.transform.flip(img, True, False) for img in self.right_images],[pygame.transform.flip(self.right_jump_image,True,False)], [pygame.image.load(filename).convert_alpha() for filename in self.right_files],[self.right_jump_image]]
		self.image = self.pics[0][0]
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

	def move_right(self):
		self.direction = "right"
		self.index = (self.index +1)%2
		self.image = self.pics[3][self.index]
		self.rect.center = (self.x,self.y)
	def move_left(self):
		self.direction = "left"
		self.index = (self.index +1)%2
		self.image = self.pics[1][self.index]
		self.rect.center = (self.x,self.y)
	def stand(self):
		self.image = self.pics[0][0]
	
	def jump(self, group):
		if self.direction == "right":
			self.image = self.pics[4][0]
		else:
			self.image = self.pics[2][0]

		if self.jump_count < 20:
			self.y -= 15
			self.rect.centery = self.y
		self.jump_count += 1

		
	def gravity(self):
		self.y += 10
		self.rect.centery = self.y
		if self.rect.centery > 300:
			source = audio.play_file("maleyell.wav")
			self.kill()
			print("Death")






'''
Groups
'''
scenery = pygame.sprite.Group()
background = pygame.sprite.Group()
background.add(Background("graphics/Sky.png",-400,150, 4))
background.add(Background("graphics/Sky.png",400,150, 4))
background.add(Background("graphics/Sky.png",1200,150, 4))
land = pygame.sprite.Group()
first = Background("graphics/ground.png",325,325,8)

land.add(first)

scenery.add(background)
scenery.add(land)

player = Player(200,50)


all_sprites = pygame.sprite.Group()
all_sprites.add(scenery)
all_sprites.add(player)

while True:
	#Event loop - Looks for for user input which could include: key presses, mouse movement, mouse clicks, etc.
	for event in pygame.event.get():
		# Close game if the red square in the top left of the window is clicked
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player.stand()
				for e in enemies:
					e.adjust = 0
			if event.key == pygame.K_LEFT:
				player.stand()
				for e in enemies:
					e.adjust = 0
			if event.key == pygame.K_UP:
				player.stand()
			
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		for s in scenery:
			s.move_left()
		player.move_right()	
	if keys[pygame.K_LEFT]:
		for s in scenery:
			s.move_right()
		player.move_left()
	if keys[pygame.K_UP]:
		# player.jump_count+=1
		player.jump(land)


	
	if not pygame.sprite.spritecollide(player,land,False):
		player.gravity()
	else:
		player.jump_count = 0


	
	all_sprites.draw(screen)



	# Updates all of the images and objects on the screen (display surface)
	pygame.display.update()

	#Setting the game's frame rate to 60 frames per second
	clock.tick(30)