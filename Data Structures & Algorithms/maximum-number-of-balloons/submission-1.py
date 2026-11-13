class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        og = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        m = {}
        for c in text:
            curr = m.get(c) or 0
            m[c] = curr + 1

        count = 0
        while True:
            for c, v in og.items():
                n = m.get(c) or 0
                if n - v < 0:
                    return count
                m[c] = n - v
            count += 1

        return count
