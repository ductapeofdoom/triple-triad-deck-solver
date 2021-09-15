import requests
import random
import itertools
import copy
import cProfile
import math
from Card import Card
from simulate import *


BASE_URL = "https://triad.raelys.com/api"
NPC_ENDPOINT = BASE_URL + "/npcs" 
MERMOON_ID = "2293762"
CARD_ENDPOINT = BASE_URL + "/cards"
THREE_STAR_OR_LESS_QUERY = CARD_ENDPOINT + "?stars_lteq=3&language=en"
FOUR_AND_FIVE_STAR_QUERY = CARD_ENDPOINT + "?stars_gt=3&language=en"


def big_loop():
	for i in range(math.factorial(5) * math.factorial(4) * math.factorial(9)):
		pass

def make_random_deck(three_star_cards, four_plus_cards, owner):
	deck = []
	three_stars = random.sample(three_star_cards, 4)
	four_plus_stars = random.sample(four_plus_cards, 1)
	for card in three_stars:
		deck.append(Card(card["name"], card["stars"], card["stats"]["numeric"]["top"], card["stats"]["numeric"]["right"], card["stats"]["numeric"]["bottom"], card["stats"]["numeric"]["left"], owner))
	for card in four_plus_stars:
		deck.append(Card(card["name"], card["stars"], card["stats"]["numeric"]["top"], card["stats"]["numeric"]["right"], card["stats"]["numeric"]["bottom"], card["stats"]["numeric"]["left"], owner))
	return deck

def json_to_card(deck, owner):
	converted_deck = []
	for card in deck:
		converted_deck.append(Card(card["name"], card["stars"], card["stats"]["numeric"]["top"], card["stats"]["numeric"]["right"], card["stats"]["numeric"]["bottom"], card["stats"]["numeric"]["left"], owner))
	return converted_deck

def build_npc_decks(npc_id):
	decks = []
	npc_data = requests.get(NPC_ENDPOINT + "/{}?deck=1".format(npc_id)).json()
	npc_fixed_cards = npc_data["fixed_cards"]
	npc_variable_cards = npc_data["variable_cards"]
	possible_variants = itertools.combinations(npc_variable_cards, 5-len(npc_fixed_cards))
	for variant in possible_variants:
		current_deck = npc_fixed_cards + list(variant)
		decks.append(current_deck)
	return decks

def bit_encode_deck(deck):
	new_deck = []
	for card in deck:
		new_deck.append(card.bit_encode())
	return new_deck

if __name__ == "__main__":
	# mermoon = requests.get(MERMOON_URL).json()
	# print(mermoon)
	three_star_cards = requests.get(THREE_STAR_OR_LESS_QUERY).json()["results"]
	four_plus_cards = requests.get(FOUR_AND_FIVE_STAR_QUERY).json()["results"]
	blue_deck = make_random_deck(three_star_cards, four_plus_cards, 1)
	# red_deck = []
	# for card in blue_deck:
	# 	new_card = copy.deepcopy(card)
	# 	new_card.owner = 2
	# 	red_deck.append(copy.deepcopy(new_card))
	red_deck = make_random_deck(three_star_cards, four_plus_cards, 2)
	# print(blue_deck)
	# print(red_deck
	# print(simulate_no_rules(bit_encode_deck(blue_deck), bit_encode_deck(red_deck)))
	# cProfile.run('big_loop()')
	# mermoon_decks = build_npc_decks(MERMOON_ID)
	# mermoon_blue = []
	# mermoon_red = []
	# for deck in mermoon_decks:
	# 	mermoon_blue.append(json_to_card(deck, 1))
	# 	mermoon_red.append(json_to_card(deck, 2))
	# for deck in mermoon_red:
	# 	# print(deck)
	# 	print(simulate_no_rules(blue_deck, deck))
	spot_order_permutations = list(itertools.permutations([(0, x) for x in range(0, 3)] + [(1, x) for x in range(0,3)] + [(2, x) for x in range(0,3)]))
	print(len(spot_order_permutations))
	cProfile.run('play_permutations(1, bit_encode_deck(blue_deck), bit_encode_deck(red_deck), spot_order_permutations)')