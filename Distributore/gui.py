import json
import os
import tkinter as tk
from tkinter import ttk

codeInsert = ""

def main():
    gui = tk.Tk()
    gui.title("Distributore")
    
    # Imposta una dimensione fissa per la finestra
    gui.geometry("1000x500")
    gui.resizable(False, False)

    # Centra la finestra
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    position_top = int((screen_height / 2) - 250)
    position_right = int((screen_width / 2) - 500)
    gui.geometry(f"1000x500+{position_right}+{position_top}")

    # Percorso dei file JSON
    products_file_path = os.path.join(os.path.dirname(__file__), 'Json', 'products.json')
    resti_file_path = os.path.join(os.path.dirname(__file__), 'Json', 'resto.json')
    
    # Carica i prodotti
    try:
        with open(products_file_path, 'r') as fileProdotti:
            data = json.load(fileProdotti)
            prodotti = data.get('products', [])
    except (FileNotFoundError, json.JSONDecodeError):
        prodotti = []

    # Carica il resto
    try:
        with open(resti_file_path, 'r') as fileResti:
            resti = json.load(fileResti).get('monete', {})
    except (FileNotFoundError, json.JSONDecodeError):
        resti = {
            "2.00": 0,
            "1.00": 0,
            "0.5": 0,
            "0.2": 0,
            "0.1": 0,
            "0.05": 0
        }

    # Variabili per l'interfaccia
    money_inserted = tk.DoubleVar(value=0.0)
    display_info = tk.StringVar(value="Benvenuto! Inserisci il codice del prodotto.")
    display_money = tk.StringVar(value=f"Soldi inseriti: €{money_inserted.get():.2f}")

    def save_resti():
        try:
            with open(resti_file_path, 'w') as fileResti:
                json.dump({"monete": resti}, fileResti, indent=4)
        except Exception:
            pass

    # Setup dell'interfaccia
    main_frame = ttk.Frame(gui)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Frames principali
    lableFrameInfo = ttk.LabelFrame(main_frame, text="Info")
    lableFrameInfo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    frameProduct = ttk.Frame(main_frame)
    frameProduct.grid(row=1, column=0, padx=10, pady=10)

    lableFrameProducts = ttk.LabelFrame(frameProduct, text="Products")
    lableFrameProducts.grid(row=0, column=0, padx=10, pady=10)

    frameButtons = ttk.Frame(main_frame)
    frameButtons.grid(row=1, column=1, padx=10, pady=10)

    lableFrameButtons = ttk.LabelFrame(frameButtons, text="Buttons")
    lableFrameButtons.grid(row=0, column=0, padx=10, pady=10)

    lableFrameMoney = ttk.LabelFrame(frameButtons, text="Money")
    lableFrameMoney.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    lableFrameCurrentMoney = ttk.LabelFrame(main_frame, text="Current Money")
    lableFrameCurrentMoney.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(lableFrameCurrentMoney, textvariable=display_money).grid(row=0, column=0, padx=10, pady=10)

    def button_function(buttonArgument):
        global codeInsert
        if buttonArgument == "←":
            codeInsert = codeInsert[:-1]
            displayTastierino.delete(len(codeInsert), tk.END)
        elif buttonArgument == "✓":
            try:
                code = int(codeInsert)
                for product in prodotti:
                    if product.get('id') == code:
                        if product.get('quantita', 0) > 0:
                            if money_inserted.get() >= product.get('prezzo', 0):
                                money_inserted.set(round(money_inserted.get() - product.get('prezzo', 0), 2))
                                display_money.set(f"Soldi inseriti: €{money_inserted.get():.2f}")  # Update money display
                                product['quantita'] -= 1
                                display_info.set(f"Prodotto erogato: {product.get('nome')}\nResto: €{money_inserted.get():.2f}")
                            else:
                                display_info.set("Soldi insufficienti!")
                        else:
                            display_info.set("Prodotto esaurito!")
                        break
                else:
                    display_info.set("Prodotto non trovato!")
            except ValueError:
                display_info.set("Inserire un codice numerico valido")
            codeInsert = ""
            displayTastierino.delete(0, tk.END)
        elif buttonArgument == "✗":
            codeInsert = ""
            displayTastierino.delete(0, tk.END)
        else:
            if len(codeInsert) < 3:
                codeInsert += str(buttonArgument)
                displayTastierino.delete(0, tk.END)
                displayTastierino.insert(0, codeInsert)


    def add_money(amount):
        money_inserted.set(round(money_inserted.get() + amount, 2))
        display_money.set(f"Soldi inseriti: €{money_inserted.get():.2f}")
        
        # Aggiunge la moneta al JSON solo per le monete fisiche
        if amount in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
            # Trova la chiave corretta nel formato del JSON
            if amount == 0.05: key = "0.05"
            elif amount == 0.1: key = "0.1"
            elif amount == 0.2: key = "0.2"
            elif amount == 0.5: key = "0.5"
            elif amount == 1.0: key = "1.00"
            elif amount == 2.0: key = "2.00"
            
            if key in resti:
                resti[key] += 1
            else:
                resti[key] = 1
            save_resti()

    def give_change():
        change = round(money_inserted.get(), 2)
        if change == 0:
            display_info.set("Nessun resto da erogare.")
            return

        change_given = {}
        remaining = change
        
        # Ordina le monete dal valore più alto al più basso secondo il formato del JSON
        coin_order = ["2.00", "1.00", "0.5", "0.2", "0.1", "0.05"]
        for coin_str in coin_order:
            coin_value = float(coin_str)
            if remaining >= coin_value and resti.get(coin_str, 0) > 0:
                num_coins = min(int(remaining // coin_value), resti[coin_str])
                if num_coins > 0:
                    change_given[coin_str] = num_coins
                    remaining = round(remaining - (num_coins * coin_value), 2)
                    resti[coin_str] -= num_coins

        if remaining > 0:
            display_info.set("Resto insufficiente. Mi scuso per l'inconveniente.")
        else:
            display_info.set(f"Resto erogato: {', '.join([f'{v}x{c}€' for c, v in change_given.items()])}")
            money_inserted.set(0.0)
            display_money.set(f"Soldi inseriti: €{money_inserted.get():.2f}")
            save_resti()

    # Tastierino numerico
    displayTastierino = tk.Entry(lableFrameButtons, width=30)
    displayTastierino.grid(row=0, column=0, columnspan=3, pady=10)

    buttons = [
        ('A', 1, 0), ('B', 1, 1), ('←', 1, 2),
        (1, 2, 0), (2, 2, 1), (3, 2, 2),
        (4, 3, 0), (5, 3, 1), (6, 3, 2),
        (7, 4, 0), (8, 4, 1), (9, 4, 2),
        ('✓', 5, 0), (0, 5, 1), ('✗', 5, 2)
    ]

    for (text, row, col) in buttons:
        tk.Button(lableFrameButtons, text=str(text), width=10, height=2, 
                 command=lambda t=text: button_function(t)).grid(row=row, column=col)

    # Mostra prodotti
    for i, product in enumerate(prodotti):
        product_info = f"ID: {product.get('id', 'N/A')} - {product.get('nome', 'N/A')}\nPrezzo: €{product.get('prezzo', 'N/A')} - Quantità: {product.get('quantita', 'N/A')}"
        tk.Label(lableFrameProducts, text=product_info, justify=tk.LEFT).grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="w")

    # Pulsanti denaro modificati
    money_buttons = [
        (0.05, "5 cent"), (0.10, "10 cent"), (0.20, "20 cent"), 
        (0.50, "50 cent"), (1.00, "1 euro"), (2.00, "2 euro"),
        (10.00, "Chiavetta 10€"), (20.00, "Chiavetta 20€")
    ]

    for i, (value, label) in enumerate(money_buttons):
        tk.Button(lableFrameMoney, text=label, width=15, height=2, 
                  command=lambda v=value: add_money(v)).grid(row=i // 2, column=i % 2, padx=5, pady=5)

    # Pulsante resto
    tk.Button(lableFrameMoney, text="Richiedi resto", width=15, height=2, 
              command=give_change).grid(row=len(money_buttons) // 2 + 1, column=0, columnspan=2, pady=10)

    # Schermo informazioni
    tk.Label(lableFrameInfo, textvariable=display_info, wraplength=400).grid(row=0, column=0, padx=10, pady=10)
    
    gui.mainloop()

if __name__ == "__main__":
    main()