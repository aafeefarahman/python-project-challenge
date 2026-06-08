import tkinter as tk
from tkinter import messagebox
import random

WORDS = {
    "Tech": ["python", "algorithm", "database", "developer", "network", "computer"],
    "Movies": ["avatar", "inception", "interstellar", "gladiator", "titanic"],
    "Animals": ["elephant", "tiger", "giraffe", "penguin", "dolphin"],
    "Countries": ["india", "canada", "japan", "germany", "france"]
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Pro")
        self.root.geometry("900x700")

        self.score = 0
        self.max_wrong = 6
        self.hint_used = False

        self.category_var = tk.StringVar(value="Tech")

        top = tk.Frame(root)
        top.pack(pady=10)

        tk.Label(top, text="HANGMAN PRO", font=("Arial", 22, "bold")).pack()

        tk.OptionMenu(top, self.category_var, *WORDS.keys()).pack(pady=5)

        self.score_label = tk.Label(top, text="Score: 0", font=("Arial", 12))
        self.score_label.pack()

        self.word_label = tk.Label(root, text="", font=("Courier", 28, "bold"))
        self.word_label.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Hint", command=self.use_hint).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Restart", command=self.start_game).grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack(pady=10)

        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.pack()

        self.start_game()

    def start_game(self):
        self.word = random.choice(WORDS[self.category_var.get()]).upper()
        self.guessed = set()
        self.wrong = 0
        self.hint_used = False

        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i, letter in enumerate(letters):
            btn = tk.Button(
                self.keyboard_frame,
                text=letter,
                width=4,
                command=lambda l=letter: self.guess(l)
            )
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)

        self.canvas.delete("all")
        self.draw_gallows()
        self.update_word()

    def update_word(self):
        display = " ".join(
            l if l in self.guessed else "_"
            for l in self.word
        )
        self.word_label.config(text=display)

    def guess(self, letter):
        self.guessed.add(letter)

        if letter in self.word:
            self.score += 10
        else:
            self.score -= 5
            self.wrong += 1
            self.draw_hangman()

        self.score_label.config(text=f"Score: {self.score}")
        self.update_word()

        if all(l in self.guessed for l in self.word):
            self.score += 50
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Winner", f"You won!\nWord: {self.word}")
            self.start_game()

        if self.wrong >= self.max_wrong:
            messagebox.showerror("Game Over", f"The word was {self.word}")
            self.start_game()

    def use_hint(self):
        if self.hint_used:
            return

        hidden = [l for l in self.word if l not in self.guessed]

        if hidden:
            reveal = random.choice(hidden)
            self.guessed.add(reveal)
            self.score -= 15
            self.score_label.config(text=f"Score: {self.score}")
            self.update_word()
            self.hint_used = True

    def draw_gallows(self):
        self.canvas.create_line(50, 250, 200, 250)
        self.canvas.create_line(100, 250, 100, 50)
        self.canvas.create_line(100, 50, 180, 50)
        self.canvas.create_line(180, 50, 180, 80)

    def draw_hangman(self):
        parts = [
            lambda: self.canvas.create_oval(160, 80, 200, 120),
            lambda: self.canvas.create_line(180, 120, 180, 180),
            lambda: self.canvas.create_line(180, 140, 150, 160),
            lambda: self.canvas.create_line(180, 140, 210, 160),
            lambda: self.canvas.create_line(180, 180, 160, 220),
            lambda: self.canvas.create_line(180, 180, 200, 220),
        ]

        if 1 <= self.wrong <= len(parts):
            parts[self.wrong - 1]()

root = tk.Tk()
app = HangmanGame(root)
root.mainloop()
