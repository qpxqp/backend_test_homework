from math import sqrt
from typing import Optional


def add_numbers(x_val: int, y_val: int) -> int:
    return x_val + y_val


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    root: float = calculate_square_root(your_number)
    return (
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {root}'
    )


x_value: int = 10
y_value: int = 5
print('Сумма чисел: ', add_numbers(x_value, y_value))
print(calc(25.5))
