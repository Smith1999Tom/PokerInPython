import sys
import pygame
import random
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5,35)

size = width, height = 920, 640
speed = [2, 2]
black = 0, 0, 0
background = 49, 117, 61

cNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cSuit = ['H', 'D', 'C', 'S']

class Opponent:
	rect = None
	image = None
	card = [None, None]
	chips = 100
	confidence = 0
	cool = 0
	def __init__(self, x, y, image):
		self.image = pygame.image.load(image)
		chips = 100
		confidence = 1
		cool = 1
		self.rect = self.image.get_rect(topleft=(x, y))
	def getChips(self):
		return self.chips

	def getRect(self):
		return self.rect

	def getImage(self):
		return self.image

	def getCards(self):
		return self.card

	def clearCards(self):
		card = [None, None]


class Player:
	card = [None, None]
	def __init__(self):
		chips = 100
	def getChips(self):
		return self.chips

	def getCards(self):
		return self.card

	def clearCards(self):
		card = [None, None]


def shuffleDeck():
	return


def main():


	pygame.init()
	clock = pygame.time.Clock()

	myfont = pygame.font.SysFont('Elephant', 16)
	

	screen = pygame.display.set_mode(size)

	ball = pygame.image.load("ball.png")
	ballrect = ball.get_rect()

	r1 = random.randint(1, 13)
	r2 = random.randint(1, 13)
	s1 = random.randint(0, 3)
	s2 = random.randint(0, 3)


	card1 = pygame.image.load(f"Card_{r1}{cSuit[s1]}.png")
	card2 = pygame.image.load(f"Card_{r2}{cSuit[s2]}.png")
	card1rect = card1.get_rect(center=((width/2) - 20, height - 80)) #center=((width/2) - 40, height - 150)
	card2rect = card2.get_rect(center=((width/2) + 20, height - 80)) #topleft=((width/2) + 40, height - 150)

	
	player1 = Opponent(40, 20, "Player2.png")
	player1text = myfont.render(str(player1.getChips()), False, (0, 0, 0))
	player2 = Opponent(388, 20, "Player3.png")
	player2text = myfont.render(str(player2.getChips()), False, (0, 0, 0))
	player3 = Opponent(736, 20, "Player4.png")
	player3text = myfont.render(str(player3.getChips()), False, (0, 0, 0))

	btnFold = pygame.image.load("Btn_Fold.png")
	btnFoldRect = btnFold.get_rect(center=(340, 460))
	btnCheck = pygame.image.load("Btn_Check.png")
	btnCheckRect = btnCheck.get_rect(center=(460, 460))
	btnRaise = pygame.image.load("Btn_Raise.png")
	btnRaiseRect = btnRaise.get_rect(center=(580, 460))

	#fold check raise
	#	  call

	card1pos = [card1rect.x, card1rect.y]
	card2pos = [card2rect.x, card2rect.y]


	mousepos = [0, 0]

	while True:
		mousepos = pygame.mouse.get_pos()

		card1rect.x = card1pos[0]
		card1rect.y = card1pos[1]

		card2rect.x = card2pos[0]
		card2rect.y = card2pos[1]


		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		if (card1rect.collidepoint(mousepos) and not card2rect.collidepoint(mousepos)):
			card1rect.y -= 10

		if card2rect.collidepoint(mousepos):
			card2rect.y -= 10

		ballrect = ballrect.move(speed)
		

		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]



		screen.fill(background)
		screen.blit(ball, ballrect)
		screen.blit(card1, card1rect)
		screen.blit(card2, card2rect)
		screen.blit(player1.getImage(), player1.getRect())
		screen.blit(player1text, player1.getRect())
		screen.blit(player2.getImage(), player2.getRect())
		screen.blit(player2text, player2.getRect())
		screen.blit(player3.getImage(), player3.getRect())
		screen.blit(player3text, player3.getRect())

		screen.blit(btnFold, btnFoldRect)
		screen.blit(btnCheck, btnCheckRect)
		screen.blit(btnRaise, btnRaiseRect)
		pygame.display.flip()


		clock.tick(30)

if __name__ == '__main__': main()