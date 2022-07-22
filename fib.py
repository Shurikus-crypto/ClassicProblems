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


# Итеративный способ
def fib5(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, next + last
        # new_next = next + last
        # last = next
        # next = new_next
    return next


# Генератор чисел Фибоначчи
def fib6(n: int) -> int:
    # специальный случай (возвращаем 0, но не покидаем функции - следующий вызов функции со след. строки)
    yield 0                     # fib(0)

    if n > 0:                   # fib(1)
        yield 1

    last: int = 0               # начальное значение fib(0) - уже прошли, см. выше
    next: int = 1               # начальное значение fib(1) - уже прошли, см. выше
    for _ in range(1, n):
        last, next = next, next + last
        yield next


if __name__ == '__main__':
    print('Iterator = ', fib5(10))
    print('\n From generator = ')
    for i in fib6(10):
        print(i)
