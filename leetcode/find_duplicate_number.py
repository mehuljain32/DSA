#Problem: https://leetcode.com/problems/find-the-duplicate-number/

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for num in nums:
#             cur = abs(num)
#             if nums[cur] < 0:
#                 duplicate = cur
#                 break
#             nums[cur] = -nums[cur]

#         # Restore numbers
#         for i in range(len(nums)):
#             nums[i] = abs(nums[i])

#         return duplicate


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         #Tortoise-hare algorithm
        
#         #find intersection of tortoise and hare
#         tortoise = hare = nums[0]
        
#         while True:
#             tortoise = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break
        
#         #hare is at intersection
#         #find entrance of the cycle
        
#         tortoise = nums[0]
        
#         #loop breaks when they meet at entrance if cycle aka duplicate element
#         while tortoise != hare:
#             tortoise = nums[tortoise]
#             hare = nums[hare]
        
#         return hare

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #binary search from solution
        
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            curr = (low + high) // 2
            count = 0
            
            #total num less than equal to curr
            count = sum(i <= curr for i in nums)
            
            if count > curr:
                dup = curr
                high = curr - 1
            else:
                low = curr + 1
        return dup