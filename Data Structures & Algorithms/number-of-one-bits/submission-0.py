class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(32): # int has indices for bits 0-31
            if (1 << i) & n:
                out += 1
        return out
