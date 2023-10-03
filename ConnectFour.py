from game import Game
class ConnectFour(Game):
    def __init__(self):
        super().__init__()
        self.board = [[' 'for x in range(7)] for y in range(6)]
        self.tokens = ["R", "Y"]

    def getTurn(self):
        # Returns the token of the current turn
        return self.tokens[self.turn % len(self.tokens)]

    def step(self, column):
       
        # Obtain the row it ended up
        row = self.placeToken(column, self.tokens[self.turn % len(self.tokens)])

        # Only perform move if possible
        if row != -1:
            # Check for winning move
            self.gameOver = self.winningMove(column, row)

            super().step()

    def winningMove(self, column, row):
        return self.checkHorizontal(column, row) or \
               self.checkVertical(column, row) or \
               self.checkDiagonals(column, row)

    def checkHorizontal(self, column, row):
        # Check left and right
        tokenCount = 0
        for i in range(column, len(self.board[row])):
            if self.board[row][column] == self.board[row][i]:
                tokenCount += 1
            else:
                break

        if tokenCount < 4:
            for i in range(column - 1, -1, -1):
                if self.board[row][column] == self.board[row][i]:
                    tokenCount += 1
                else:
                    break

        return tokenCount >= 4
    
    def checkVertical(self, column, row):
    # Check down from position until we go off board or hit a color that is not ours
        tokenCount = 0
        for i in range(row, len(self.board)):
            if self.board[row][column] == self.board[i][column]:
                tokenCount += 1
            else:
                break
        return tokenCount >= 4
    
    def checkDiagonals(self, column, row):
        return self.genericDiagonalCheck(column, row, 1, 1) or \
               self.genericDiagonalCheck(column, row, -1, 1)
    
    def genericDiagonalCheck(self, column, row, colMod, rowMod):
        tokenCount = 0
        r, c = row, column
        while r < len(self.board) and c < len(self.board[row]) and r >= 0 and c >= 0:
            if self.board[r][c] == self.board[row][column]:
                tokenCount += 1
                r += rowMod
                c += colMod
            else:
                break

        if tokenCount < 4:
            r, c = row - rowMod, column - colMod
            while r < len(self.board) and c < len(self.board[row]) and r >= 0 and c >= 0:
                if self.board[r][c] == self.board[row][column]:
                    tokenCount += 1
                    r -= rowMod
                    c -= colMod
                else:
                    break
        return tokenCount >= 4
    
    def getInput(self):
        user_input = input("Enter the column for turn " + self.getTurn() + ": ")

        if user_input.isdigit():
            value = int(user_input)
            if value < 0 or value > 6:
                print("Value is out of range. Try again!")
                return self.getInput()
            else:
                return value
        else:
            print("Incorrect input. Try again!")
            return self.getInput()
        
    def placeToken(self, column, token):
        # place a token in column move for turn
        # start at bottom and work way up

        row = len(self.board) - 1

        while(self.board[row][column] != ' '):
            row -= 1

        # Can’t place any more tokens in this column
            if row < 0:
                return -1
            
        self.board[row][column] = token
        return row
    
    def __str__(self):
        display = "\n".join(["| " + " | ".join(x) + " |" for x in self.board])
        display += "\n"
        display += "-----" * len(self.board) + "\n"
        display += " " + " ".join([" " + str(x) + " " for x in range(len(self.board[0]))]) + "\n"

        return display
    
def main():
    game = ConnectFour()
    game.main()
    game.reset()
    game.main()

if __name__ == '__main__':
    main()
