#Problem: https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            #calculate euclidean distance between point and origin
            return point[0] ** 2 + point[1] ** 2
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(points)):
            dist = -distance(points[i])
            
            if len(heap) == k:
                heapq.heappushpop(heap,(dist, points[i][0], points[i][1]))
            else:
                heapq.heappush(heap, (dist, points[i][0], points[i][1]))
        return [(x,y) for (dist,x,y) in heap]


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         def distance(point):
#             #calculate euclidean distance between point and origin
#             return point[0] ** 2 + point[1] ** 2
        
#         points.sort(key=distance)
        
#         return points[:k]