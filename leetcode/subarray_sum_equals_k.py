#Problem:   https://leetcode.com/problems/subarray-sum-equals-k/solution/

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#         n = len(nums)
#         count = 0
        
#         prefixSum = [0] * (n+1)
#         prefixSum[0] = 0
        
#         for i in range(1,n+1):
#             prefixSum[i] = prefixSum[i-1] + nums[i-1]
        
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 if prefixSum[j] - prefixSum[i] == k:
#                     count += 1
        
#         return count
        
        #TC: n^2
        #SC: constant
#         count = 0
#         n = len(nums)
    
#         for i in range(n):
#             sum_now = 0
#             for j in range(i,n):
#                 sum_now += nums[j]
#                 if sum_now == k:
#                     count += 1
#         return count
        count = 0
        n = len(nums)
        sum_now = 0
        freqDict = defaultdict()
        freqDict[0] = 1
        # print(freqDict.get(-4))
        for i in range(n):
            sum_now += nums[i]
            if freqDict.get(sum_now-k):
                count += freqDict[sum_now-k]
            if not freqDict.get(sum_now):
                freqDict[sum_now] = 1
            else:
                freqDict[sum_now] += 1
        return count