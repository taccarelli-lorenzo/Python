import tkinter as tk
from tkinter import ttk

codeInsert = ""

def main():
    gui = tk.Tk()
    gui.title("Distributore")

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
            print(codeInsert)
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
        tk.Button(lableFrameButtons, text=str(text), width=10, height=2, command=lambda t=text: button_function(t)).grid(row=row, column=col)

    products = ["Prodotto 1", "Prodotto 2", "Prodotto 3", "Prodotto 4"]
    for i, product in enumerate(products):
        tk.Label(lableFrameProducts, text=product).grid(row=i, column=3, padx=10, pady=10)

    gui.mainloop()

if __name__ == "__main__":
    main()