class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findWord(row, col, i):
            if i > len(word) - 1:
                return True

            if row < 0 or row > len(board) - 1:
                return False

            if col > len(board[0]) - 1 or col < 0:
                return False

            if board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            up = findWord(row - 1, col, i + 1)
            down = findWord(row + 1, col, i + 1)
            left = findWord(row, col - 1, i + 1)
            right = findWord(row, col + 1, i + 1)

            board[row][col] = temp

            return up or down or left or right

            


        for i in range(len(board)):
            for j in range(len(board[0])):
                if findWord(i, j, 0):
                    return True

        return False