import json
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#------------------------------------------------------------------------------------------#
# Funzioni per caricare e salvare i dati

# Carica i prodotti da file JSON
def carica_prodotti(file_prodotti):
    try:
        with open(file_prodotti, 'r') as f:
            dati = json.load(f)
            return dati.get('products', [])
    except:
        return []

# Carica il resto disponibile da file JSON
def carica_resto(file_resto):
    default = {"2.00": 0, "1.00": 0, "0.5": 0, "0.2": 0, "0.1": 0, "0.05": 0}
    try:
        with open(file_resto, 'r') as f:
            return json.load(f).get('monete', default)
    except:
        return default

# Salva il resto aggiornato su file JSON
def salva_resto(file_resto, resto):
    try:
        with open(file_resto, 'w') as f:
            json.dump({"monete": resto}, f, indent=4)
    except Exception as e:
        print("Errore nel salvataggio:", e)

# Salva i prodotti aggiornati su file JSON
def salva_prodotti(file_prodotti, prodotti):
    try:
        with open(file_prodotti, 'w') as f:
            json.dump({"products": prodotti}, f, indent=4)
    except Exception as e:
        print("Errore nel salvataggio:", e)

#------------------------------------------------------------------------------------------#
# Funzione principale che avvia l'interfaccia del distributore

