from dataclasses import dataclass
import math
import copy
import struct
from Card import Card, CARD_BIT_LENGTH

ADJACENTCY_MATRIX = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1), (0, 2)], (0, 2): [(0, 1), (1, 2)], (1, 0): [(0, 0), (1, 1), (2, 0)], (1, 1): [(0, 1), (1, 2), (1, 0), (2, 1)], (1, 2): [(0, 2), (2, 2), (1, 1)], (2, 0): [(1, 0), (2, 1)], (2, 1):[(2, 0), (1, 1), (2, 2)], (2, 2): [(2, 1), (1, 2)]}

def distance(spot1, spot2):
	x_diff = abs(spot1[0] - spot2[0])
	y_diff = abs(spot1[1] - spot2[1])
	return x_diff + y_diff

# INITAL_CARDS = [[Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0)], [Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0)], [Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0), Card("blank", 1, 1, 1, 1, 1, 0)]]

class Board:
	"""
	Board is represented by numbers as follows:
	0 1 2
	3 4 5
	6 7 8
	"""
	def __init__(self):
		self.open_squares = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
		# Initialize all squares as empty
		self.board = [[None, None, None], [None, None, None], [None, None, None]]

	def copy_board(self):
		new_board = Board()
		new_board.open_squares = copy.copy(self.open_squares)
		# new_board.board = copy.copy(self.board)
		for spot in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
			spot_x = spot[0]
			spot_y = spot[1]
			new_board.board[spot_x][spot_y] = self.board[spot_x][spot_y]
		return new_board

	def evaluate_board(self, spot_played, card):
		# for i in range(-1, 2):
		# 	for j in range(-1, 2):
		for adjacent_spot in ADJACENTCY_MATRIX[spot_played]:
			# attmepted_check = (spot_played[0] + i, spot_played[1] + j)
			# Bounds check to see if we are checking a card on the board
			# Also skip the check if the square hasn't been used yet
			# Also check to make sure we aren't moving diagonally
			if adjacent_spot not in self.open_squares:
				# print("Attmepted: {}".format(attmepted_check))
				# print("Played: {}".format(spot_played))
				# Find the relavant side of each relavant card
				played_card_side = None
				collided_card_side = None
				if spot_played[0] - adjacent_spot[0] == -1:
					played_card_side = card[7]
					collided_card_side = self.board[adjacent_spot[0]][adjacent_spot[1]][3]
				elif spot_played[0] - adjacent_spot[0] == 1:
					played_card_side = card[3]
					collided_card_side = self.board[adjacent_spot[0]][adjacent_spot[1]][7]
				elif spot_played[1] - adjacent_spot[1] == -1:
					played_card_side = card[5]
					collided_card_side = self.board[adjacent_spot[0]][adjacent_spot[1]][9]
				elif spot_played[1] - adjacent_spot[1] == 1:
					played_card_side = card[9]
					collided_card_side = self.board[adjacent_spot[0]][adjacent_spot[1]][5]
				# Capture card if needed
				if played_card_side > collided_card_side and card[1] != self.board[adjacent_spot[0]][adjacent_spot[1]][1]:
					self.board[adjacent_spot[0]][adjacent_spot[1]] = card[0:2] + self.board[adjacent_spot[0]][adjacent_spot[1]][2:]

	# Checks the winner, first player is used to determine number of cards needed to win
	# Returns 1 if Blue, 2 if Red, 3 if a draw
	def check_winner(self, first_player):
		if len(self.open_squares) > 0:
			print("[BoardError] Game is not over. Winner cannot be determined")
			raise Exception()
		else:
			blue_cards = 0
			red_cards = 0
			for row in self.board:
				for card in row:
					# print(card)
					if card[1] == 1:
						blue_cards += 1
					else:
						red_cards += 1
			# print(blue_cards, red_cards)
			# If blue was first
			if first_player == 1:
				if blue_cards > red_cards and blue_cards > 5:
					return 1
				elif red_cards > blue_cards and red_cards > 4:
					return 2
				else:
					return 3
			else:
				if red_cards > blue_cards and red_cards > 5:
					return 2
				elif blue_cards > red_cards and blue_cards > 4:
					return 1
				else:
					return 3



	# Adds card to the board at spot
	def add_card(self, card, spot):
		if spot in self.open_squares:
			self.board[spot[0]][spot[1]] = card
			self.open_squares.remove(spot)
			self.evaluate_board(spot, card)
		else:
			print("[BoardError]Cannot play in that spot")
			raise Exception()

	def __str__(self):
		b = self.board
		return " {} | {} | {} \n{}{}{}|{}{}{}|{}{}{}\n {} | {} | {} \n___________\n {} | {} | {} \n{}{}{}|{}{}{}|{}{}{}\n {} | {} | {} \n___________\n {} | {} | {} \n{}{}{}|{}{}{}|{}{}{}\n {} | {} | {} \n".format(b[0][0].top, b[1][0].top, b[2][0].top, b[0][0].left, b[0][0].owner, b[0][0].right, b[1][0].left, b[1][0].owner, b[1][0].right, b[2][0].left, b[2][0].owner, b[2][0].right, b[0][0].bottom, b[1][0].bottom, b[2][0].bottom, b[0][1].top, b[1][1].top, b[2][1].top, b[0][1].left, b[0][1].owner, b[0][1].right, b[1][1].left, b[1][1].owner, b[1][1].right, b[2][1].left, b[2][1].owner, b[2][1].right, b[0][1].bottom, b[1][1].bottom, b[2][1].bottom, b[0][2].top, b[1][2].top, b[2][2].top, b[0][2].left, b[0][2].owner, b[0][2].right, b[1][2].left, b[1][2].owner, b[1][2].right, b[2][2].left, b[2][2].owner, b[2][2].right, b[0][2].bottom, b[1][2].bottom, b[2][2].bottom)

if __name__ == "__main__":
	test_board = Board()
	# print(test_board.open_squares)
	# test_board.evaluate_board((1, 1))