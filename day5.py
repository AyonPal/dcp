"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
column, or diagonal.
"""


class Board:
    def __init__(self, n):
        self.N = n
        self.board = [[0 for i in range(n)] for j in range(n)]

    def printBoard(self):
        [print(i) for i in self.board]

    def putQueen(self, i, j):
        self.board[i][j] = 1

    def removeQueen(self, i):
        for j in range(self.N):
            self.board[i][j] = 0

    # qid represent row
    def checkThreat(self, qid, col):
        y = 0
        while(y < self.N):
            if(self.board[y][col] == 1):
                return True
            y += 1
        x = qid
        y = col
        while(x >= 0 and y >= 0):
            if(self.board[x][y] == 1):
                return True
            x -= 1
            y -= 1
        x = qid
        y = col
        while (x >= 0 and y < self.N):
            if(self.board[x][y] == 1):
                return True
            x -= 1
            y += 1

    def solve(self, i=0, count=0):
        if i == self.N:
            return count+1

        for j in range(self.N):
            if not self.checkThreat(i, j):
                self.putQueen(i, j)
                count += self.solve(i + 1)
                self.removeQueen(i)
        return count


if (__name__ == "__main__"):
    for i in range(10):
        board = Board(i)
        print(f'{i} = {board.solve()}')
