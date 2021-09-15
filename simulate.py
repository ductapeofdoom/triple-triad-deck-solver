import random
import itertools
import copy
from multiprocessing import Process, Pool
from Board import Board

def copy_deck(deck):
	new_deck = []
	for card in deck:
		new_deck.append(copy.copy(card))
	return new_deck

def play_permutations(first_play, current_first_permutation, current_second_permutation, spot_order_permutations):
	blue_wins = 0
	red_wins = 0
	draws = 0
	play_string_dict = {}
	for k in range(0, len(spot_order_permutations)):
		current_order_permutation = list(spot_order_permutations[k])
		current_step_count  = 0
		current_dict = play_string_dict
		current_board = Board()
		while current_step_count < len(current_order_permutation):
			current_step = current_order_permutation[current_step_count]
			if current_step not in current_dict.keys():
				current_dict[current_step] = {}
				try:
					# current_board = copy.deepcopy(current_dict["board"])
					current_board = current_dict["board"].copy_board()
				except KeyError:
					pass
				current_dict = current_dict[current_step]
				break
			else:
				current_step_count += 1
				current_dict = current_dict[current_step]

		for p in range(current_step_count, len(current_order_permutation)):
			# If first
			if p % 2 == 0:
				current_board.add_card(current_first_permutation[p // 2], current_order_permutation[p])
			# If second
			elif p % 2 == 1:
				current_board.add_card(current_second_permutation[p // 2], current_order_permutation[p])

			current_dict["board"] = current_board.copy_board()
			current_dict[current_order_permutation[p]] = {}
			current_dict = current_dict[current_order_permutation[p]] 

		winner = current_board.check_winner(first_play)
		if winner == 1:
			blue_wins +=1
		elif winner == 2:
			red_wins +=1
		elif winner == 3:
			draws += 1
	print(blue_wins, red_wins, draws)
	return(blue_wins, red_wins, draws)

def simulate_no_rules(blue_deck, red_deck, first_play=0):
	blue_wins = 0
	red_wins = 0
	draws = 0
	# Flip coin to see who plays first
	if first_play == 0:
		first_play = random.randint(1, 2)
	if (first_play == 1):
		print("Blue plays first")
	else:
		print("Red plays first")
	first_deck = blue_deck if first_play == 1 else red_deck
	second_deck = blue_deck if first_play == 2 else red_deck
	first_possible_play_permutations = list(itertools.permutations(first_deck))
	second_possible_play_permutations = list(itertools.permutations(second_deck, 4))
	spot_order_permutations = list(itertools.permutations([(0, x) for x in range(0, 3)] + [(1, x) for x in range(0,3)] + [(2, x) for x in range(0,3)]))
	deck_combinations = []
	# Pull a permuation from each
	print(len(first_possible_play_permutations), len(second_possible_play_permutations), len(spot_order_permutations))
	for i in range(0, len(first_possible_play_permutations)):
		for j in range(0, len(second_possible_play_permutations)):
			deck_combinations.append((first_play, first_possible_play_permutations[i], second_possible_play_permutations[j], spot_order_permutations))
			# play_permutations(first_play, first_possible_play_permutations[i], second_possible_play_permutations[j], spot_order_permutations)
	# for i in range(1):
	# 	Process(target=play_permutations, args=deck_combinations[i]).start()
	with Pool(processes=8) as pool:
		pool.starmap(play_permutations, deck_combinations)
			
	return(blue_wins, red_wins, draws)

