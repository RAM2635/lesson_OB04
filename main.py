from abc import ABC, abstractmethod
import random


# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def name(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        damage = random.randint(10, 20)
        return f"Боец наносит удар мечом на {damage} урона."

    def name(self):
        return "Меч"


class Bow(Weapon):
    def attack(self):
        damage = random.randint(5, 15)
        return f"Боец стреляет из лука на {damage} урона."

    def name(self):
        return "Лук"


# Класс монстра
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0


# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} меняет оружие на {self.weapon.name()}.")

    def attack_monster(self, monster: Monster):
        attack_result = self.weapon.attack()
        print(attack_result)

        # Извлекаем урон из сообщения
        damage = int(attack_result.split()[-2])  # Получаем значение урона из строки
        if monster.take_damage(damage):
            print("Монстр побежден!")
        else:
            print(f"Здоровье монстра осталось: {monster.health}")


# Шаг 4: Реализация боя
def main():
    # Создаём бойца и монстра
    fighter = Fighter("Воин", Sword())
    monster = Monster(18)  # Монстр с 18 единицами здоровья

    # Бой с мечом
    fighter.attack_monster(monster)

    # Смена оружия на лук
    fighter.change_weapon(Bow())

    # Бой с луком
    fighter.attack_monster(monster)


if __name__ == "__main__":
    main()
