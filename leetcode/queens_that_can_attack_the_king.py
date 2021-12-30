#Problem: https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        
        queen = {(x,y) for x,y in queens}
        print(queen)
        # res.append(queens[i])
        
        #trace in row and col from position of king
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in range(1,8):
                    x = king[0] + i * k
                    y = king[1] + j * k
                    
                    if (x,y) in queen:
                        res.append([x,y])
                        break
        return res

        
        
                
        