class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = [0] * 26
        for c in s1:
            x[ord(c) - ord('a')] += 1

        y = [0] * 26
        for r in range(len(s2)):
            y[ord(s2[r]) - ord('a')] += 1

            if r >= len(s1):
                y[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if x == y:
                return True

        return False