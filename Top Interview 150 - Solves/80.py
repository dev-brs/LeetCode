#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        
        while i < len(nums):
            if nums[i] == nums[i-1] == nums[i-2]:
                nums.pop(i-2)
            else:
                i += 1

        return len(nums)