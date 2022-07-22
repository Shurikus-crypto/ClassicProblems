# Вычисление чисел Фибоначчи

# Бесконечная рекурсия- нет базового случая
def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


# Классическая реализация
# n=50 уже не работает, слишком много вызов
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


if __name__ == '__main__':
    print(fib2(10))