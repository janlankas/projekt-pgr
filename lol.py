import random

class MineSweeper:
    def __init__(self, rows, cols, mines):
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.mines = mines
        self.rows = rows
        self.cols = cols
        self.mine_locations = []
        self.generate_mines()
        self.generate_numbers()

    def generate_mines(self):
        while len(self.mine_locations) < self.mines:
            mine_location = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            if mine_location not in self.mine_locations:
                self.mine_locations.append(mine_location)
                row, col = mine_location
                self.board[row][col] = -1

    def generate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= row + i < self.rows) and (0 <= col + j < self.cols):
                            if self.board[row + i][col + j] == -1:
                                count += 1
                self.board[row][col] = count

    def play(self):
        while True:
            self.print_board()
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if self.board[row][col] == -1:
                print("BOOM! Game Over!")
                break
            else:
                print("Safe!")
    def print_board(self):
        for row in self.board:
            print(row)

game = MineSweeper(10, 10, 10)
game.play()
