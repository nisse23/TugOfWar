import tkinter as tk
from tkinter import messagebox
import random
import pyrow


class TugOfWarGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tug of War Game")

        self.player_position = 3
        self.opponent_position = 3

        self.canvas = tk.Canvas(self.master, width=300, height=100, bg="white")
        self.canvas.pack()

        self.display_tug_of_war()

        self.button_quit = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.button_quit.pack(side=tk.LEFT, padx=10)

        # Periodically check whether the canvas should be updated
        self.master.after(100, self.update_game)

    def display_tug_of_war(self):
        if (
            hasattr(self, "canvas") and self.canvas.winfo_exists()
        ):  # Check if the canvas still exists
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 300, 100, fill="white")
            self.canvas.create_text(
                150,
                50,
                text="Opponent [{}-{}-{}-{}-{}-{}] Player".format(
                    "|" * self.opponent_position,
                    "<",
                    ">",
                    "|" * (5 - self.opponent_position),
                    "<",
                    ">",
                    "|" * self.player_position,
                ),
                font=("Arial", 10, "bold"),
            )

    def tug_left(self):
        self.player_position -= 1
        self.opponent_move()
        self.check_winner()

    def tug_right(self):
        self.player_position += 1
        self.opponent_move()
        self.check_winner()

    def opponent_move(self):
        opponent_move = random.choice([-1, 1])
        self.opponent_position += opponent_move

    def check_winner(self):
        if self.player_position <= 0 or self.opponent_position >= 6:
            self.display_tug_of_war()
            messagebox.showinfo("Tug of War", "Congratulations! You won!")
            self.master.destroy()
        elif self.opponent_position <= 0 or self.player_position >= 6:
            self.display_tug_of_war()
            messagebox.showinfo("Tug of War", "Oh no! You lost. Better luck next time.")
            self.master.destroy()

    def quit_game(self):
        self.master.destroy()

    def update_game(self):
        # Periodically check whether the canvas should be updated
        self.display_tug_of_war()

        pyrow.pyrow.find()
        ergs = pyrow.pyrow(erg)
        # get input from the rowing machine
        data = pyrow.pyrow.get_monitor(forceplot=False)
        if data[power] > 100:
            self.tug_left()
        else:
            self.tug_right()
        if not (
            self.player_position <= 0
            or self.opponent_position >= 6
            or self.opponent_position <= 0
            or self.player_position >= 6
        ):
            self.master.after(100, self.update_game)


if __name__ == "__main__":
    root = tk.Tk()
    game = TugOfWarGame(root)
    root.mainloop()
