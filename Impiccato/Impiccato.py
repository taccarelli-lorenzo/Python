import os
import json
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ImpiccatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Impiccato")
        self.root.geometry("900x800")
        self.root.resizable(False, False)        
        self.max_tentativi = 7
        
        self.image_folder = os.path.join(os.path.dirname(__file__), 'impiccato-image')
        self.images = []
        self.image_size = (250, 350)
        self.load_images()
        
        self.parola = ""
        self.parola_nascosta = ""
        self.lettere = []
        self.tentativi_falliti = 0
        
        self.setup_ui()
        self.carica_dati()
        self.nuova_partita()
        
    #------------------------------------------------------------------------------------------#
    # Caricamento immagini #
    
    def load_images(self):
        try:
            for i in range(self.max_tentativi):
                img_path = os.path.join(self.image_folder, f'imp{i}.gif')
                img = Image.open(img_path)
                img = img.resize(self.image_size, Image.LANCZOS)
                self.images.append(ImageTk.PhotoImage(img))
        except Exception as e:
            self.message_box("Errore", f"Impossibile caricare le immagini: {str(e)}")
            self.root.destroy()
    
    #------------------------------------------------------------------------------------------#
    # Aggiorna l'immagine in base ai tentativi falliti #
    
    def update_image(self):
        if self.tentativi_falliti < len(self.images):
            self.current_image = self.images[self.tentativi_falliti]
            self.image_label.config(image=self.current_image)
    
    #------------------------------------------------------------------------------------------#
    # Carica le parole e le lettere dai file JSON #
    
    def carica_dati(self):
        try:
            # Carica le parole #
            file_path = os.path.join(os.path.dirname(__file__), 'parole.json')
            with open(file_path, 'r') as file:
                self.parole_totali = json.load(file)
            
            # Carica le lettere #
            file_path = os.path.join(os.path.dirname(__file__), 'lettere.json')
            with open(file_path, 'r') as file:
                self.lettere_totali = json.load(file)
                
        except Exception as e:
            self.message_box("Errore", f"Errore nel caricamento dei dati: {str(e)}")
            self.root.destroy()
    
    #------------------------------------------------------------------------------------------#
    # Inizia una nuova partita #
    
    def nuova_partita(self):
        self.parola = random.choice(self.parole_totali).upper()
        self.parola_nascosta = "_ " * len(self.parola)
        self.lettere = self.lettere_totali.copy()
        self.tentativi_falliti = 0
        self.entry_lettera.config(state='normal')
        self.update_image()
        self.aggiorna_ui()
    
    #------------------------------------------------------------------------------------------#
    # Configura l'interfaccia grafica #
    
    def setup_ui(self):
        self.message_frame = tk.Frame(self.root)
        self.message_frame.pack(pady=5)
        self.message_label = tk.Label(self.message_frame, text="", font=("Helvetica", 12))
        self.message_label.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)
        
        self.label_parola = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.label_parola.pack(pady=20)
        
        self.label_tentativi = tk.Label(self.root, text="Tentativi falliti: 0/7", font=("Helvetica", 14))
        self.label_tentativi.pack(pady=10)
        
        self.entry_lettera = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry_lettera.pack(pady=10)
        self.entry_lettera.bind('<Return>', lambda event: self.verifica_lettera())
        
        tk.Button(self.root, text="Invia", command=self.verifica_lettera, font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.root, text="Nuova Partita", command=self.nuova_partita, font=("Helvetica", 14)).pack(pady=10)
        
        self.label_lettere_rimaste = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.label_lettere_rimaste.pack(pady=10)
    
    #------------------------------------------------------------------------------------------#
    # Mostra messaggi colorati #
    
    def mostra_messaggio(self, messaggio, tipo="info"):
        colori = {
            "info": "black",
            "errore": "red",
            "successo": "green",
            "avviso": "orange"
        }
        self.message_label.config(text=messaggio, fg=colori.get(tipo, "black"))
        self.root.after(3000, lambda: self.message_label.config(text=""))
    
    #------------------------------------------------------------------------------------------#
    # Verifica la lettera inserita dall'utente #
    
    
    def verifica_lettera(self):
        scelta = self.entry_lettera.get().upper()
        self.entry_lettera.delete(0, tk.END)
        
        if len(scelta) != 1 or not scelta.isalpha():
            self.mostra_messaggio("Inserisci una singola lettera valida", "avviso")
            return
        
        if scelta in self.lettere:  
            self.lettere.remove(scelta)
            
            if scelta in self.parola:
                nuova_parola = list(self.parola_nascosta.replace(" ", ""))
                for i, char in enumerate(self.parola):
                    if char == scelta:
                        nuova_parola[i] = scelta
                self.parola_nascosta = " ".join(nuova_parola)
                
                if "_" not in self.parola_nascosta:
                    self.mostra_messaggio(f"Complimenti! Hai indovinato la parola: {self.parola}", "successo")
                    self.entry_lettera.config(state='disabled')
            else:
                self.tentativi_falliti += 1
                self.update_image()
                if self.tentativi_falliti >= self.max_tentativi:
                    img_path = os.path.join(self.image_folder, 'hangman1.gif')
                    try:
                        img = Image.open(img_path)
                        img = img.resize(self.image_size, Image.LANCZOS)
                        self.current_image = ImageTk.PhotoImage(img)
                        self.image_label.config(image=self.current_image)
                    except Exception as e:
                        self.mostra_messaggio(f"Errore nel caricamento immagine: {str(e)}", "errore")
                    self.mostra_messaggio(f"Game Over! La parola era: {self.parola}", "errore")
                    self.entry_lettera.config(state='disabled')
        else:
            self.mostra_messaggio(f"La lettera '{scelta}' non è valida o è già stata usata", "avviso")
        
        self.aggiorna_ui()

    #------------------------------------------------------------------------------------------#
    # Aggiorna l'interfaccia utente #
    
    def aggiorna_ui(self):
        self.label_parola.config(text=self.parola_nascosta)
        self.label_tentativi.config(text=f"Tentativi falliti: {self.tentativi_falliti}/{self.max_tentativi}")
        self.label_lettere_rimaste.config(text=f"Lettere rimaste: {', '.join(sorted(self.lettere))}")