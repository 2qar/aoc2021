import functools
import sys

class Board:
    def __init__(self, board_str):
        self.marked = {}
        board = board_str.split('\n')
        for i in range(len(board)):
            board[i] = [int(x) for x in board[i].strip().split()]
            for x in board[i]:
                self.marked[x] = False
        self.board = board

    def mark(self, x):
        if x in self.marked:
            self.marked[x] = True
    
    def _row_has_bingo(self, row):
        return functools.reduce(lambda x, y: x and y, map(lambda x: self.marked[x], row))

    def has_bingo(self):
        columns = []
        for row in range(len(self.board)):
            columns.append([])
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                columns[j].append(self.board[i][j])

        i = 0
        bingo = False
        while i < len(self.board) and not bingo:
            bingo = self._row_has_bingo(self.board[i]) or self._row_has_bingo(columns[i])
            i += 1
        return bingo
    
    def score(self):
        return sum(filter(lambda x: not self.marked[x], self.marked.keys()))

    def reset(self):
        for key in self.marked.keys():
            self.marked[key] = False

boards = open("input").read()[0:-1].split("\n\n")
nums = [int(x) for x in boards[0].split(",")]
boards = [Board(board_str) for board_str in boards[1:]]

# Part 1
found_winner = False
i = 0
while i < len(nums) and not found_winner:
    j = 0
    while j < len(boards) and not found_winner:
        boards[j].mark(nums[i])
        if boards[j].has_bingo():
            print(nums[i] * boards[j].score())
            found_winner = True
        j += 1
    i += 1

for board in boards:
    board.reset()

# Part 2
playing = len(boards)
has_bingo = [False] * len(boards)
last_winner_score = 0
i = 0
while i < len(nums) and playing != 0:
    j = 0
    while j < len(boards) and playing != 0:
        boards[j].mark(nums[i])
        if boards[j].has_bingo() and not has_bingo[j]:
            has_bingo[j] = True
            playing -= 1
            if playing == 0:
                last_winner_score = nums[i] * boards[j].score()
        j += 1
    i += 1
print(last_winner_score)
