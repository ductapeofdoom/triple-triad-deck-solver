from dataclasses import dataclass
import struct

CARD_BIT_LENGTH = 10

@dataclass
class Card:
	name: str # Name of the card
	stars: int # Star level of the card
	top: int # Top number of the card
	right: int # Right number of the card
	bottom: int # Bottom number of the card
	left: int # Left number of the card
	owner: int # Owner of the card; 1 for blue, 2 for red

	def bit_encode(self):
		# Owner, Top, Right, Bottom, Left
		return struct.pack(">hhhhh", self.owner, self.top, self.right, self.bottom, self.left)

	def __str__(self):
		return "{}\n{}\n".format(self.name, self.stars)