import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,600)
FRAME_PER__SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_BULLET_EVENT = pygame.USEREVENT+1

bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4= pygame.image.load('./images/enemy0_down4.png')

enemy1_down_group = pygame.sprite.Group()

enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed = 1):
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect =  self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed

class Enemysprite(GameSprite):
	def __init__(self):
		imagename = "./images/enemy0.png"
		super().__init__(imagename,random.randint(1,5))
		
		self.rect.bottom = 0
		self.rect.x = random.randint(1,480-self.rect.width)
		self.down_index = 0
	def update(self):
		super().update() 
		if self.rect.top >= 600:
			self.kill()
	def __del__(self):
		pass

class BackGroundSprint(GameSprite):
	def __init__(self,isalt = True):
		imagename = "./images/background.png"
		super().__init__(imagename,5)
		if not isalt:
			self.rect.bottom = 0
	def update(self):
		super().update()
		if self.rect.top >= 600:
			self.rect.bottom = 0#移到屏幕上方

class HeroSprint(GameSprite):
	def __init__(self):
		imagename = ("./images/hero.gif")
		super().__init__(imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom-20
	def update(self):
		self.rect.x += self.speed
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

		self.rect.y += self.speed1
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom

class BulletSprite(GameSprite):
	def __init__(self):
		imagename = "./images/plane.png"
		super().__init__(imagename,-25)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()

class Soruce(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()
