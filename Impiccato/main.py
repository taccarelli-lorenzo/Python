import tkinter as tk
from Impiccato import Impiccato 

def main():
    gui = tk.Tk()
    app = Impiccato(gui)  
    gui.mainloop()      

if __name__ == "__main__":
    main()