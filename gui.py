import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.title("Pack Example")

codeInsert = ""

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
    if(buttonArgument != "Confirm" and buttonArgument != "Delete"):
        codeInsert += str(buttonArgument)
    else:
        if(buttonArgument == "Confirm"):
            print("Confirm")
            print(codeInsert)
            codeInsert = ""
        else:
            print("Delete")
            codeInsert = ""

button0 = tk.Button(lableFrameButtons, text="0", width=10, height=2, command=lambda: button_function(0))
button1 = tk.Button(lableFrameButtons, text="1", width=10, height=2, command=lambda: button_function(1))
button2 = tk.Button(lableFrameButtons, text="2", width=10, height=2, command=lambda: button_function(2))
button3 = tk.Button(lableFrameButtons, text="3", width=10, height=2, command=lambda: button_function(3))
button4 = tk.Button(lableFrameButtons, text="4", width=10, height=2, command=lambda: button_function(4))
button5 = tk.Button(lableFrameButtons, text="5", width=10, height=2, command=lambda: button_function(5))
button6 = tk.Button(lableFrameButtons, text="6", width=10, height=2, command=lambda: button_function(6))
button7 = tk.Button(lableFrameButtons, text="7", width=10, height=2, command=lambda: button_function(7))
button8 = tk.Button(lableFrameButtons, text="8", width=10, height=2, command=lambda: button_function(8))
button9 = tk.Button(lableFrameButtons, text="9", width=10, height=2, command=lambda: button_function(9))

buttonA = tk.Button(lableFrameButtons, text="A", width=10, height=2, command=lambda: button_function('A'))
buttonB = tk.Button(lableFrameButtons, text="B", width=10, height=2, command=lambda: button_function('B'))
buttonCancel = tk.Button(lableFrameButtons, text="←", width=10, height=2, command=lambda: button_function('C'))

buttonConfirm = tk.Button(lableFrameButtons, text="✓", width=10, height=2, command=lambda: button_function('Confirm'))
buttonDelete = tk.Button(lableFrameButtons, text="✗", width=10, height=2, command=lambda: button_function('Delete'))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonA.grid(row=3, column=0)
buttonB.grid(row=3, column=1)
buttonCancel.grid(row=3, column=2)
buttonConfirm.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonDelete.grid(row=4, column=2)

# Aggiunta dei prodotti alla stessa scheda
product_label1 = tk.Label(lableFrameProducts, text="Prodotto 1")
product_label2 = tk.Label(lableFrameProducts, text="Prodotto 2")
product_label3 = tk.Label(lableFrameProducts, text="Prodotto 3")
product_label4 = tk.Label(lableFrameProducts, text="Prodotto 4")

product_label1.grid(row=0, column=3, padx=10, pady=10)
product_label2.grid(row=1, column=3, padx=10, pady=10)
product_label3.grid(row=2, column=3, padx=10, pady=10)
product_label4.grid(row=3, column=3, padx=10, pady=10)

gui.mainloop()