# Вычисление чисел Фибоначчи
from functools import lru_cache
from typing import Dict

# Бесконечная рекурсия- нет базового случая


def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


# Классическая реализация
# n=50 уже не работает, слишком много вызов
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


# Мемоизация
# Запоминаем результаты всех вызовов
memo: Dict[int, int] = {0: 0, 1: 1}         # два базовых случая


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


# Автоматическая мемоизация с помощью декоратора
@lru_cache(maxsize=None)
def fib4(n: int) -> int:                    # Точно такая же реализация, как в классической реализации
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)


if __name__ == '__main__':
    print(fib4(50))
