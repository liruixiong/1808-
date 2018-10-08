import pygame
from GameSprite import *

pygame.init()

screen = pygame.display.set_mode((300,600))
bg = pygame.image.load("./images/background.png")

hero = pygame.image.load("./images/plane.png")
time = pygame.time.Clock()

enemy_group = pygame.sprite.Group()
diji = Enemysprite()
enemy_group.add(diji)

rect = pygame.Rect(125,100,100,126)


while True:
	time.tick(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏")
			pygame.quit()
			exit()
	rect.y -= 10
	if rect.y + rect.height <= 0:
		rect.y = 600
	screen.blit(bg,(0,0))
	screen.blit(hero,rect)

	enemy_group.update()
	enemy_group.draw(screen)

	pygame.display.update()


