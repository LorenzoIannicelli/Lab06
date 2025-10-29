class Automobile:
    def __init__(self, codice, marca, modello, anno, posti, disponibile):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.posti = int(posti)
        self.disponibile = disponibile

    def __eq__(self, other):
        return isinstance(other, Automobile) and self.codice == other.codice

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"

    def __repr__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"
