import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master):
        self.master = master
        master.title("Minesweeper")
        self.flagged_cells = []
        # Create a grid of buttons
        self.buttons = []
        for i in range(10):
            row = []
            for j in range(10):
                button = tk.Button(master, text=" ", width=2, height=1, state='normal')
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Add mines to the grid
        self.mines = []
        for i in range(10):
            mine_row = []
            for j in range(10):
                mine = random.choice([True, False])
                mine_row.append(mine)
            self.mines.append(mine_row)

        # Add functionality to the buttons
        for i in range(10):
            for j in range(10):
                self.buttons[i][j].config(command=lambda row=i, col=j: self.reveal(row, col))
                self.buttons[i][j].bind("<Button-3>", lambda event, row=i, col=j: self.add_remove_flag(event, row, col))

    def reveal(self, row, col):
        if (row, col) in self.flagged_cells:
            return
        if self.mines[row][col]:
            self.gameover()
            self.buttons[row][col].config(text="X")
        else:
            count = 0
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if self.mines[i][j]:
                            count += 1
            self.buttons[row][col].config(text=str(count))

    def gameover(self):
        for i in range(10):
            for j in range(10):
                if self.mines[i][j]:
                    self.buttons[i][j].config(text="X")
                self.buttons[i][j].config(state='disable')
        tk.messagebox.showinfo("Game Over", "You clicked on a bomb! Try again.")

    def add_remove_flag(self, event, row, col):
        if (row, col) in self.flagged_cells:
            self.flagged_cells.remove((row, col))
            self.buttons[row][col].config(text=" ")
        else:
            self.flagged_cells.append((row, col))
            self.buttons[row][col].config(text="F")

root = tk.Tk()
my_game = Minesweeper(root)
root.mainloop()
