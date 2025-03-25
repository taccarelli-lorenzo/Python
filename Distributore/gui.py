import json
import os
import tkinter as tk
from tkinter import ttk

codeInsert = ""

def main():
    gui = tk.Tk()
    gui.title("Distributore")
    
    # Percorso del file JSON
    file_path = os.path.join(os.path.dirname(__file__), 'Json', 'products.json')
    
    # Carica i prodotti con un fallback se il file non esiste
    try:
        with open(file_path, 'r') as fileProdotti:
            data = json.load(fileProdotti)
            prodotti = data.get('products', [])
            print("File letto correttamente:", prodotti)
    except FileNotFoundError:
        print("Errore: File 'products.json' non trovato nella directory:", os.path.abspath(file_path))
        prodotti = []  # Lista vuota come fallback
    except json.JSONDecodeError:
        print("Errore: Il file non contiene JSON valido")
        prodotti = []  # Lista vuota come fallback
    except Exception as e:
        print(f"Errore sconosciuto: {type(e).__name__}: {e}")
        prodotti = []  # Lista vuota come fallback

    # Setup dell'interfaccia grafica
    frameProduct = ttk.Frame(gui)
    frameProduct.grid(row=0, column=0, padx=10, pady=10)

    lableFrameProducts = ttk.LabelFrame(frameProduct, text="Products")
    lableFrameProducts.grid(row=0, column=0, padx=10, pady=10)

    frameButtons = ttk.Frame(gui)
    frameButtons.grid(row=0, column=1, padx=10, pady=10)

    lableFrameButtons = ttk.LabelFrame(frameButtons, text="Buttons")
    lableFrameButtons.grid(row=0, column=0, padx=10, pady=10)

    def button_function(buttonArgument):
        global codeInsert
        if buttonArgument == "←":
            codeInsert = codeInsert[:-1]
            displayTastierino.delete(len(codeInsert), tk.END)
        elif buttonArgument == "✓":
            print("Confirm")
            print("Codice inserito:", codeInsert)
            # Verifica se il codice esiste nei prodotti
            try:
                code = int(codeInsert)
                for product in prodotti:
                    if product.get('id') == code:
                        print(f"Prodotto trovato: {product.get('nome')} - €{product.get('prezzo')} - Q.tà: {product.get('quantita')}")
                        break
                else:
                    print("Prodotto non trovato!")
            except ValueError:
                print("Inserire un codice numerico valido")
            codeInsert = ""
            displayTastierino.delete(0, tk.END)
        elif buttonArgument == "✗":
            print("Delete")
            codeInsert = ""
            displayTastierino.delete(0, tk.END)
        else:
            if len(codeInsert) < 3:
                codeInsert += str(buttonArgument)
                displayTastierino.delete(0, tk.END)
                displayTastierino.insert(0, codeInsert)

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
        if text == '✓':
            tk.Button()

    # Mostra i prodotti
    for i, product in enumerate(prodotti):
        product_id = product.get('id', 'N/A')
        product_nome = product.get('nome', 'N/A')
        product_prezzo = product.get('prezzo', 'N/A')
        product_quantita = product.get('quantita', 'N/A')
        
        # Mostra le informazioni del prodotto
        product_info = f"ID: {product_id} - {product_nome}\nPrezzo: €{product_prezzo} - Quantità: {product_quantita}"
        tk.Label(lableFrameProducts, text=product_info, justify=tk.LEFT).grid(row=i, column=0, padx=10, pady=5, sticky="w")

    gui.mainloop()

if __name__ == "__main__":
    main()