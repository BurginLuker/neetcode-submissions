class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = Counter(s)
        for c in t:
            c1[c] -= 1

        return all(i == 0 for i in c1.values())

