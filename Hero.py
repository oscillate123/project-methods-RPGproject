from numpy.random import choice

class Hero:
    def __init__(self, hero_name, initiative, health, attack, agility, score, type, start_score):
        self.start_score = start_score
        self.hero_name = hero_name
        self.initiative = initiative
        self.health = health
        self.attack = attack
        self.agility = agility
        self.score = score
        self.type = type
        self.dict = {"Name": hero_name, "Initiative": initiative, "Health": health, "Attack": attack, "Score": score, "Type": type}
        self.hero_total_loot = 0

    #def __str__(self):
        #return f"Type : {self.type}\nName : {self.hero_name}\nScore : {self.score}\n "

    def print_stats(self):
        print("-----------------")
        print(f"Class : {self.__class__.__name__}  ")
        print("-----------------\n")
        print(f"Name : {self.hero_name}\n")
        print(f"Initiative : {self.initiative}")
        print(f"Health : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Agility : {self.agility}")
        print("-----------------\n")

    def special_skill(self, round):
        pass

    def add_hero_dict(self, list):
        list.append(self.dict)

class Knight(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 5, 9, 6, 4, 0, "Knight", 0)

    def special_skill(self, round):
        self.agility = 1000

class Wizard(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 6, 4, 9, 5, 0, "Wizard", 0)

    def special_skill(self):
        escape_procent = 0.80
        return escape_procent

class Rouge(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name, 7, 5, 5, 7, 0, "Rouge", 0)

    def special_skill(self,):
        value_points = [True, False]
        probabilities = [0.25, 0.75]

        critical_or_not = choice(value_points, p=probabilities)

        return critical_or_not
