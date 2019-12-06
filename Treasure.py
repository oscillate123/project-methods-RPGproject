from numpy.random import choice

class Treasure:
    def __init__(self):
        self.coins = 2
        self.moneybag = 6
        self.gold = 10
        self.rock = 14
        self.small_treasure_chest = 20

    def generate_treasure(self):

        total_loot = 0
        picked_points = []

        for i in range(6):

            value_points = [2, 6, 10, 14, 20, 0]
            probabilities = [0.4, 0.2, 0.15, 0.1, 0.05, 0.10]

            random_value = choice(value_points, p=probabilities)

            print(random_value)

            if random_value in picked_points:
                continue
            else:
                picked_points.append(random_value)
                total_loot += random_value

        print(total_loot)

        print(f"TOTAL LOOT : {total_loot}")

t = Treasure()
t.generate_treasure()
