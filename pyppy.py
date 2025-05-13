import tkinter as tk
from tkinter import ttk, messagebox
import random

class ExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Examples")
        self.root.geometry("600x400")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Basic widgets tab
        basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(basic_frame, text='Basic Widgets')

        # Label
        tk.Label(basic_frame, text="This is a Label").pack(pady=5)

        # Button
        tk.Button(basic_frame, text="Click Me!", command=self.show_message).pack(pady=5)

        # Entry
        self.entry = tk.Entry(basic_frame)
        self.entry.pack(pady=5)
        self.entry.insert(0, "Type here...")

        # Checkbutton
        self.check_var = tk.BooleanVar()
        tk.Checkbutton(basic_frame, text="Check me", variable=self.check_var).pack(pady=5)

        # Radio buttons
        self.radio_var = tk.StringVar(value="1")
        tk.Radiobutton(basic_frame, text="Option 1", variable=self.radio_var, value="1").pack()
        tk.Radiobutton(basic_frame, text="Option 2", variable=self.radio_var, value="2").pack()

        # Advanced widgets tab
        advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(advanced_frame, text='Advanced Widgets')

        # Combobox
        self.combo = ttk.Combobox(advanced_frame, values=["Option 1", "Option 2", "Option 3"])
        self.combo.pack(pady=5)
        self.combo.set("Select an option")

        # Listbox
        self.listbox = tk.Listbox(advanced_frame, height=4)
        self.listbox.pack(pady=5)
        for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
            self.listbox.insert(tk.END, item)

        # Scale
        tk.Scale(advanced_frame, from_=0, to=100, orient=tk.HORIZONTAL).pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(advanced_frame, length=200, mode='determinate')
        self.progress.pack(pady=5)
        self.progress['value'] = 70

        # Text widget
        self.text = tk.Text(advanced_frame, height=4, width=30)
        self.text.pack(pady=5)
        self.text.insert(tk.END, "This is a Text widget\nYou can write multiple lines here")

    def show_message(self):
        messagebox.showinfo("Message", "You clicked the button!")
        
    def button(self):
        self.button = tk.Button(self.root, text="Click Me", command=self.show_message)
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()
    
    class NumberGuessingGame:
        def __init__(self, root):
            self.root = root
            self.root.title("Guess the Number")
            self.root.geometry("400x300")
            
            self.min_number = 1
            self.max_number = 100
            self.secret_number = random.randint(self.min_number, self.max_number)
            self.attempts = 0
            
            # Create main frame
            main_frame = ttk.Frame(root, padding=20)
            main_frame.pack(expand=True, fill='both')
            
            # Title
            ttk.Label(main_frame, text="Guess the Number Game", font=("Arial", 16)).pack(pady=10)
            
            # Instructions
            ttk.Label(main_frame, text=f"I'm thinking of a number between {self.min_number} and {self.max_number}").pack(pady=5)
            
            # Guess input
            input_frame = ttk.Frame(main_frame)
            input_frame.pack(pady=10)
            
            ttk.Label(input_frame, text="Your guess:").grid(row=0, column=0, padx=5)
            self.guess_entry = ttk.Entry(input_frame, width=10)
            self.guess_entry.grid(row=0, column=1, padx=5)
            self.guess_entry.focus()
            
            # Submit button
            ttk.Button(main_frame, text="Submit Guess", command=self.check_guess).pack(pady=10)
            
            # Feedback label
            self.feedback = ttk.Label(main_frame, text="")
            self.feedback.pack(pady=5)
            
            # Attempts counter
            self.attempts_label = ttk.Label(main_frame, text="Attempts: 0")
            self.attempts_label.pack(pady=5)
            
            # New game button
            ttk.Button(main_frame, text="New Game", command=self.new_game).pack(pady=10)
            
            # Bind Enter key to submit
            self.guess_entry.bind("<Return>", lambda event: self.check_guess())
        
        def check_guess(self):
            try:
                guess = int(self.guess_entry.get())
                self.attempts += 1
                self.attempts_label.config(text=f"Attempts: {self.attempts}")
                
                if guess < self.min_number or guess > self.max_number:
                    self.feedback.config(text=f"Please enter a number between {self.min_number} and {self.max_number}")
                elif guess < self.secret_number:
                    self.feedback.config(text="Too low! Try a higher number.")
                elif guess > self.secret_number:
                    self.feedback.config(text="Too high! Try a lower number.")
                else:
                    messagebox.showinfo("Congratulations!", 
                                       f"You guessed it! The number was {self.secret_number}.\nIt took you {self.attempts} attempts.")
                    self.new_game()
            except ValueError:
                self.feedback.config(text="Please enter a valid number")
            finally:
                self.guess_entry.delete(0, tk.END)
                self.guess_entry.focus()
        
        def new_game(self):
            self.secret_number = random.randint(self.min_number, self.max_number)
            self.attempts = 0
            self.attempts_label.config(text="Attempts: 0")
            self.feedback.config(text="")
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.focus()

    if __name__ == "__main__":
        root = tk.Tk()
        app = NumberGuessingGame(root)
        root.mainloop()


        class MemoryGame:
            def __init__(self, root):
                self.root = root
                self.root.title("Memory Game")
                self.root.geometry("500x550")
                
                # Game variables
                self.size = 4  # 4x4 grid
                self.symbols = ["🍎", "🍌", "🍒", "🍓", "🍑", "🍇", "🍍", "🌮"] * 2
                self.cards = []
                self.flipped = []
                self.matched_pairs = 0
                self.moves = 0
                self.game_over = False
                
                # Create main frame
                self.main_frame = ttk.Frame(root, padding=20)
                self.main_frame.pack(expand=True, fill='both')
                
                # Title
                ttk.Label(self.main_frame, text="Memory Game", font=("Arial", 16)).pack(pady=10)
                
                # Info frame
                info_frame = ttk.Frame(self.main_frame)
                info_frame.pack(pady=10)
                
                self.moves_label = ttk.Label(info_frame, text="Moves: 0")
                self.moves_label.grid(row=0, column=0, padx=20)
                
                self.pairs_label = ttk.Label(info_frame, text="Pairs: 0/8")
                self.pairs_label.grid(row=0, column=1, padx=20)
                
                # Game grid
                self.game_frame = ttk.Frame(self.main_frame)
                self.game_frame.pack(pady=10)
                
                # New game button
                ttk.Button(self.main_frame, text="New Game", command=self.new_game).pack(pady=10)
                
                # Initialize game
                self.new_game()
            
            def new_game(self):
                # Clear existing cards
                for widget in self.game_frame.winfo_children():
                    widget.destroy()
                
                # Reset game variables
                self.matched_pairs = 0
                self.moves = 0
                self.flipped = []
                self.game_over = False
                self.cards = []
                
                # Update labels
                self.moves_label.config(text="Moves: 0")
                self.pairs_label.config(text="Pairs: 0/8")
                
                # Shuffle symbols
                random.shuffle(self.symbols)
                
                # Create cards
                for i in range(self.size):
                    for j in range(self.size):
                        idx = i * self.size + j
                        card = tk.Button(self.game_frame, text="", width=5, height=2, 
                                         font=("Arial", 16), command=lambda idx=idx: self.flip_card(idx))
                        card.grid(row=i, column=j, padx=5, pady=5)
                        self.cards.append(card)
            
            def flip_card(self, idx):
                # Ignore if game over or card already matched or already flipped
                if self.game_over or "disabled" in self.cards[idx].state() or idx in self.flipped:
                    return
                
                # Flip the card
                self.cards[idx].config(text=self.symbols[idx])
                
                # Add to flipped list
                self.flipped.append(idx)
                
                # If we flipped two cards
                if len(self.flipped) == 2:
                    self.moves += 1
                    self.moves_label.config(text=f"Moves: {self.moves}")
                    
                    # Check if they match
                    if self.symbols[self.flipped[0]] == self.symbols[self.flipped[1]]:
                        # Match found
                        self.matched_pairs += 1
                        self.pairs_label.config(text=f"Pairs: {self.matched_pairs}/8")
                        
                        # Disable matched cards
                        for idx in self.flipped:
                            self.cards[idx].config(state="disabled", relief="flat", bg="light green")
                        
                        self.flipped = []
                        
                        # Check if game is over
                        if self.matched_pairs == 8:
                            self.game_over = True
                            messagebox.showinfo("Congratulations!", 
                                               f"You've completed the game in {self.moves} moves!")
                    else:
                        # No match, flip back after a delay
                        self.root.after(1000, self.flip_back)
            
            def flip_back(self):
                # Flip cards back
                for idx in self.flipped:
                    self.cards[idx].config(text="")
                self.flipped = []

        if __name__ == "__main__":
            root = tk.Tk()
            app = MemoryGame(root)
            root.mainloop()
            
            
