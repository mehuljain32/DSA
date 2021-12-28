#Problem: https://leetcode.com/problems/intervals-between-identical-elements/

from collections import defaultdict
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        pos_dict = defaultdict()
        res = [0] * len(arr)
        for index, value in enumerate(arr):
            if pos_dict.get(value):
                pos_dict[value].append(index)
            else:
                pos_dict[value] = [index]
        print(pos_dict)
        
        # for i in range(len(arr)):
        #     index_pos = pos_dict[arr[i]]
        #     ans = 0
        #     for j in index_pos:
        #         if i != j:
        #             ans += abs(i-j)
        #     res.append(ans)
        
        for i in pos_dict:
            index_pos = pos_dict[i]
            
            prefix_sum = [0] * (len(index_pos)+1)
            
            #calculate prefix sums
            
            for i in range(len(index_pos)):
                prefix_sum[i+1] = prefix_sum[i] + index_pos[i]
                
            for index,value in enumerate(index_pos):
                res[value] = (value * (index+1) - prefix_sum[index+1]) + ((prefix_sum[len(index_pos)] - prefix_sum[index]) - value * (len(index_pos) - index))
        return res
    
    #eg: index_pos = [2,5,6,7]
    #to find sum of abs diff less than for i = 2 or index_pos[2] = 6
    #6-1 + 6-5 + 6-6
    #or 6 * 3 - (1+5+6)
    #or 6 * (i+1) - prefix_sum[i+1]
    #likewise
    #prefix_sum[len(index_pos)] - prefix_sum[index] - value(6 in above eg)*(len(index_pos) - index)
    #gives sum of abs diff greater than curr value