给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。


```py
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k-=1
            stack.append(ch)
        
        start = 0
        while start < len(stack) and stack[start] == '0':
            start += 1
        stack = stack[start:]
        if k > 0:
            stack = stack[:-k]
        return "".join(stack) or "0"
```