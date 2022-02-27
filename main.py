import pygame
import random
import os
from blackjack import Cards

# sets the game window's demntions and the black background
#CONSTANTS
WIDTH = 800
HEIGHT = 600
BACKGROUND = (220, 20, 60)


def main():
	# init starts the screen and the clock
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	deck = Cards()
	card = deck.get_card()
	
	while True:
		screen.fill(BACKGROUND)
		# blit moves all the pixels of our game image into the screen
		screen.blit(card.image, card.rect)
		# flip updates the screen
		pygame.display.flip()
		# the game redraws the game screen 60 times per sec
		clock.tick(60)	
		# Setting up caption
		pygame.display.set_caption("Welcome to Blackjack")


if __name__=="__main__":
	main()