def main():
    gui = tk.Tk()
    gui.title("Distributore Automatico")
    gui.state('zoomed')  # Finestra a schermo intero

    # Percorsi dei file JSON
    cartella_corrente = os.path.dirname(__file__)
    file_prodotti = os.path.join(cartella_corrente, 'Json', 'products.json')
    file_resto = os.path.join(cartella_corrente, 'Json', 'resto.json')
    
    # Caricamento iniziale dei dati
    prodotti = carica_prodotti(file_prodotti)
    resto = carica_resto(file_resto)

    soldi_inseriti = 0.0
    codice_inserito = ""
    messaggio = "Benvenuto! Inserisci il codice del prodotto."

    #------------------------------------------------------------------------------------------#
    # Funzioni di interfaccia e logica

    # Aggiorna le etichette dei prodotti nell'interfaccia
    def aggiorna_prodotti():
        for prodotto in prodotti:
            id_prodotto = prodotto['id']
            if id_prodotto in widgets_prodotti:
                testo = f"ID: {prodotto['id']}\n{prodotto['nome']}\n€{prodotto['prezzo']:.2f}\nDisponibili: {prodotto['quantita']}"
                widgets_prodotti[id_prodotto]['label'].config(text=testo)

    # Gestione Soldi
    def aggiungi_soldi(importo):
        nonlocal soldi_inseriti
        soldi_inseriti = round(soldi_inseriti + importo, 2)
        label_soldi.config(text=f"Soldi inseriti: €{soldi_inseriti:.2f}")
            
        if importo in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
            chiave = f"{importo:.2f}" if importo >= 0.1 else "0.05"
            resto[chiave] = resto.get(chiave, 0) + 1
            salva_resto(file_resto, resto)

    # Calcola e restituisce il resto all'utente
    def dai_il_resto():
        nonlocal soldi_inseriti, messaggio
        if soldi_inseriti == 0:
            messaggio = "Nessun resto da erogare."
            label_info.config(text=messaggio)
            return

        resto_da_dare = soldi_inseriti
        monete_usate = {}
        monete = ["2.00", "1.00", "0.5", "0.2", "0.1", "0.05"]

        # Calcola le monete da restituire partendo dalle più grandi
        for moneta in monete:
            valore = float(moneta)
            if resto_da_dare >= valore and resto.get(moneta, 0) > 0:
                numero_monete = min(int(resto_da_dare // valore), resto[moneta])
                if numero_monete > 0:
                    monete_usate[moneta] = numero_monete
                    resto_da_dare = round(resto_da_dare - (numero_monete * valore), 2)
                    resto[moneta] -= numero_monete

        # Verifica se il resto è stato erogato correttamente
        if resto_da_dare > 0:
            messaggio = "Resto insufficiente. Mi scuso per l'inconveniente."
        else:
            dettagli_resto = ", ".join([f"{num} moneta/e da {valore}€" for valore, num in monete_usate.items()])
            messaggio = f"Resto erogato: {dettagli_resto}"
            soldi_inseriti = 0.0
            label_soldi.config(text=f"Soldi inseriti: €{soldi_inseriti:.2f}")
            salva_resto(file_resto, resto)

        label_info.config(text=messaggio)

    # Gestisce l'inserimento del codice e l'acquisto del prodotto
    def gestisci_tasto(tasto):
        nonlocal codice_inserito, messaggio, soldi_inseriti
        
        if tasto == "←":
            codice_inserito = codice_inserito[:-1]
            entry_codice.delete(len(codice_inserito), tk.END)
        elif tasto == "✗":
            codice_inserito = ""
            entry_codice.delete(0, tk.END)
        elif tasto == "✓":
            try:
                codice = int(codice_inserito)
                for prodotto in prodotti:
                    if prodotto['id'] == codice:
                        if prodotto['quantita'] > 0:
                            if soldi_inseriti >= prodotto['prezzo']:
                                soldi_inseriti = round(soldi_inseriti - prodotto['prezzo'], 2)
                                label_soldi.config(text=f"Soldi inseriti: €{soldi_inseriti:.2f}")
                                prodotto['quantita'] -= 1
                                salva_prodotti(file_prodotti, prodotti)
                                aggiorna_prodotti()
                                messaggio = f"Prodotto erogato: {prodotto['nome']}\nResto: €{soldi_inseriti:.2f}"
                            else:
                                messaggio = "Soldi insufficienti!"
                        else:
                            messaggio = "Prodotto esaurito!"
                        break
                else:
                    messaggio = "Prodotto non trovato!"
            except ValueError:
                messaggio = "Inserire un codice numerico valido"

            codice_inserito = ""
            entry_codice.delete(0, tk.END)
            label_info.config(text=messaggio)
        else:
            if len(codice_inserito) < 3:
                codice_inserito += str(tasto)
                entry_codice.delete(0, tk.END)
                entry_codice.insert(0, codice_inserito)

    #------------------------------------------------------------------------------------------#
    # Costruzione interfaccia grafica (GUI)

    # Struttura principale della finestra
    frame_principale = ttk.Frame(gui)
    frame_principale.place(relx=0.5, rely=0.5, anchor="center")

    # Info e messaggi all'utente
    frame_info = ttk.LabelFrame(frame_principale, text="Info")
    frame_info.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    label_info = tk.Label(frame_info, text=messaggio, wraplength=400, font=12)
    label_info.grid(row=0, column=0, padx=10, pady=10)

    # Sezione prodotti
    frame_prodotti = ttk.Frame(frame_principale)
    frame_prodotti.grid(row=1, column=0, padx=10, pady=10)

    label_prodotti = ttk.LabelFrame(frame_prodotti, text="Prodotti Disponibili")
    label_prodotti.grid(row=0, column=0, padx=10, pady=10)

    # Sezione tastierino e denaro
    frame_pulsanti = ttk.Frame(frame_principale)
    frame_pulsanti.grid(row=1, column=1, padx=10, pady=10)

    frame_tastierino = ttk.LabelFrame(frame_pulsanti, text="Inserisci codice")
    frame_tastierino.grid(row=0, column=0, padx=10, pady=10)

    frame_soldi = ttk.LabelFrame(frame_pulsanti, text="Inserisci denaro")
    frame_soldi.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    frame_soldi_attuali = ttk.LabelFrame(frame_principale, text="Credito Attuale")
    frame_soldi_attuali.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    label_soldi = tk.Label(frame_soldi_attuali, text=f"Soldi inseriti: €{soldi_inseriti:.2f}", font=12)
    label_soldi.grid(row=0, column=0, padx=10, pady=10)

    entry_codice = tk.Entry(frame_tastierino, width=30, font=14)
    entry_codice.grid(row=0, column=0, columnspan=3, pady=10)

    # Tastierino per inserire il codice
    tasti = [
        ('A', 1, 0), ('B', 1, 1), ('←', 1, 2),
        (1, 2, 0), (2, 2, 1), (3, 2, 2),
        (4, 3, 0), (5, 3, 1), (6, 3, 2),
        (7, 4, 0), (8, 4, 1), (9, 4, 2),
        ('✓', 5, 0), (0, 5, 1), ('✗', 5, 2)
    ]

    # Creazione dei pulsanti tastierino
    for (testo, riga, colonna) in tasti:
        tk.Button(
            frame_tastierino, 
            text=str(testo), 
            width=8, 
            height=2,
            font=12,
            command=lambda t=testo: gestisci_tasto(t)
        ).grid(row=riga, column=colonna, padx=5, pady=5)

    # Visualizzazione dei prodotti con immagini (se disponibili)
    widgets_prodotti = {}
    for i, prodotto in enumerate(prodotti):
        frame_prodotto = ttk.Frame(label_prodotti)
        frame_prodotto.grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="w")
        
        img_label = None
        nome_immagine = f"{prodotto['nome'].split()[0].lower()}.jpg"
        percorso_immagine = os.path.join(cartella_corrente, nome_immagine)

        # Caricamento immagine del prodotto
        if os.path.exists(percorso_immagine):
            try:
                img = Image.open(percorso_immagine).resize((100, 100), Image.Resampling.LANCZOS)
                foto = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame_prodotto, image=foto)
                img_label.image = foto
                img_label.grid(row=0, column=0, padx=5)
            except Exception as e:
                print(f"Errore caricamento immagine {nome_immagine}: {e}")

        testo_prodotto = f"ID: {prodotto['id']}\n{prodotto['nome']}\n€{prodotto['prezzo']:.2f}\nDisponibili: {prodotto['quantita']}"
        label_testo = tk.Label(frame_prodotto, text=testo_prodotto, justify=tk.LEFT, font=10)
        label_testo.grid(row=0, column=1 if img_label else 0, padx=5)

        widgets_prodotti[prodotto['id']] = {
            'label': label_testo,
            'image': img_label
        }

    # Pulsanti per inserire denaro
    pulsanti_soldi = [
        (0.05, "0.05"), (0.10, "0.10"), (0.20, "0.20"), 
        (0.50, "0.50"), (1.00, "1.00"), (2.00, "2.00"),
        (10.00, "10.00€"), (20.00, "20.00€")
    ]

    # Creazione dei pulsanti monete e chiavette
    for i, (valore, etichetta) in enumerate(pulsanti_soldi):
        tk.Button(
            frame_soldi, 
            text=etichetta, 
            width=12, 
            height=2,
            font=10,
            command=lambda v=valore: aggiungi_soldi(v)
        ).grid(row=i // 2, column=i % 2, padx=5, pady=5)

    # Pulsante per richiedere il resto
    tk.Button(
        frame_soldi, 
        text="Richiedi resto", 
        width=15, 
        height=2,
        font=10,
        command=dai_il_resto
    ).grid(row=len(pulsanti_soldi) // 2 + 1, column=0, columnspan=2, pady=10)

    gui.mainloop()

if __name__ == "__main__":
    main()
