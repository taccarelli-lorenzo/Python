import json
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#------------------------------------------------------------------------------------------#
# Funzioni per caricare e salvare i dati in JSON #

def load_products(products_file):
    try:
        with open(products_file, 'r') as fileProdotti:
            data = json.load(fileProdotti)
            return data.get('products', [])
    except Exception as e:
        return []

def load_resti(resti_file):
    try:
        with open(resti_file, 'r') as fileResti:
            return json.load(fileResti).get('monete', {
                "2.00": 0, "1.00": 0, "0.5": 0, 
                "0.2": 0, "0.1": 0, "0.05": 0
            })
    except Exception as e:
        return {
            "2.00": 0, "1.00": 0, "0.5": 0,
            "0.2": 0, "0.1": 0, "0.05": 0
        }

def save_resti(resti_file, resti):
    try:
        with open(resti_file, 'w') as fileResti:
            json.dump({"monete": {
                "2.00": resti["2.00"],
                "1.00": resti["1.00"],
                "0.5": resti["0.5"],
                "0.2": resti["0.2"],
                "0.1": resti["0.1"],
                "0.05": resti["0.05"]
            }}, fileResti, indent=4)
    except Exception as e:
        print(f"Errore nel salvataggio del resto: {e}")

def save_products(products_file, prodotti):
    try:
        with open(products_file, 'w') as fileProdotti:
            json.dump({"products": [ 
                {
                    "id": p["id"],
                    "nome": p["nome"],
                    "prezzo": p["prezzo"],
                    "quantita": p["quantita"]
                } for p in prodotti
            ]}, fileProdotti, indent=4)
    except Exception as e:
        print(f"Errore nel salvataggio dei prodotti: {e}")
#------------------------------------------------------------------------------------------#
# Funzione principale per l'interfaccia grafica #

