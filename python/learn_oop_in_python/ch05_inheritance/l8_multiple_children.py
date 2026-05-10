#!/usr/bin/env python3

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows


    def shoot(self, target):
        if self.__num_arrows == 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)

# Testing code (add this below your classes)
# Step 1: Create a Hero instance as the target
target_hero = Hero("Hercules", 100)

# Step 2: Create an Archer instance with 2 arrows
archer = Archer("Apollo", 50, 2)

# Step 3: Call shoot twice
print(f"Target's health before the first shot: {target_hero.get_health()}")
archer.shoot(target_hero)
print(f"Target's health after the first shot: {target_hero.get_health()}")

print(f"Target's health before the second shot: {target_hero.get_health()}")
archer.shoot(target_hero)
print(f"Target's health after the second shot: {target_hero.get_health()}")

# Step 4: Try a third shot (should raise an exception)
try:
    archer.shoot(target_hero)
except Exception as e:
    print(f"Exception caught: {e}")