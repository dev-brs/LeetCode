#https://leetcode.com/problems/permutations/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        if(len(nums) == 1):
            return [nums[:]]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                
            answer.extend(perms)
            nums.append(n)
            
        return answer