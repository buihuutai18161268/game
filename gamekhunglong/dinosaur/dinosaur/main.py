import pygame

# hàm khởi tạo
pygame.init()

# hệ màu RGB
WHITE = (255,255,255) 
BLACK = (0,0,0)
RED = (255,0,0)

# gốc tọa độ phía trên tay trái màn hình
# tạo cửa sổ có (ngang,dọc) = (x,y) = (600,300)
screen = pygame.display.set_mode((600,300))
# đặt tên chương trình
pygame.display.set_caption("GAME KHỦNG LONG")

running = True	
clock = pygame.time.Clock()

# tạo độ của khủng long
dinosaur_x = 0
dinosaur_y = 222
# tạo dộ ảnh nền 
background_x = 0
background_y = 0
# tọa độ cây
tree_x = 550
tree_y = 227

#load ảnh lên
dinosaur = pygame.image.load('dinosaur.png')
tree = pygame.image.load('tree.png')
background = pygame.image.load('background.jpg')

# tốc độ di chuyển của màn hình 
x_velocity = 2
# tọa độ khi khủng long nhảy
y_velocity = 7

# biến nhảy của khủng long
jump = False

# biến khi khủng long chạm vào cây
pausing = False

# điểm 
score = 0
# tạo chữ 
# sans là kiểu chữ có sẵn , cỡ chữ:40
font = pygame.font.SysFont('sans',20)
font1 = pygame.font.SysFont('sans',40)

# âm thanh
sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('te.wav')

while running:
	screen.fill(WHITE)
	# màn hình nháy 60 trong 1s
	clock.tick(60)

	# cập nhật hình ảnh trên pygame
	# Trước khi bức ảnh background di chuyển từ phải qua trái qua hết màn hình screen(600,300)
	background1_pos = screen.blit(background,(background_x,background_y))
	# Sau khi bức ảnh background di chuyển từ phải qua trái qua hết màn hình screen(600,300)
	background2_pos = screen.blit(background,(background_x+600,background_y))
	# khi background chạy ra khỏi màn hình thì sẽ xuất hiện lại vị trí ban đầu

	# điểm 
	if dinosaur_x+50 == tree_x or dinosaur_x == tree_x: # 50 là chiều ngang của bức ảnh khủng long
		score += 1
	text_score = font.render("Score:" + str(score),True,RED)
	screen.blit(text_score,(5,5))

	# tốc độ(tọa độ) di chuyển của background từ phải qua trái
	background_x -= x_velocity

	if background_x+600 <= 0:
		background_x = 0
	tree_pos = screen.blit(tree,(tree_x,tree_y))
	dinosaur_pos = screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
	# tốc độ(tọa độ) di chuyển của cây từ phải qua trái
	tree_x -= x_velocity
	# khi cây chạy ra khỏi màn hình thì sẽ xuất hiện lại vị trí ban đầu
	if tree_x <= -25: # 25 là chiều ngang của bức ảnh cây
		tree_x = 550

	# khi khủng long chạy ra khỏi màn hình thì sẽ xuất hiện lại vị trí ban đầu
	if dinosaur_x >= 650:
		dinosaur_x = 0	

	# xử lý khi nhấn phím SPACE(nhảy)
	if 100 <= dinosaur_y <=222:
		if jump == True:
			dinosaur_y -= y_velocity
	else:
		jump = False
	if dinosaur_y < 222:
		if jump == False:
			dinosaur_y += y_velocity

	# tốc độ(tọa độ) di chuyển của khủng long từ trái qua phải
	dinosaur_x += x_velocity

	# Khi khủng long và cây chạm nhau 
	# Hàm để kiểm tra khủng long và cây chạm nhau 
	if dinosaur_pos.colliderect(tree_pos):
		pausing = True
		text_gameover = font.render("GAME OVER",True,BLACK)
		screen.blit(text_gameover,(300,150))
		x_velocity = 0
		y_velocity = 0
		# âm thanh
		pygame.mixer.Sound.play(sound2)

	# xét những sự kiện như là bấm chuột , nút tắt(quit(x)) , ấn bàn phím
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: # khi nào bật nút quit(x) thoát vòng lặp while True 
			running = False 
		# xử lý phím (bàn phím)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: # nhấn phím space(cách)
				if dinosaur_y == 222:
					# cho khủng long nhảy
					jump = True
					# âm thanh
					pygame.mixer.Sound.play(sound1)
			if event.key == pygame.K_RETURN: # nhấm phím enter
				if pausing:
					# chơi lại từ đầu
					dinosaur_x = 0
					dinosaur_y = 222
					background_x = 0
					background_y = 0
					tree_x = 550
					tree_y = 227
					x_velocity = 2
					y_velocity = 7
					jump = False
					pausing = False
					score = 0

	# hiển thị tất cả những gì vẽ lên màn hình bảng screen mới chạy được
	pygame.display.flip() 

pygame.quit() # làm giảm dung lượng bộ nhớ, thoát trò chơi
