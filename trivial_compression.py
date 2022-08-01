# Простейшее сжатие (битовая упаковка генов)
from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1                    # начальная метка
        for nucleotide in gene.upper():
            self.bit_string <<= 2                   # сдвиг влево на два бита
            if nucleotide == "A":
                self.bit_string |= 0b00             # поменять два последних бита на 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")

    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length()-1, 2):   # -1 чтобы исключить метку
            bits: int = self.bit_string >> i & 0b11             # получить только 2 значимых бита
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f'Invalid bits: {bits}')
        return gene[::-1]                                       # обращение строки

    def __str__(self) -> str:                                   # строковое представление объекта
        return self.decompress()


if __name__ == '__main__':
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100

    print(f'Original is {getsizeof(original)} bytes')
    compressed: CompressedGene = CompressedGene(original)               # сжатие
    print(f'Compressed is {getsizeof(compressed.bit_string)} bytes')
    print(compressed)                                                   # строковое представление (распаковка)
    print(f'Original and decompressed are the same: {(original == compressed.decompress())}')
