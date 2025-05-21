import random
import json

""" num_articoli = int(input("Inserisci la quantita di articoli acquistati: "))

prezzo = 0 
    
while prezzo <= 0:
    prezzo = float(input("Inserisci il prezzo unitario (Maggiore di 0): "))
    
prezzo = (prezzo * num_articoli)

prezzoTot = prezzo + (prezzo*0.22)

print(f"Il totale da pagare e", prezzoTot) """ 



""" temperatura = int(input("Inserisci la temperatura in gradi Celsius: "))

if temperatura < 0:
    print("Temperatura sotto lo zero")
elif temperatura == 0:
    print("Punto di congelamento dell'acqua")
elif temperatura >= 1 and temperatura <= 30:
    print("Temperatura normale")
else:
    print("Giornata calda") """
    
""" numeri = [4, 6, 7, 9, 10, 12, 13]

for n in numeri:
    if n % 3 == 0:
        print(n) """



""" def quadrato_somma(x, y):
    somma = x + y
    risultato = somma ** 2
    return risultato

print(quadrato_somma(2, 3)) """

""" def filtra_maggiori_media(lista):

    nuova = []

    media = sum(lista) / len(lista)

    for x in lista:

        if x > media :

            nuova.append(x)

    return nuova """
    
""" titolo = "titolo"
autore = "autore"
prezzo = 0

class Libro:
    def __init__(self, titolo, autore, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo

class LibroScolastico(Libro):
    def __init__(self, titolo, autore, prezzo):
        super().__init__(titolo, autore, prezzo) """


""" dati = '{"nome": "Mario", "cognome": "Rossi", "eta": 30, "citta": "Roma"}'
dati_dict = json.loads(dati)
print(dati_dict)  # This will print a Python dictionary
print(dati)"""
