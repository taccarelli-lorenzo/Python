import os
import json
import random
import string

def main():
    
    parolaCreata = ""
    trovato = False
    tentativiFalliti = 0
    
    print("Benvenuto in Impiccato!")
    
    file_path = os.path.join(os.path.dirname(__file__), 'parole.json')
    
    try:
        with open(file_path, 'r') as fileParole:
            paroleTot = json.load(fileParole)
    except FileNotFoundError:
        print("Errore: File 'products.json' non trovato nella directory:", os.path.abspath(file_path))
    except json.JSONDecodeError:
        print("Errore: Il file non contiene JSON valido")
    except Exception as e:
        print(f"Errore sconosciuto: {type(e).__name__}: {e}")
    
    file_path = os.path.join(os.path.dirname(__file__), 'lettere.json')
    
    try:
        with open(file_path, 'r') as fileLettere:
            lettere = json.load(fileLettere)
    except FileNotFoundError:
        print("Errore: File 'products.json' non trovato nella directory:", os.path.abspath(file_path))
    except json.JSONDecodeError:
        print("Errore: Il file non contiene JSON valido")
    except Exception as e:
        print(f"Errore sconosciuto: {type(e).__name__}: {e}")
        
    parola = random.choice(paroleTot)
    print(parola)
    
    parolaNascosta = "_" * len(parola)
    print(parolaNascosta)
    
    while not trovato and tentativiFalliti < 7:
        print(lettere)
        print()
    
        scelta = input(f"Scegli una lettera tra quelle rimaste: ")
        print()
    
        if scelta.upper() in lettere:
            lettere.remove(scelta.upper())
            if scelta not in parola:  # Increment tentativiFalliti if the guess is incorrect
                tentativiFalliti += 1
                print(f"Lettera sbagliata! Tentativi falliti: {tentativiFalliti}")
        else:
            print(f"La lettera '{scelta}' non è valida o è già stata usata. Riprova.")
    
        for x, char in enumerate(parola):
            if char == scelta:
                parolaNascosta = parolaNascosta[:x] + scelta + parolaNascosta[x+1:]
    
        print(parolaNascosta)
        
        if parolaNascosta == parola:
            trovato = True
            print()
            print("Parola trovata!")
            print(parolaNascosta)
        
    
    
    
    
        
if __name__ == "__main__":
    main()