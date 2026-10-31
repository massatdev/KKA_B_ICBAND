import string

elements = ["Pyro", "Hydro", "Electro", "Anemo", "Geo", "Dendro", "Cryo"]

class Boss:
    def __init__(self, name, max_health, dps, defense, element):
        self.name = name
        self.max_health = max_health
        self.dps = dps
        self.defense = defense
        self.element = element

    def display_info(self):
        print(f"Boss Name: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Damage Per Second: {self.dps}")
        print(f"Defense: {self.defense}")
        print(f"Element: {self.element}")