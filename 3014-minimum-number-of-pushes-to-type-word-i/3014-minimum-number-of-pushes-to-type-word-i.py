class Solution:
    def minimumPushes(self, word: str) -> int:
        t=0
        for i in range(len(word)):
            pushes=i//8+1
            t+=pushes
        return t