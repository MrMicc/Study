from typing import List


class Sudoku:

    def __init__(self, board: List[List[str]] = [["1", "2", "3"], ["3", "1", "2"], ["2", "3", "1"]], squares: int = 3):
        self.rows = [set() for i in range(len(board))]
        self.cols = [set() for i in range(len(board))]
        self.square = [[set() for i in range(squares)] for y in range(squares)]
        self.board = board

    def is_valid(self) -> bool:
        for row in range(len(self.rows)):
            for col in range(len(self.cols)):
                cell_value = self.board[row][col]
                if cell_value == ".":
                    continue
                if int(cell_value) not in range(1, 10) or cell_value in self.rows[row] or cell_value in self.cols[col] or cell_value in self.square[row // len(self.square)][col // len(self.square)]:
                    return False
                self.rows[row].add(cell_value)
                self.cols[col].add(cell_value)
                self.square[row // len(self.square)][col //
                                                     len(self.square)].add(cell_value)
        return True
