可以有重复元素
```py
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l < r:
            # print("{},{}".format(l,r))
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            while l<=mid and nums[l] == nums[mid]:
                l+=1
            while mid < r and nums[r] == nums[mid]:
                r-=1
            if nums[l] < nums[mid]:# 前半段有序
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
                continue
            elif nums[r] > nums[mid]:# 后半段有序
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return nums[l] == target
```