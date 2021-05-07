import pygame
from pygame.locals import *
import math
import random

#Initialize_setup the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# thêm cảnh quan
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# main chính của game
player = pygame.image.load("resources/images/dude.png")

running = True

# Tạo chuyển động cho chú thỏ
# điều khiển được chú thỏ theo điều khiển trên bàn phím.
keys = [False, False, False, False]
playerpos=[100,100]

while running:
	screen.fill((0,0,0)) 

	# 6 - draw the player on the screen at X:100, Y:100
	# Tuy nhiên, bức ảnh grass.png chưa lấp đầy khung hình. Vì thế, bạn cần vẽ thêm một số phần vào trước phần #6. Thêm những dòng code sau vào trước screen.blit(player, (100,100))
	for x in range(int(width/grass.get_width())+1):
	    for y in range(int(height/grass.get_height())+1):
	        screen.blit(grass,(x*100,y*100))
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345 ))

	screen.blit(player, (100,100))
	pygame.display.flip()

	# xét những sự kiện khi bấm chuột, bấm nút tắt(quit(x)), ấn bàn phím 
	for event in pygame.event.get():
		# sự kiên án nút quit(x)
		if event.type == pygame.QUIT:
			running = False

	# pygame.display.flip()