import character

def main():
    with open("chara.txt", "r") as file:
        for line in file:
            name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element = line.strip().split(",")
            char = character.Character(name, max_health, atk, defense, crit_chance, crit_damage, elemental_bonus, element)
            char.display_info()

if __name__ == "__main__":
    main()