import random


def main():
    print("-- Starting New Game")
    gender = ask_gender("> Please select your character's gender (M/F): ")
    name = ask_input("str", "> Please enter a name for your character: ")
    player = Player(gender, name)
    # weapon = Weapon("Wooden Sword", 30, 10)
    print(
        "\n-- This is the story of the brave {player_name}, {pronoun} travelled "
        "through the lands of Codia in search of epic treasure") \
        .format(player_name=player.name, pronoun=player.gender.he_she)
    day = 0
    while player.health > 0:
        day += 1
        player.show_stats()
        print("\n- Day {day_number}:".format(day_number=day))
        generate_next_event(player)
        print("- End of day {day_number}:".format(day_number=day))

    print("\n-- {player_name} died on day {day}, game over...".format(player_name=player.name,
                                                                      player_xp=player.xp, day=day))
    if player.xp == 0:
        player.xp = 1
    print("Your score was: {}".format(player.xp * day))


def ask_gender(message):
    # return "M"
    value = raw_input(message).upper()
    if value.isalpha() and (value == "M" or value == "F"):
        return value
    else:
        print("-- Please choose between M or F")
        return ask_input(type, message)


def ask_reaction(message):
    # reactions = ("attack", "flee", "intimidate")
    # return "attack"
    # return reactions[random.randint(0, reactions.__len__() - 1)]
    value = raw_input(message).lower()
    if value.isalpha() and (value == "attack" or value == "flee" or value == "inventory" or value == "intimidate"):
        return value
    else:
        print "-- Please choose one of the available options"
        return ask_reaction(message)


def ask_input(input_type, message):
    # return "Tester"
    value = raw_input(message)
    if input_type == "int":
        try:
            return int(value)
        except ValueError:
            print "-- Invalid number!"
            return ask_input(input_type, message)
    elif input_type == "str":
        if value.isalpha():
            return value
        else:
            print "-- Please only use letters"
            return ask_input(input_type, message)


def generate_next_event(p):
    i = random.randint(0, 100)
    if i < 50:
        event = MonsterEvent(p)
    # elif i > 90:
    #    event = ItemEvent(p)
    else:
        event = MiscEvent(p)

    return event


class MonsterEvent:
    def __init__(self, p):
        self.monster = Monster(p)
        print(
            "-- {player_name} stumbled upon a {monster_name} with power level {monster_power}".format(
                    player_name=p.name,
                    monster_name=self.monster.name,
                    monster_power=(
                                      random.randint(
                                              int(
                                                      p.level / 1.2),
                                              int(
                                                      p.level / 1.2))) + 1))
        self.in_event = True
        while self.in_event and self.monster.health > 0 and p.health > 0:
            print("|  {monster_name}'s stats:".format(monster_name=self.monster.name))
            print("|  HP: {monster_hp}".format(monster_hp=self.monster.health))
            print("|  Attack Damage: {monster_ad}".format(monster_ad=self.monster.attack))
            # p.take_damage(monster.attack)
            p.do_reaction(p.show_options(), self)
            if self.monster.health > 0 and self.in_event is True:
                if self.monster.attack > 0:
                    self.monster.do_attack(p)
                else:
                    p.do_attack(self.monster)
                    print("-- The {} could no longer attack and {} finished it off".format(self.monster.name, p.name))
                    gained_xp = (self.monster.init_health * self.monster.attack) / 3
                    p.xp += gained_xp
                    print("-- {} gained {} XP for killing the {} (Total XP: {})".
                          format(p.name, gained_xp, self.monster.name, p.xp))
                if self.monster.health <= 0:
                    print("-- The {} died".format(self.monster.name))


class Monster:
    def __init__(self, p):
        name1 = ("Gargling ", "Huge ", "Tiny ", "Massive ", "Vicious ", "")
        name2 = ("Troll", "Robot", "Goblin", "Raider", "Gnome", "Baby")
        self.name = ("{}{}".format(name1[random.randint(0, name1.__len__()) - 1],
                                   name2[random.randint(0, name1.__len__()) - 1]))
        self.max_health = int((p.level * 1.4) + ((p.base_attack * p.level) * 5))
        self.health = random.randint(10, self.max_health)
        self.init_health = self.health
        self.attack = random.randint(1, int(p.base_health / 10))

    def do_attack(self, p):
        print("-- {} attacked".format(self.name)),
        amount = self.attack
        # p.take_damage(self, self.attack)
        if random.randint(0, 100) >= 8:
            print("and dealt"),
            if random.randint(0, 100) <= 8:
                amount *= 2
                print("{} damage (critical hit!)".format(amount)),
            else:
                print("{} damage".format(amount)),
            print("to {}".format(p.name))
            p.take_damage(amount)
        else:
            print("and missed")


