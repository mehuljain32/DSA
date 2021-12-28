# Problem:  https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        #prefix sums array
        freq = [0] * k
        freq[0] = 1
        
        sum_till_now = 0
        
        for i in nums:
            sum_till_now += i
            
            rem = sum_till_now % k
            
            # if rem < 0:
            #     rem += k
            count += freq[rem]
            freq[rem] += 1
        
                    
        return count