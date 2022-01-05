#Problem: https://leetcode.com/problems/largest-number/


from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x,y):
            if x+y > y+x:
                return 1
            elif x+y == y + x:
                return 0
            else:
                return -1
        
        n = len(nums)
        
        nums = [str(i) for i in nums]
        
        #sort in desc order, key given to sort based on str generated after concat
        #eg without key, '3' < '30' and we'll get '303' but we want '330'
        nums.sort(key=cmp_to_key(compare), reverse = True)        
        
        # print(nums)
        return '0' if nums[0] == '0' else ''.join(nums)