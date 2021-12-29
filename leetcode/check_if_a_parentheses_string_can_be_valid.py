#Problem: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #total brackets which can be flipped
        total_unlocked = 0
        
        #total open and closed locked
        open_locked = 0
        close_locked = 0
        
        n = len(s)
        #if not even then definitely one of the brackets is extra
        if n % 2 == 1:
            return False
        
        for i in range(n-1,-1,-1):
            if locked[i] == '0':
                total_unlocked += 1
            elif s[i] == '(':
                open_locked += 1
            elif s[i] == ')':
                close_locked += 1
            
            #check if open_locked are more than close_locked + total_unlocked
            if total_unlocked - open_locked + close_locked < 0:
                return False
        
        total_unlocked = 0
        open_locked = 0
        close_locked = 0
        
        for i in range(n):
            if locked[i] == '0':
                total_unlocked += 1
            elif s[i] == '(':
                open_locked += 1
            elif s[i] == ')':
                close_locked += 1
        
            #check if close_locked are more than open_locked + total_unlocked
            if total_unlocked + open_locked - close_locked < 0:
                return False
        
        return True
            
            