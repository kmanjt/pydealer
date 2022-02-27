#!/usr/bin/env python3

import pygame
import os
import random


class Blackjack(object):
	def __init__(self):
		self.deck = [card for card in os.listdir(".assets/cards-png")]


class Deck(object):
	
	def __init__(self):
		self.deck = [card for card in os.listdir("assets/cards-png")]
		self.cards_used = []
		
	def get_card(self):
		card = random.choice(self.deck)
		val, suit = self.get_card_details(card)
		self.remove_card(card)
		image = pygame.image.load("assets/cards-png/"+card)
		card_obj = Card(val, suit, image)
		return card_obj

	def get_card_details(self, card):
		tokens = card.split("_")
		val = tokens[0]
		suit = tokens[-1].strip(".png")
		return val, suit
		
	def remove_card(self, card):
		if card in self.deck:
			self.deck.remove(card)

class Card(object):

	def __init__(self, value, suit, image):
		self.value = value
		self.suit = suit
		self.image = image
		self.rect = self.image.get_rect()
