#https://leetcode.com/problems/two-sum/submissions/1200197364/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i, num in enumerate(nums):
            if hasher.get(target - num) is not None:
                return [hasher[target - num], i]
            hasher[num] = i
                    