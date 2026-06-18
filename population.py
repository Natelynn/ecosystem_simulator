"""Модуль для управления группами (популяциями) организмов."""

from typing import List
# Импортируем классы строго из файла organism
from organism import Herbivore, Predator


class Population:
    """Класс, группирующий организмы по типам и управляющий ими."""

    def __init__(self):
        """Инициализация пустых списков популяций."""
        self.herbivores: List[Herbivore] = []
        self.predators: List[Predator] = []

    def add_herbivore(self, animal: Herbivore) -> None:
        """Добавляет травоядное в популяцию."""
        self.herbivores.append(animal)

    def add_predator(self, animal: Predator) -> None:
        """Добавляет хищника в популяцию."""
        self.predators.append(animal)

    def clean_dead(self) -> None:
        """Удаляет мертвые организмы из списков популяций."""
        self.herbivores = [h for h in self.herbivores if h.is_alive()]
        self.predators = [p for p in self.predators if p.is_alive()]
