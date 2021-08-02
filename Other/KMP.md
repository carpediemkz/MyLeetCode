KMP 算法需要理解 and 记忆

```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(needle):
            next = [0 for _ in range(len(needle))]
            j = 0
            # 长度为 1 的字符串没有真前缀、真后缀
            # aaaxaaaa
            # j = 3
            # next[6] = 3
            next[0] = j
            for i in range(1, len(needle)):
                # j 是上轮匹配的长度，所以前有长度为 j 的已匹配真前缀、前后缀
                while j > 0 and needle[j]!=needle[i]:
                    j = next[j-1]
                # 继续可以匹配的逻辑
                if needle[j] == needle[i]:
                    j += 1
                next[i] = j
            return next
        
        if not needle:
            return 0

        # next 数组含义: next[i] 字符串 neddle[0:i+1] 真前缀 == 真后缀 的最大长度
        next = getNext(needle)

        j = 0
        for i in range(len(haystack)):
            # j 是上轮匹配的长度，所以前有长度为 j 的已匹配真前缀、前后缀
            while j > 0 and needle[j] != haystack[i]:
                j = next[j-1]
            # 继续可以匹配的逻辑
            # i, j 分别为真前缀、真后缀的下一个字母
            # 若匹配 j 自增 1 即可
            if needle[j] == haystack[i]:
                j+= 1
            if j == len(needle):
                return i - j + 1
        return -1
```