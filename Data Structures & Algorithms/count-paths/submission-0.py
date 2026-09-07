class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def findPath(row, column):
            key = f"{row}-{column}"
            if key in cache:
                return cache[key]

            if row >= m or column >= n:
                return 0

            if row == m - 1 and column == n - 1:
                return 1

            x = findPath(row + 1, column)
            y = findPath(row, column + 1)

            cache[key] = x + y
            return x + y

        
        return findPath(0, 0)