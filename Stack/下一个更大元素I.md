给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

```py
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        l = len(nums2)
        stack = []
        for i in range(l-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                hmap[nums2[i]] = stack[-1]
            else:
                hmap[nums2[i]] = -1
            stack.append(nums2[i])
        return [hmap[x] for x in nums1]
```