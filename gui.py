import tkinter as tk

gui = tk.Tk()
gui.title("Pack Example")

codeInsert = ""

def button_function(buttonArgument):
    if(buttonArgument != "Confirm" and buttonArgument != "Delete"):
        if(len(codeInsert) == 4):
            print("Code is full")
        else:
            global codeInsert
            codeInsert += str(buttonArgument)
    else:
        if(buttonArgument == "Confirm"):
            print("Confirm")
            print(codeInsert)
            codeInsert = ""
        else:
            print("Delete")
            codeInsert = ""
    

button0 = tk.Button(gui, text="0", width=10, height=2, command=lambda: button_function(0))
button1 = tk.Button(gui, text="1", width=10, height=2, command=lambda: button_function(1))
button2 = tk.Button(gui, text="2", width=10, height=2, command=lambda: button_function(2))
button3 = tk.Button(gui, text="3", width=10, height=2, command=lambda: button_function(3))
button4 = tk.Button(gui, text="4", width=10, height=2, command=lambda: button_function(4))
button5 = tk.Button(gui, text="5", width=10, height=2, command=lambda: button_function(5))
button6 = tk.Button(gui, text="6", width=10, height=2, command=lambda: button_function(6))
button7 = tk.Button(gui, text="7", width=10, height=2, command=lambda: button_function(7))
button8 = tk.Button(gui, text="8", width=10, height=2, command=lambda: button_function(8))
button9 = tk.Button(gui, text="9", width=10, height=2, command=lambda: button_function(9))

buttonA = tk.Button(gui, text="A", width=10, height=2, command=lambda: button_function('A'))
buttonB = tk.Button(gui, text="B", width=10, height=2, command=lambda: button_function('B'))
buttonC = tk.Button(gui, text="C", width=10, height=2, command=lambda: button_function('C'))

buttonConfirm = tk.Button(gui, text="C", width=10, height=2, command=lambda: button_function('Confirm'))
buttonDelete = tk.Button(gui, text="D", width=10, height=2, command=lambda: button_function('Delete'))

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
buttonC.grid(row=3, column=2)
buttonConfirm.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonDelete.grid(row=4, column=2)

gui.mainloop()
