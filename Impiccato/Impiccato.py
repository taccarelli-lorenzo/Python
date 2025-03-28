import os
import json
import random
import tkinter as tk
from tkinter import messagebox

class ImpiccatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Impiccato")
        
        self.parola = ""
        self.parola_nascosta = ""
        self.lettere = []
        self.tentativi_falliti = 0
        self.max_tentativi = 7
        
        self.setup_ui()
        self.carica_dati()
        self.nuova_partita()
        
        
        
    def setup_ui(self):
        self.label_parola = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.label_parola.pack(pady=20)
        
        self.label_tentativi = tk.Label(self.root, text="Tentativi falliti: 0", font=("Helvetica", 14))
        self.label_tentativi.pack(pady=10)
        
        self.entry_lettera = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry_lettera.pack(pady=10)
        
        self.button_invia = tk.Button(self.root, text="Invia", command=self.verifica_lettera, font=("Helvetica", 14))
        self.button_invia.pack(pady=10)
        
        self.label_lettere_rimaste = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.label_lettere_rimaste.pack(pady=10)
        
        
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
        
    