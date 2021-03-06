from Treasure import*
from Fight import*

class room:
	def __init__(self, name="", status="", coordinate=[], edge=False):
		self.name = name

		self.room_character = "O"
		self.edge_character = " "
		self.mark_character = "X"
		self.room_finished_character = "Ø"
		self.room_unfinished_character = "o"
		self.total_loot = self.treasure()

		self.status = status
		self.coordinate = coordinate
		self.edge = self.if_edge()
		self.hero = None
		self.fight = None
		
	def room_characters_index(self):
		room_index_dictionary = {
			"room_character": self.room_character,
			"edge_character": self.edge_character,
			"mark_character": self.mark_character,
			"room_finished_character": self.room_finished_character,
			"room_unfinished_character": self.room_unfinished_character
		}
		return room_index_dictionary

	def is_here(self):
		self.status = self.mark_character

	def unfinished(self):
		self.status = self.room_unfinished_character

	def finished(self):
		self.status = self.room_finished_character

	def is_edge(self):
		self.status = self.edge_character

	def fight_generator(self, hero_instance, is_ai=False):
		# method for fight initialize if room follow criterias

		if self.status == self.room_finished_character: # no fight if room is finished
			self.fight = False
			return self.fight

		elif self.status == self.edge: # no fight if room is edge
			self.fight = False
			return self.fight

		# elif self.status == self.room_unfinished_character: # return the fight instance if unfinished room
		# 	return self.fight

		# elif self.status == self.room_character: # returns the fight instance
		else:
			new_fight = Fight(hero=hero_instance, is_Ai=is_ai)
			self.fight = new_fight
			return self.fight
			
		
	def treasure(self):
		# metod for trease initialize
		t = Treasure()
		return t.generate_treasure()
		#h.hero_total_loot = self.total_loot

	def get_coordinate(self):
		return self.coordinate

	def if_edge(self):
		# method for checking if the room is an edge
		if self.status == self.edge_character:
			self.fight = False
			return True
		else:
			return False
	
if __name__ == "__main__":

	def grid_generator(grid_size_with_edge=6):
		# generates two grids, one grid with all the symbols of the

		number = grid_size_with_edge
		rooms_grid = []

		for y in range(number):
			row_rooms = []
			for x in range(number):
				if x is not 0 and x is not max(range(number)):
					if y is not 0 and y is not max(range(number)):
						z = x + y
						z = room(coordinate=[y, x], status=room().room_character, edge=False)
						row_rooms.append(z)
					else:
						z = x + y
						z = room(coordinate=[y, x], status=room().edge_character, edge=True)
						row_rooms.append(z)
				else:
					z = x + y
					z = room(coordinate=[y, x], status=room().edge_character, edge=True)
					row_rooms.append(z)

			rooms_grid.append(row_rooms)

		return rooms_grid

	def print_map(arrays):
		print()
		visual_grid = []

		for y in arrays:
			rows = []
			for instance in y:
				rows.append(instance.status)
			visual_grid.append(rows)

		for row in visual_grid:
			print(" ".join(row))


	def update_room(grid, coordinate, update=""):
		if update == "unfinished":
			grid[coordinate[0]][coordinate[1]].unfinished()
		elif update == "finished":
			grid[coordinate[0]][coordinate[1]].finished()
		elif update == "is_here":
			grid[coordinate[0]][coordinate[1]].is_here()
		elif update == "edge":
			grid[coordinate[0]][coordinate[1]].edge()

	x = grid_generator()
	# print_map(x)
	update_room(grid=x, coordinate=[1, 1], update="finished")
	# print_map(x)
	update_room(grid=x, coordinate=[2, 1], update="is_here")
	print_map(x)
