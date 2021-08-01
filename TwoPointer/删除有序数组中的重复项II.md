给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        pt = 0
        cur = 0
        count = 1
        last = 1000000
        while cur < l:
            if count < 2 or nums[cur] != last:
                if nums[cur] != last:
                    last = nums[cur]
                    count = 0
                count+=1
                nums[pt] = nums[cur]
                pt+=1             
            cur+=1
        return pt
```