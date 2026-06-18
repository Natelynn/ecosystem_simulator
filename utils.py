"""Модуль со вспомогательными функциями для симуляции."""

import random
from typing import Tuple


def get_weather_impact() -> Tuple[str, int]:
    """Генерирует случайные погодные условия и их влияние на потерю энергии.

    Returns:
        Кортеж (название погоды, штраф к энергии).
    """
    conditions = {
        "Солнечно и тепло": 5,
        "Проливной дождь": 10,
        "Засуха": 15
    }
    weather = random.choice(list(conditions.keys()))
    return weather, conditions[weather]
