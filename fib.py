# Вычисление чисел Фибоначчи

# Бесконечная рекурсия- нет базового случая
def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)
