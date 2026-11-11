#Calcolatore in python

#Funzione somma
class Somma:
    def __init__(self, *valori):
        self.valori = valori

    def esegui(self):
        for v in self.valori:
            somma += v;

        return somma;

#Funzione divisione
#Errore per divisore = 0
class Divisione:
    def __init__(self, dividendo, divisore):
        self.dividendo = dividendo
        self.divisore = divisore

    def esegui(self):
        if self.divisore == 0:
            raise ValueError("Non si può dividere per zero")
        else:
            return self.dividendo / self.divisore