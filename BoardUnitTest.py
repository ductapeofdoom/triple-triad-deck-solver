import unittest
from Board import *

# Returns a tuple containg (number_of_blue_cards_owned, number_of_red_cards_owned)
def count_owned_cards(board):
	blue_count = 0
	red_count = 0
	for row in board.board:
		for card in row:
			if card and card[1] == 1:
				blue_count += 1
			elif card and card[1] == 2:
				red_count += 1
	return (blue_count, red_count)

class TestBlueFirstPlayer(unittest.TestCase):

	""" Unit tests to cover blue going first and winning with various valid card counts """

	def test_9_card_win(self):
		# Name collisions don't matter and stars dont matter
		blue_card_1 = Card("Card1", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 10, 10, 10, 1, 1).bit_encode()
		blue_card_3 = Card("Card3", 1, 1, 1, 1, 1, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 1, 1, 1, 1, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 3, 3, 3, 3, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 1, 1, 1, 1, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 1, 1, 1, 1, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 1, 1, 1,1, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 1, 1, 1, 1, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 1, 1, 1, 1, 2).bit_encode()

		board = Board()

		# First move: blue plays top-left corner
		board.add_card(blue_card_1, (0,0))
		self.assertEqual(count_owned_cards(board), (1,0))

		# Second move: red plays top-center
		board.add_card(red_card_1, (0,1))
		self.assertEqual(count_owned_cards(board), (1,1))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (0, 2))
		self.assertEqual(count_owned_cards(board), (2, 1))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (1,0))
		self.assertEqual(count_owned_cards(board), (2, 2))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 2))

		# Sixth move: red plays middle-right
		board.add_card(red_card_3, (1, 2))
		self.assertEqual(count_owned_cards(board), (3,3))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (2, 2))
		self.assertEqual(count_owned_cards(board), (4, 3))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (2, 1))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (1,1))
		self.assertEqual(count_owned_cards(board), (9, 0))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 1)



	def test_8_card_win(self):
		# Name collisions don't matter and stars dont matter
		blue_card_1 = Card("Card1", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 10, 10, 10, 1, 1).bit_encode()
		blue_card_3 = Card("Card3", 10, 10, 10, 10, 10, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 10, 10, 10, 10, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 10, 10, 1, 10, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 10, 1, 10, 10, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 1, 10, 10, 10, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 1, 1, 1, 1, 2).bit_encode()

		board = Board()

		# First move: blue plays top-left corner
		board.add_card(blue_card_1, (0,0))
		self.assertEqual(count_owned_cards(board), (1,0))

		# Second move: red plays top-center
		board.add_card(red_card_1, (0,1))
		self.assertEqual(count_owned_cards(board), (1,1))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (0, 2))
		self.assertEqual(count_owned_cards(board), (2, 1))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (1,0))
		self.assertEqual(count_owned_cards(board), (2, 2))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 2))

		# Sixth move: red plays bottom-middle
		board.add_card(red_card_3, (2, 1))
		self.assertEqual(count_owned_cards(board), (3,3))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (2, 2))
		self.assertEqual(count_owned_cards(board), (4, 3))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (1, 2))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (1,1))
		self.assertEqual(count_owned_cards(board), (8, 1))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 1)

	def test_7_card_win(self):
		# Name collisions don't matter and stars dont matter
		blue_card_1 = Card("Card1", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 10, 10, 10, 1, 1).bit_encode()
		blue_card_3 = Card("Card3", 10, 10, 10, 10, 10, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 10, 10, 10, 10, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 10, 10, 1, 10, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 10, 1, 10, 10, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 1, 1, 1, 1, 2).bit_encode()

		board = Board()

		# First move: blue plays top-left corner
		board.add_card(blue_card_1, (0,0))
		self.assertEqual(count_owned_cards(board), (1,0))

		# Second move: red plays top-center
		board.add_card(red_card_1, (0,1))
		self.assertEqual(count_owned_cards(board), (1,1))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (0, 2))
		self.assertEqual(count_owned_cards(board), (2, 1))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (1,0))
		self.assertEqual(count_owned_cards(board), (2, 2))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 2))

		# Sixth move: red plays bottom-middle
		board.add_card(red_card_3, (2, 1))
		self.assertEqual(count_owned_cards(board), (3,3))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (2, 2))
		self.assertEqual(count_owned_cards(board), (4, 3))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (1, 2))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (1,1))
		self.assertEqual(count_owned_cards(board), (7, 2))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 1)

	def test_6_card_win(self):
		# Name collisions don't matter and stars dont matter
		blue_card_1 = Card("Card1", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 10, 10, 10, 1, 1).bit_encode()
		blue_card_3 = Card("Card3", 10, 10, 10, 10, 10, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 10, 10, 10, 10, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 10, 10, 1, 10, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 1, 1, 1, 1, 2).bit_encode()

		board = Board()

		# First move: blue plays top-left corner
		board.add_card(blue_card_1, (0,0))
		self.assertEqual(count_owned_cards(board), (1,0))

		# Second move: red plays top-center
		board.add_card(red_card_1, (0,1))
		self.assertEqual(count_owned_cards(board), (1,1))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (0, 2))
		self.assertEqual(count_owned_cards(board), (2, 1))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (1,0))
		self.assertEqual(count_owned_cards(board), (2, 2))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 2))

		# Sixth move: red plays bottom-middle
		board.add_card(red_card_3, (2, 1))
		self.assertEqual(count_owned_cards(board), (3,3))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (2, 2))
		self.assertEqual(count_owned_cards(board), (4, 3))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (1, 2))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (1,1))
		self.assertEqual(count_owned_cards(board), (6, 3))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 1)

	def test_draw(self):
		# Name collisions don't matter and stars dont matter
		blue_card_1 = Card("Card1", 1, 8, 7, 6, 5, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 2, 1, 4, 6, 1).bit_encode()
		blue_card_3 = Card("Card3", 10, 10, 10, 10, 10, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 10, 10, 10, 10, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 1, 1, 1, 1, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 5, 5, 5, 8, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 10, 10, 10, 10, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 1, 1, 1, 1, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 1, 1, 1, 1, 2).bit_encode()

		board = Board()

		# First move: blue plays top-left corner
		board.add_card(blue_card_1, (0,0))
		self.assertEqual(count_owned_cards(board), (1,0))

		# Second move: red plays top-center
		board.add_card(red_card_1, (0,1))
		self.assertEqual(count_owned_cards(board), (0,2))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (0, 2))
		self.assertEqual(count_owned_cards(board), (2, 1))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (1,0))
		self.assertEqual(count_owned_cards(board), (2, 2))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 2))

		# Sixth move: red plays bottom-middle
		board.add_card(red_card_3, (2, 1))
		self.assertEqual(count_owned_cards(board), (3,3))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (2, 2))
		self.assertEqual(count_owned_cards(board), (4, 3))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (1, 2))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (1,1))
		self.assertEqual(count_owned_cards(board), (5, 4))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 3)

	def test_blue_random_game_draw(self):
		blue_card_1 = Card("Card1", 1, 9, 3, 3, 9, 1).bit_encode()
		blue_card_2 = Card("Card2", 1, 7, 8, 1, 4, 1).bit_encode()
		blue_card_3 = Card("Card3", 10, 3, 7, 8, 2, 1).bit_encode()
		blue_card_4 = Card("Card4", 1, 8, 1, 4, 7, 1).bit_encode()
		blue_card_5 = Card("Card5", 1, 2, 3, 8, 7, 1).bit_encode()

		red_card_1 = Card("Card1", 1, 8, 4, 6, 6, 2).bit_encode()
		red_card_2 = Card("Card2", 1, 6, 1, 7, 8, 2).bit_encode()
		red_card_3 = Card("Card3", 1, 4, 7, 1, 8, 2).bit_encode()
		red_card_4 = Card("Card4", 1, 3, 5, 9, 7, 2).bit_encode()
		red_card_5 = Card("Card5", 1, 6, 10, 7, 7, 2).bit_encode()

		board = Board()

		board.add_card(blue_card_1, (2,2))
		self.assertEqual(count_owned_cards(board), (1,0))

		board.add_card(red_card_1, (2,1))
		self.assertEqual(count_owned_cards(board), (1,1))

		# Third move: blue plays top-right 
		board.add_card(blue_card_2, (2, 0))
		self.assertEqual(count_owned_cards(board), (3, 0))

		# Fourth move: red plays middle-left
		board.add_card(red_card_2, (0,2))
		self.assertEqual(count_owned_cards(board), (3, 1))

		# Fifth move: blue plays bottom-left
		board.add_card(blue_card_3, (0, 0))
		self.assertEqual(count_owned_cards(board), (4, 1))

		# Sixth move: red plays bottom-middle
		board.add_card(red_card_3, (1, 2))
		self.assertEqual(count_owned_cards(board), (4,2))

		# Seventh move: blue plays bottom-right
		board.add_card(blue_card_4, (1, 1))
		self.assertEqual(count_owned_cards(board), (5, 2))

		# Eigth move: red plays bottom center
		board.add_card(red_card_4, (1, 0))
		self.assertEqual(count_owned_cards(board), (4, 4))

		# Ninth move: blue plays center taking the three remaing red cards
		board.add_card(blue_card_5, (0,1))
		self.assertEqual(count_owned_cards(board), (5, 4))

		# Check that blue won
		self.assertEqual(board.check_winner(1), 3)

if __name__ == "__main__":
	unittest.main()