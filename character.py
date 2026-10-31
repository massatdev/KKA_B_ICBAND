import string

elements = ["Pyro", "Hydro", "Electro", "Anemo", "Geo", "Dendro", "Cryo"]

class Character:
    def __init__(self, name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element):
        self.name = name
        self.max_health = max_health
        self.atk = atk
        self.defense = defense
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.elemental_bonus = elemental_bonus
        self.element = element
        self.type = "DPS"

    def display_info(self):
        print(f"Character Name: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Attack: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"Critical Chance: {self.crit_chance}")
        print(f"Critical Damage: {self.crit_damage}")
        print(f"Elemental Bonus: {self.elemental_bonus}")
        print(f"Element: {self.element}")
        print(f"Type: {self.type}")

    def calculate_damage(self):
            base_damage = self.atk * (1 + self.elemental_bonus)
            crit_hits = base_damage * self.crit_damage
            total_damage = (crit_hits * self.crit_chance) + (base_damage * (1 - self.crit_chance))
            return total_damage
    
    def display_dps(self):
        damage = self.calculate_damage()
        print(f"{self.name} deals {damage:.2f} damage per attack.")

class HealingCharacter(Character):
    def __init__(self, name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element):
        super().__init__(name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element)
        self.type = "Healer"

    def calculate_healing(self):
        base_healing = self.max_health * 0.2
        return base_healing / 2

    def display_healing(self):
        healing = self.calculate_healing()
        print(f"{self.name} heals for {healing:.2f} health per second.")

class BuffCharacter(Character):
    def __init__(self, name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element):
        super().__init__(name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element)
        self.type = "Buff"

    def apply_buff(self):
        buff_amount = self.atk * 0.4 
        return buff_amount / 100

    def display_buff(self):
        buff = self.apply_buff()
        print(f"{self.name} provides a buff of {buff:.2f} to allies.")