"""Главный файл запуска консольного симулятора жизни."""

import time
from organism import Herbivore, Predator
from population import Population
from ecosystem import Ecosystem


def main() -> None:
    """Основная функция для инициализации и запуска симуляции."""
    # Инициализируем популяции
    pop = Population()

    # Заселяем экосистему жителями
    pop.add_herbivore(Herbivore("Заяц-01", 20))
    pop.add_herbivore(Herbivore("Заяц-02", 25))
    pop.add_herbivore(Herbivore("Олень", 40))

    pop.add_predator(Predator("Волк", 30))
    pop.add_predator(Predator("Лиса", 20))

    # Создаем экосистему
    eco = Ecosystem(pop)

    # Цикл симуляции на 5 дней
    for _ in range(5):
        eco.simulate_day()
        time.sleep(1)  # Пауза для читаемости вывода в консоли

    print("\n=== Симуляция завершена ===")


if __name__ == "__main__":
    main()
