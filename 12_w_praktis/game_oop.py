class Character:
    def __init__(self, health, attack, name):
        self.health = health
        self.attack = attack
        self.name = name

    def fight(self, opponent):
        """این شخصیت به دیگری حمله می‌کند"""
        print(f"{self.name} attacks {opponent.name} with {self.attack} damage!")
        opponent.health -= self.attack
        if opponent.health <= 0:
            print(f"{opponent.name} is defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")


class Warrior(Character):
    def __init__(self):
        # مقداردهی اولیه برای واریر
        super().__init__(health=150, attack=25, name="Warrior")


class Mage(Character):
    def __init__(self):
        # مقداردهی اولیه برای مجی
        super().__init__(health=100, attack=40, name="Mage")

# ساخت دو شخصیت
warrior = Warrior()
mage = Mage()

# شروع نبرد!
warrior.fight(mage)
mage.fight(warrior)
warrior.fight(mage)
mage.fight(warrior)
warrior.fight(mage)