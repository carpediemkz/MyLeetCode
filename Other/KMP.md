KMP 算法需要理解 and 记忆

```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(needle):
            next = [0 for _ in range(len(needle))]
            j = 0
            next[0] = j
            for i in range(1, len(needle)):
                while j > 0 and needle[j]!=needle[i]:
                    j = next[j-1]
                if needle[j] == needle[i]:
                    j += 1
                next[i] = j
            return next
        
        if not needle:
            return 0

        next = getNext(needle)

        j = 0
        for i in range(len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = next[j-1]
            if needle[j] == haystack[i]:
                j+= 1
            if j == len(needle):
                return i - j + 1
        return -1
```