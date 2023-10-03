from game import Game

class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.board = [[" " for x in range(3) for y in range(3)]]
        self.tokens = ["X", "O"]

    def getTurn(self):
        return self.tokens[self.turn % 2]
    
    def isGameOver(self):
        return self.gameOver
    
    def getInput(self):
        row, column = input("Enter row and column separated by a space: ").split()

        return (int(row), int(column))
    
    def step(self, move):
        row, column = move
        self.board[row][column] = self.tokens[self.turn % 2]

        # Manually check all possible wins
        if self.board[0][0] != " " and \
                self.board[0][0] == self.board[0][1] and \
                self.board[0][1] == self.board[0][2]:
            self.gameOver = True
        elif self.board[0][0] != " " and \
                self.board[0][0] == self.board[1][0] and \
                self.board[1][0] == self.board[2][0]:
            self.gameOver = True
        elif self.board[0][0] != " " and \
                self.board[0][0] == self.board[1][1] and \
                self.board[1][1] == self.board[2][2]:
            self.gameOver = True
        elif self.board[2][0] != " " and \
                self.board[2][0] == self.board[1][1] and \
                self.board[1][1] == self.board[0][2]:
            self.gameOver = True
        elif self.board[0][1] != " " and \
                self.board[0][1] == self.board[1][1] and \
                self.board[1][1] == self.board[2][1]:
            self.gameOver = True
        elif self.board[0][2] != " " and \
                self.board[0][2] == self.board[1][2] and \
                self.board[1][2] == self.board[2][2]:
            self.gameOver = True
        elif self.board[1][0] != " " and \
                self.board[1][0] == self.board[1][1] and \
                self.board[1][1] == self.board[1][2]:
            self.gameOver = True

        super().step()
    
    def __str__(self):
        return "\n-+-+-\n".join(["|".join(row) for row in self.board]) + "\n"
    
if __name__ == "__main__":
    game = TicTacToe()
    game.main()
        