class ItemEvent:
    def __init__(self, p):
        print("Item!")
        self.powerLevel = p.level


class MiscEvent:
    def __init__(self, p):
        misc_type = random.randint(0, 100)
        if misc_type <= 30 and p.health != p.base_health:
            print("-- {} found a mystical flower that restored {} health".format(p.name, p.gender.his_her))
            p.health = p.base_health
        elif 31 <= misc_type <= 60:

            damage = random.randint(1, 5)
            print("-- {} ate a poisonous berry that did {} damage".format(p.name, damage))
            p.take_damage(damage)

        else:
            print("-- {} had a quiet day, nothing happened".format(p.name))
        self.powerLevel = p.level


class Player:
    def __init__(self, g, n):
        self.name = n
        self.gender = Gender(g)
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.health = 50
        self.base_health = 50
        self.eventsDone = 0
        self.base_attack = 5

    def take_damage(self, amount):
        if amount > self.health:
            amount = self.health
        self.health -= amount
        if self.health > 0:
            print("|  {}'s remaining health: {health}".format(self.name, health=self.health))

    def show_options(self):
        print("-- How does {} act?".format(self.name))
        print("-- Options are: Attack (94% chance) | Intimidate (35% chance) | Flee (65% chance)")
        reaction = ask_reaction("> Enter your choice: ")
        return reaction

    def do_attack(self, monster):
        damage = int(random.randint((int((self.base_attack * (0.8 * self.level)) / 1.2)),
                                    (int((self.base_attack * (0.8 * self.level)) * 1.2))))
        if monster.attack == 0:
            damage = monster.health
        if monster.health < damage:
            damage = monster.health
        monster.health -= damage
        return damage

    def do_reaction(self, reaction, event):
        monster = event.monster
        if reaction == "attack":
            attack = self.do_attack(monster)
            print("-- {} attacked and did {} damage to the {}".format(self.name, attack, monster.name))
            if event.monster.health <= 0:
                print("-- {} killed the {}!".format(self.name, monster.name))
                gained_xp = (event.monster.init_health * event.monster.attack) / 3
                self.xp += gained_xp
                print("-- {} got {} XP for killing the monster (Total XP: {})".format(self.name, gained_xp, self.xp))
        elif reaction == "flee":
            # print("-- {} chose to {}".format(self.name, reaction))
            if random.randint(0, 100) <= 65:
                print("-- {} fled from the monster".format(self.name))
                event.in_event = False
            else:
                print("-- {} could not escape the monster".format(self.name))
        elif reaction == "inventory":
            print("-- {} chose to {}".format(self.name, reaction))
        elif reaction == "intimidate":
            # print("-- {} chose to {}".format(self.name, reaction))
            if random.randint(0, 100) <= 35:
                print("-- {} intimidated the {} and its Attack Damage halved!".format(self.name, event.monster.name))
                event.monster.attack /= 2
            else:
                print("-- {} shouted at the {}, but it was not intimidated".format(self.name, event.monster.name))

    def show_stats(self):
        print
        if self.xp > ((self.level * self.level) * self.level):
            print("--  {} levelled up".format(self.name)),
            while self.xp > ((self.level * self.level) * self.level):
                self.level += 1
            print("to level {}!".format(self.level))
        print("|  {}'s stats:".format(self.name))
        print("|  HP: {}".format(self.health))
        print("|  Base Attack Damage: {}".format(self.base_attack * self.level))
        print("|  Level: {}".format(self.level))
        print("|  XP: {}".format(self.xp))
        print("|  XP needed for level up: {}".format((self.level * self.level) * self.level))


class Gender:
    def __init__(self, g):
        if g == "M":
            self.he_she = "he"
            self.his_her = "his"
        else:
            self.he_she = "she"
            self.his_her = "her"


class Weapon:
    def __init__(self, n, p, d):
        self.name = n
        self.power = p
        self.durability = d


class Item:
    def __init__(self):
        pass


class Potion:
    def __init__(self):
        pass


if __name__ == "__main__":
    main()


class Area:
    def __init__(self):
        pass
