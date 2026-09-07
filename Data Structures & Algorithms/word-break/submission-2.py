class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}

        def isWord(i):
            if i in cache:
                return cache[i]

            if i == len(s):
                return True
            
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    reachedEnd = isWord(i + len(w))
                    if reachedEnd:
                        cache[i] = True
                        return True

            cache[i] = False
            return False

        l = isWord(0)
        return l