import os
import json
import tkinter as tk

class Statistiche:
    def __init__(self, gui):
        self.gui = gui
        self.gui.title("Statistiche")
        self.gui.state('zoomed')
        
        self.carica_dati()
        
#------------------------------------------------------------------------------------------#
    # Carica file JSON #

    def carica_dati(self):
        try:
            # Carica gli studenti #
            with open('studenti.json', 'r') as file:
                self.parole_totali = json.load(file)
            
        except Exception as e:
            self.gui.destroy()

def main():
    gui = tk.Tk()
    app = Statistiche(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()