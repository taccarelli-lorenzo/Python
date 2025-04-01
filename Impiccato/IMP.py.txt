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
    
    def carica_dati(self):
        try:
            file_path_parole = os.path.join(os.path.dirname(__file__), 'parole.json')
            with open(file_path_parole, 'r') as file_parole:
                self.parole_tot = json.load(file_parole)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel caricamento delle parole: {e}")
            self.parole_tot = []
        
        try:
            file_path_lettere = os.path.join(os.path.dirname(__file__), 'lettere.json')
            with open(file_path_lettere, 'r') as file_lettere:
                self.lettere = json.load(file_lettere)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nel caricamento delle lettere: {e}")
            self.lettere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    def nuova_partita(self):
        self.parola = random.choice(self.parole_tot).upper()
        self.parola_nascosta = "_" * len(self.parola)
        self.tentativi_falliti = 0
        self.lettere_rimaste = self.lettere[:]
        
        self.aggiorna_ui()
    
    def aggiorna_ui(self):
        self.label_parola.config(text=" ".join(self.parola_nascosta))
        self.label_tentativi.config(text=f"Tentativi falliti: {self.tentativi_falliti}")
        self.label_lettere_rimaste.config(text=f"Lettere rimaste: {', '.join(self.lettere_rimaste)}")
        self.entry_lettera.delete(0, tk.END)
    
    def verifica_lettera(self):
        scelta = self.entry_lettera.get().upper()
        
        if len(scelta) != 1 or scelta not in self.lettere_rimaste:
            messagebox.showwarning("Attenzione", f"La lettera '{scelta}' non è valida o è già stata usata.")
            return
        
        self.lettere_rimaste.remove(scelta)
        
        if scelta in self.parola:
            nuova_parola_nascosta = list(self.parola_nascosta)
            for i, char in enumerate(self.parola):
                if char == scelta:
                    nuova_parola_nascosta[i] = scelta
            self.parola_nascosta = "".join(nuova_parola_nascosta)
        else:
            self.tentativi_falliti += 1
        
        self.aggiorna_ui()
        
        if self.parola_nascosta == self.parola:
            messagebox.showinfo("Vittoria", f"Hai trovato la parola: {self.parola}")
            self.nuova_partita()
        elif self.tentativi_falliti >= self.max_tentativi:
            messagebox.showerror("Sconfitta", f"Hai perso! La parola era: {self.parola}")
            self.nuova_partita()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImpiccatoApp(root)
    root.mainloop()