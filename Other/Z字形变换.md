简单的数学规律
```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        x = 2 * numRows - 2
        l = len(s)
        for i in range(numRows):
            n = 0
            while n*x + i < l:
                ans += s[n*x + i]
                if i > 0 and i < numRows-1:
                    if n*x + numRows-1 + (numRows-i-1) < l:
                         ans += s[n*x + numRows-1 + (numRows-i-1)]
                n += 1
        return ans
```