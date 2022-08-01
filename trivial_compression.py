# Простейшее сжатие (битовая упаковка генов)

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
