import json
import os
import tkinter as tk
from tkinter import ttk

class Statistiche:
    def __init__(self, gui):
        self.gui = gui
        self.gui.title("Statistiche")
        self.gui.state('zoomed')
        
        self.carica_dati()
        self.menu()
        
#------------------------------------------------------------------------------------------#
    # Carica file JSON #

    def carica_dati(self):
        try:
            # Carica gli studenti #
            file_path = os.path.join(os.path.dirname(__file__), 'studenti.json')
            with open(file_path, 'r') as file:
                self.parole_totali = json.load(file)
            
        except FileNotFoundError:
            self.gui.destroy()

#------------------------------------------------------------------------------------------#
    # Menu a tendina #
    
    def menu(self):
        tendina = ttk.Combobox(self.gui, width=18)
        tendina['values']=["elemento1","elemento2", "elemento3"]
        tendina.grid(row=0, column=0, sticky=tk.W)
        
    

def main():
    gui = tk.Tk()
    app = Statistiche(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()