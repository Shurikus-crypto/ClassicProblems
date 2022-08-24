# Невскрываемое шифрование с помощью оператора XOR
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """" Функция возвращает одно целое случайное число,
         размером => length байт """
    tb: bytes = token_bytes(length)
    # сейчас преобразуем эту строку в целое число
    return int.from_bytes(tb, 'big')


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()                   # строку в байты
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, 'big')   # из строки байтов в целое
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1:int, key2: int) -> str:
    decrypted: int = key1 ^ key2                                # обратная операция
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, 'big')  # из целого в байты
    return temp.decode()    # из байтов в строку

