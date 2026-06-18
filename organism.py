"""Модуль, содержащий классы живых организмов симуляции."""

import random


class Organism:
    """Базовый класс для всех живых существ."""

    def __init__(self, name: str, energy: int):
        """Инициализация организма."""
        self.name = name
        self.energy = energy
        self.alive = True

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм."""
        if self.energy <= 0:
            self.alive = False
        return self.alive

    def lose_energy(self, amount: int) -> None:
        """Уменьшает энергию организма."""
        self.energy -= amount
        if self.energy <= 0:
            self.alive = False


class Herbivore(Organism):
    """Класс травоядного животного (жертвы)."""

    def eat_plant(self, plant_energy: int) -> None:
        """Потребление растительной пищи."""
        if self.is_alive():
            self.energy += plant_energy
            print(f"  {self.name} поел травы. Энергия: {self.energy}")


class Predator(Organism):
    """Класс хищного животного."""

    def hunt(self, prey: Herbivore) -> bool:
        """Попытка поохотиться на травоядное животное."""
        if not self.is_alive() or not prey.is_alive():
            return False

        success = random.choice([True, False])
        if success:
            self.energy += prey.energy
            prey.lose_energy(prey.energy)
            print(f"  🔥 {self.name} успешно поохотился на {prey.name}!")
            return True

        self.lose_energy(5)
        print(f"  ❌ {self.name} упустил {prey.name}. Потеряно 5 энергии.")
        return False
