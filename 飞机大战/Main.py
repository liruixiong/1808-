import pygame
from GameSprite import *


class PlaneGame(object):

	def __init__(self):
		print("游戏初始化")
		self.screen = pygame.display.set_mode((480,600))
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		pygame.time.set_timer(CREATE_BULLET_EVENT,500)
		self.enemy_group = pygame.sprite.Group()
		self.enemy1_down_group = pygame.sprite.Group()
		self.bullet_group = pygame.sprite.Group()

		self.yx = HeroSprint()
		self.yxs = pygame.sprite.Group(self.yx)
		#分数
		self.count = 0
		self.score = 0

	def start_game(self):
		pygame.init()
		print("开始游戏...")
		while True:
			self.count += 1
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
		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.bullet_group, True, True)
		enemy1_down_group.add(enemy_down)
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
		
		#绘制分数
		self.drawText(str(self.score),SCREEN_RECT.width - 30,50)
		#敌机销毁
		for enemy1_down in enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count % 15 == 0:
				enemy1_down.down_index += 1
				if enemy1_down.down_index == 3:
					self.score +=5
					enemy1_down_group.remove(enemy1_down)
					print(self.score)
	@staticmethod
	def __game_over():
#游戏结束

		print("游戏结束")
		pygame.quit()
		exit()
	def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
		fontObj = pygame.font.Font(None,textHeight)  # 通过字体文件获得字体对象
		textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
		textRectObj.center = (posx, posy)  # 设置显示对象的坐标
		self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字	
if __name__ == '__main__':
# 创建游戏对象
	game = PlaneGame()

# 开始游戏
	game.start_game()
