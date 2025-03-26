import os
import json
import random

def main():
    
    parolaCreata = ""
    print("Benvenuto in Impiccato!")
    
    file_path = os.path.join(os.path.dirname(__file__), 'parole.json')
    
    try:
        with open(file_path, 'r') as fileParole:
            parole = json.load(fileParole)
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
        
    parola = random.choice(parole)
    print(parola)
    
    parolaNascosta = "_" * len(parola)
    print(parolaNascosta)
    
    print("Scegli una lettera tra quelle rimaste: ")
    print(lettere)
    
    scelta = input()
    
    if scelta in parola: 
        print("Lettera presente")
    
    
    
    
        
if __name__ == "__main__":
    main()