def main():
    gui = tk.Tk()
    gui.title("Distributore")
    gui.state('zoomed')

    products_file = os.path.join(os.path.dirname(__file__), 'Json', 'products.json')
    resti_file = os.path.join(os.path.dirname(__file__), 'Json', 'resto.json')
    
    prodotti = load_products(products_file)
    resti = load_resti(resti_file)

    money_inserted = tk.DoubleVar(value=0.0)
    display_info = tk.StringVar(value="Benvenuto! Inserisci il codice del prodotto.")
    display_money = tk.StringVar(value=f"Soldi inseriti: €{money_inserted.get():.2f}") 

    products_list = {}
    
    #------------------------------------------------------------------------------------------#
    # Funzioni per aggiornare la visualizzazione dei prodotti e gestire il resto #

    def update_product_display():
        for product in prodotti:
            widget_info = products_list.get(product['id'])
            if widget_info:
               
                product_info = f"ID: {product['id']}\n{product['nome']}\n€{product['prezzo']:.2f}\nDisponibili: {product['quantita']}"
                widget_info['label'].config(text=product_info)

    def add_money(amount):
        money_inserted.set(round(money_inserted.get() + amount, 2))
        display_money.set(f"Soldi inseriti: €{money_inserted.get():.2f}")
        
        if amount in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
            key = f"{amount:.2f}" if amount >= 0.1 else "0.05"
            resti[key] = resti.get(key, 0) + 1
            save_resti(resti_file, resti)

    def give_change():
        change = round(money_inserted.get(), 2)
        if change == 0:
            display_info.set("Nessun resto da erogare.")
            return

        change_given = {}
        remaining = change
        
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
            save_resti(resti_file, resti)

    def button_function(buttonArgument):
        nonlocal codeInsert
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
                                display_money.set(f"Soldi inseriti: €{money_inserted.get():.2f}")
                                product['quantita'] -= 1
                                save_products(products_file, prodotti)
                                update_product_display()  # Aggiorna la visualizzazione
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

    # Interfaccia grafica
    main_frame = ttk.Frame(gui)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Frames principali
    lableFrameInfo = ttk.LabelFrame(main_frame, text="Info")
    lableFrameInfo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    frameProduct = ttk.Frame(main_frame)
    frameProduct.grid(row=1, column=0, padx=10, pady=10)

    lableFrameProducts = ttk.LabelFrame(frameProduct, text="Prodotti Disponibili")
    lableFrameProducts.grid(row=0, column=0, padx=10, pady=10)

    frameButtons = ttk.Frame(main_frame)
    frameButtons.grid(row=1, column=1, padx=10, pady=10)

    lableFrameButtons = ttk.LabelFrame(frameButtons, text="Inserisci codice")
    lableFrameButtons.grid(row=0, column=0, padx=10, pady=10)

    lableFrameMoney = ttk.LabelFrame(frameButtons, text="Inserisci denaro")
    lableFrameMoney.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    lableFrameCurrentMoney = ttk.LabelFrame(main_frame, text="Credito Attuale")
    lableFrameCurrentMoney.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(lableFrameCurrentMoney, textvariable=display_money, font=12).grid(row=0, column=0, padx=10, pady=10)

    # Tastierino numerico
    displayTastierino = tk.Entry(lableFrameButtons, width=30, font=14)
    displayTastierino.grid(row=0, column=0, columnspan=3, pady=10)

    buttons = [
        ('A', 1, 0), ('B', 1, 1), ('←', 1, 2),
        (1, 2, 0), (2, 2, 1), (3, 2, 2),
        (4, 3, 0), (5, 3, 1), (6, 3, 2),
        (7, 4, 0), (8, 4, 1), (9, 4, 2),
        ('✓', 5, 0), (0, 5, 1), ('✗', 5, 2)
    ]

    for (text, row, col) in buttons:
        btn = tk.Button(
            lableFrameButtons, 
            text=str(text), 
            width=8, 
            height=2,
            font=12,
            command=lambda t=text: button_function(t)
        )
        btn.grid(row=row, column=col, padx=5, pady=5)

    # Mostra prodotti
    for i, product in enumerate(prodotti):
        product_frame = ttk.Frame(lableFrameProducts)
        product_frame.grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="w")
        
        try:
            product_name = product.get('nome', '').split()[0].lower()
            image_path = os.path.join(os.path.dirname(__file__), f"{product_name}.jpg")
            img = Image.open(image_path)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(product_frame, image=photo)
            img_label.image = photo
            img_label.grid(row=0, column=0, padx=5)
            
            product_info = f"ID: {product['id']}\n{product['nome']}\n€{product['prezzo']:.2f}\nDisponibili: {product['quantita']}"
            info_label = tk.Label(product_frame, text=product_info, justify=tk.LEFT, font=10)
            info_label.grid(row=0, column=1, padx=5)
            
            # Salva i widget per aggiornarli successivamente
            products_list[product['id']] = {
                'label': info_label,
                'image': img_label
            }
        except Exception:
            product_info = f"ID: {product['id']}\n{product['nome']}\n€{product['prezzo']:.2f}\nDisponibili: {product['quantita']}"
            info_label = tk.Label(product_frame, text=product_info, justify=tk.LEFT, font=10)
            info_label.grid(row=0, column=0, padx=5)
            
            products_list[product['id']] = {
                'label': info_label,
                'image': None
            }

    # Pulsanti denaro
    money_buttons = [
        (0.05, "5 cent"), (0.10, "10 cent"), (0.20, "20 cent"), 
        (0.50, "50 cent"), (1.00, "1 euro"), (2.00, "2 euro"),
        (10.00, "Chiavetta 10€"), (20.00, "Chiavetta 20€")
    ]

    for i, (value, label) in enumerate(money_buttons):
        btn = tk.Button(
            lableFrameMoney, 
            text=label, 
            width=12, 
            height=2,
            font=10,
            command=lambda v=value: add_money(v)
        )
        btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    # Pulsante resto
    tk.Button(
        lableFrameMoney, 
        text="Richiedi resto", 
        width=15, 
        height=2,
        font=10,
        command=give_change
    ).grid(row=len(money_buttons) // 2 + 1, column=0, columnspan=2, pady=10)

    # Schermo informazioni
    tk.Label(
        lableFrameInfo, 
        textvariable=display_info, 
        wraplength=400,
        font=12
    ).grid(row=0, column=0, padx=10, pady=10)
    
    codeInsert = ""  # Inizializza la variabile per l'inserimento del codice
    gui.mainloop()

if __name__ == "__main__":
    main()