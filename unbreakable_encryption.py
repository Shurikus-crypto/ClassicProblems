# Невскрываемое шифрование с помощью оператора XOR
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """  Функция возвращает одно целое число,
         образованное из n случайных байт.

         :param length: количество байт
         :type length: int
         :return: образованное число
         :rtype: int
    """
    tb: bytes = token_bytes(length)
    # сейчас преобразуем эту строку в целое число
    return int.from_bytes(tb, 'big')


def encrypt(original: str) -> Tuple[int, int]:
    """  Шифрует строку методом XOR

         :param original: шифруемая строка
         :type original: str
         :return: возвращает кортеж со значениями ключ шифрования и зашифрованную строку
         :rtype: Tuple(int, int)
        """
    original_bytes: bytes = original.encode()                   # строку в байты
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, 'big')   # из строки байтов в целое
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    """  Дешифрует строку методом XOR

         :param key1: ключ шифрования
         :type key1: int

         :param key2: зашифрованная строка (порядок не имеет значения)
         :type key2: int
         :return: оригинальная строка
         :rtype: str
    """
    decrypted: int = key1 ^ key2                                # обратная операция
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, 'big')  # из целого в байты
    return temp.decode()    # из байтов в строку


def main(original: str):
    key1, key2 = encrypt(original)
    decrypted = decrypt(key1, key2)
    print(decrypted)
    print(decrypted == original)


if __name__ == '__main__':
    main('It work!')
