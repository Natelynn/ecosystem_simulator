"""Модуль, координирующий взаимодействие между популяциями и средой."""

import random
from population import Population
from utils import get_weather_impact


class Ecosystem:
    """Класс экосистемы, моделирующий окружающую среду и шаги времени."""

    def __init__(self, population: Population):
        """Инициализация экосистемы.

        Args:
            population: Объект популяции с организмами.
        """
        self.population = population
        self.day_count = 0

    def simulate_day(self) -> None:
        """Моделирует один день из жизни экосистемы."""
        self.day_count += 1
        print(f"\n=== День {self.day_count} ===")

        # Влияние погоды (из utils.py)
        weather, energy_loss = get_weather_impact()
        print(f"Погода сегодня: {weather} (Базовая потеря энергии: {energy_loss})")

        # 1. Травоядные ищут еду (случайное количество энергии от травы)
        for herb in self.population.herbivores:
            herb.lose_energy(energy_loss)
            if herb.is_alive():
                plant_energy = random.randint(5, 15)
                herb.eat_plant(plant_energy)

        # 2. Охота хищников
        for pred in self.population.predators:
            pred.lose_energy(energy_loss)
            if pred.is_alive() and self.population.herbivores:
                # Выбираем случайную живую жертву
                target = random.choice(self.population.herbivores)
                pred.hunt(target)

        # 3. Итоги дня и очистка от погибших
        self.population.clean_dead()
        self.display_status()

    def display_status(self) -> None:
        """Выводит текущую статистику выживших в экосистеме."""
        print(f"Статистика экосистемы:")
        print(f"  Травоядных осталось: {len(self.population.herbivores)}")
        print(f"  Хищников осталось: {len(self.population.predators)}")
