import pygame
pygame.init()

screen = pygame.display.set_mode((410,728))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

fj = pygame.image.load("./images/plane.png")
screen.blit(fj,(200,200))


pygame.display.update()
while True:
	pass

pygame.quit()
