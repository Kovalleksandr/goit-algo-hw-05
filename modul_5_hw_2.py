import re
from typing import Callable

def generator_numbers(text: str):
       for match in re.finditer(r' (?P<number>\d+\.\d+) ', text):  # Шукаємо числа, відокремлені пробілами
        yield float(match.group("number"))  # Перетворюємо знайдене число у float і повертаємо

def sum_profit(text: str, func: Callable):
       return sum(func(text))  # Використовує генератор і сумує його значення


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

