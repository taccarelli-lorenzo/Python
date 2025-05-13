import random 
import tkinter as tk
from tkinter import ttk

class Start:
    def __init__(self, root):
        self.root = root 
        self.root.title("Sasso Carta Forbici")
        self.root.state("zoomed")
        
        self.scelte = ["Sasso", "Carta", "Forbice"]
        self.vittorie_utente = 0
        self.vittorie_pc = 0
        self.vittorie_max = 3
        
        self.frame_iniziale = ttk.Frame(self.root)
        self.frame_iniziale.pack(pady=150)
        
        
        # Pulsanti
         
        self.frame_pulsanti = ttk.Frame(self.root)
        self.frame_pulsanti.pack(pady=20)
        
        self.pulsante_sasso = ttk.Button(self.frame_pulsanti, text="Sasso", command=lambda: self.lotta("Sasso"))
        self.pulsante_sasso.pack(side=tk.LEFT, padx=10)
        
        self.pulsante_carta = ttk.Button(self.frame_pulsanti, text="Carta", command=lambda: self.lotta("Carta"))
        self.pulsante_carta.pack(side=tk.LEFT, padx=10)
        
        self.pulsante_forbice = ttk.Button(self.frame_pulsanti, text="Forbice", command=lambda: self.lotta("Forbice"))
        self.pulsante_forbice.pack(side=tk.LEFT, padx=10)
        
        
        # Risultati 
        
        self.frame_risultati = ttk.Frame(self.root)
        self.frame_risultati.pack(pady=20)
        
        self.label_risultato = tk.Label(self.frame_risultati, text="Fai la tua scelta!")
        self.label_risultato.pack(pady=10)
        
        self.label_punteggio = tk.Label(self.frame_risultati, text=f"Punteggio: Utente {self.vittorie_utente} - Computer {self.vittorie_pc}")
        self.label_punteggio.pack(pady=10)
        
        self.pulsante_nuova_partita = ttk.Button(self.root, text="Nuova Partita", command=self.nuova_partita)
        self.pulsante_nuova_partita.pack(pady=10)
    
    
    # Confronto 
    
    def lotta(self, scelta):
        risultato = ""
        
        self.scelta_utente = scelta
        self.scelta_pc = random.choice(self.scelte)
        
        if self.scelta_pc == self.scelta_utente:
            risultato = "Pareggio!"
            
        elif self.scelta_pc == "Sasso":
            if self.scelta_utente == "Forbice":
                risultato = "Vittoria Computer!"
                self.vittorie_pc += 1
            else:
                risultato = "Vittoria Utente!"
                self.vittorie_utente += 1
                        
        elif self.scelta_pc == "Forbice":
            if self.scelta_utente == "Carta":
                risultato = "Vittoria Computer!"
                self.vittorie_pc += 1
            else:
                risultato = "Vittoria Utente!"
                self.vittorie_utente += 1
                
        else:
            if self.scelta_utente == "Sasso":
                risultato = "Vittoria Computer!"
                self.vittorie_pc += 1
            else:
                risultato = "Vittoria Utente!"
                self.vittorie_utente += 1
    
        self.aggiorna_ui(risultato)          
        
    
    # Mostra il risultato   
    
    def aggiorna_ui(self, risultato):
        self.label_risultato.config(text=f"Utente: {self.scelta_utente} - Computer: {self.scelta_pc}\n{risultato}")
        self.label_punteggio.config(text=f"Punteggio: Utente {self.vittorie_utente} - Computer {self.vittorie_pc}")
        
        if self.vittorie_utente == self.vittorie_max:
            self.label_risultato.config(text="L'Utente Ha Vinto La Partita!")
            self.blocca_pulsanti()
            
        elif self.vittorie_pc == self.vittorie_max:
            self.label_risultato.config(text="Il Computer Ha Vinto La Partita!")
            self.blocca_pulsanti()
            
    
    # Blocca la possibilità di premere i pulsanti nel caso in cui uno dei due vinca
            
    def blocca_pulsanti(self):
        self.pulsante_sasso.config(state="disabled")
        self.pulsante_carta.config(state="disabled")
        self.pulsante_forbice.config(state="disabled")
        
    
    # Ripristina tutti i valori a quelli iniziali         
        
    def nuova_partita(self):
        self.vittorie_utente = 0
        self.vittorie_pc = 0
        self.label_risultato.config(text="Fai la tua scelta!")
        self.label_punteggio.config(text=f"Punteggio: Utente {self.vittorie_utente} - Computer {self.vittorie_pc}")
        self.pulsante_sasso.config(state="enabled")
        self.pulsante_carta.config(state="enabled")
        self.pulsante_forbice.config(state="enabled")  
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Start(root)
    root.mainloop()