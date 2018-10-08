import pygame
pygame.init()

screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("./images/mein.png")

hero = pygame.image.load("./images/plane.png")
time = pygame.time.Clock()

rect = pygame.Rect(200,200,100,126)


while True:
	time.tick(100)#每秒刷新100次
	rect.y -= 20
	screen.blit(bg,(0,0))#贴图像
	screen.blit(hero,rect)#贴图像
    
	pygame.display.update()#更新
pygame.quit()
