# Простейшее сжатие (битовая упаковка генов)

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string = 1                         # начальная метка
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
