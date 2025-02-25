# Lorenzo Taccarelli
# 4IA
# 26/02/2025
# OOP

class Veicolo:
    def __init__(self, marca, modello, anno, velocita_massima):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita_massima = velocita_massima
    def __str__(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Velocita massima: {self.velocita_massima}"

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_massima, numero_posti):
        super().__init__(marca, modello, anno, velocita_massima)
        self.numero_posti = numero_posti
    def __str__(self):
        return f"{super().__str__()}, Numero posti: {self.numero_posti}"
    
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, velocita_massima, tipo_casco):
        super().__init__(marca, modello, anno, velocita_massima)
        self.tipo_casco = tipo_casco
    def __str__(self):
        return f"{super().__str__()}, Tipo casco: {self.tipo_casco}"
    
def descrivi_veicolo(Veicolo):
    print(Veicolo)

x = Auto("Infinity", "Q50", 2016, 240, 5)
descrivi_veicolo(x)

y = Moto("Ducati", "Bella", 2024, 200, "Jet")
descrivi_veicolo(y)
