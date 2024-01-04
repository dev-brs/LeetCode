#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        msg = ''
        for x in s:
            if x.isalnum():
                msg+=x.lower()
        p1 = 0
        p2 = len(msg)-1
        print(msg)
        while p1 < p2:
            if msg[p1] != msg[p2]:return False
            p1+=1
            p2-=1
        return True
