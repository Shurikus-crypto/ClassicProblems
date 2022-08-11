# Невскрываемое шифрование с помощью оператора XOR
from secrets import token_bytes


def random_key(length: int) -> int:
    """" Функция возвращает одно целое случайное число,
         размером => length байт """
    tb: bytes = token_bytes(length)
    # сейчас преобразуем эту строку в битову строку
    return int.from_bytes(tb, 'big')
