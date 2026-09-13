class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []

        for i in range(n + 1):
            count = 0

            for j in range(32):
                if (1 << j) & i:
                    count += 1

            out.append(count)

        return out