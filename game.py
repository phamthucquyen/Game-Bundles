from abc import ABC, abstractmethod

class Game(ABC):
    
    def __init__(self):
        self.turn = 0
        self.gameOver = False

    def isGameOver(self):
        return self.gameOver
    
    @abstractmethod
    def step(self):
        if not self.gameOver:
            self.turn += 1

    def getTurn(self):
        return self.tokens[self.turn % len(self.tokens)]

    @abstractmethod
    def getInput(self):
        pass

    def main(self):
        while not self.isGameOver():
            print(self)

            self.step(self.getInput())

        print("\nGame Over!\n")
        print(self)
    
    def reset(self):
        type(self).__init__(self)