class Solution:
    def romanToInt(self, s: str) -> int:
        t=0
        r={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
         if i<len(s)-1 and r[s[i]]<r[s[i+1]]:
          t-=r[s[i]]
         else:
          t+=r[s[i]]
        return t  