#https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                
        return slow + 1