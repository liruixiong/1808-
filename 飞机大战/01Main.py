import pygame
from GameSprite import *


class PlaneGame(object):

	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode((480,600))
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		pygame.time.set_timer(CREATE_BULLET_EVENT,250)
		self.enemy_group = pygame.sprite.Group()
		self.bullet_group = pygame.sprite.Group()

		self.yx = HeroSprint()
		self.yxs = pygame.sprite.Group(self.yx)

	def start_game(self):
		print("开始游戏...")
		while True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()

			pygame.display.update()

	def __create_sprites(self):
		bsg = BackGroundSprint()
		bsg1 = BackGroundSprint(False)
		self.bgsg = pygame.sprite.Group(bsg,bsg1)

	def __event_handler(self):
#事件监听 
		for event in pygame.event.get():
 
			if event.type == pygame.QUIT:
				 PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemysprite()
				self.enemy_group.add(enemy)
			elif event.type == CREATE_BULLET_EVENT:
				bullet = BulletSprite()
				bullet.rect.x = self.yx.rect.centerx - 18
				bullet.rect.y = self.yx.rect.top - 30

				bullet1 = BulletSprite()
				bullet1.rect.x = self.yx.rect.centerx - 53
				bullet1.rect.y = self.yx.rect.top + 35

				bullet2 = BulletSprite()
				bullet2.rect.x = self.yx.rect.centerx + 17
				bullet2.rect.y = self.yx.rect.top + 35

				self.bullet_group.add(bullet,bullet1,bullet2)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.yx.speed = 5
		elif keys[pygame.K_LEFT]:
			self.yx.speed = -5
		else:
			self.yx.speed = 0

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.yx.speed1 = -5
		elif keys[pygame.K_DOWN]:
			self.yx.speed1 = 5
		else:
			self.yx.speed1 = 0

		
	def __check_collide(self):
#碰撞检测
# 1. 子弹摧毁敌机
		pygame.sprite.groupcollide(self.bullet_group,self.enemy_group, True, True)

# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.yx, self.enemy_group, True)

# 判断列表时候有内容
		if len(enemies) > 0:

# 让英雄牺牲
			self.yx.kill()

# 结束游戏
			PlaneGame.__game_over()

	def __update_sprites(self):
#更新精灵组
		self.bgsg.update()
		self.bgsg.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.yxs.update()
		self.yxs.draw(self.screen)

		self.bullet_group.update()
		self.bullet_group.draw(self.screen)
	@staticmethod
	def __game_over():
#游戏结束

		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == '__main__':
# 创建游戏对象
	game = PlaneGame()

# 开始游戏
	game.start_game()
