#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, '', 1)
            else:
                return False
        return True
