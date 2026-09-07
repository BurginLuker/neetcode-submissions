class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def findPath(i, j):
            key = f"{i}-{j}"
            if key in cache:
                return cache[key]

            if i >= len(text1) or j >= len(text2):
                return 0

            ways = 0

            if text1[i] == text2[j]:
                ways = 1 + findPath(i + 1, j + 1)
            else:
                ways = max(findPath(i + 1, j), findPath(i, j + 1))

            cache[key] = ways
            return ways



        return findPath(0, 0)
    