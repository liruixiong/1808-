import pygame
pygame.init()

screen = pygame.display.set_mode((300,600))
bg = pygame.image.load("./images/background.png")

hero = pygame.image.load("./images/plane.png")
time = pygame.time.Clock()

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
	pygame.display.update()

