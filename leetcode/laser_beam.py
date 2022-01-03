#Problem: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        n = len(bank)
        count_rows = [0] * n 
        col = len(bank[0])
        
        for i in range(n):
            for j in range(col):
                if bank[i][j] == '1':
                    count_rows[i] += 1
                    
        # print(count_rows)
        
        start_row = 0
        
        i = 1
        c = len(count_rows)
        res = 0
        while i < c:
            if count_rows[i] > 0:
                res += count_rows[start_row] * count_rows[i]
                start_row = i
            i += 1
        return res
                    