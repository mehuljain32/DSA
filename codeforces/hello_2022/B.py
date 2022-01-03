import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat


def solve():
  n = ii()
  seg = []
  for i in range(n):
    seg.append(li())
  curr_min = 0
  curr_max = 0
  curr_min_cost = 0
  res = []
  # for curr in range(len(seg)):
  #   if len(res) > 0:
  #     if seg[curr][0] > curr_min and seg[curr][1] > curr_max:
  #       res.append(curr_min_cost + seg[curr][2])
  #       curr_min = min(curr_min, seg[curr][0])
  #       curr_max = max(curr_max, seg[curr][1])
  #       curr_min_cost = min(curr_min_cost,seg[curr][2])

  #     elif seg[curr][1] > curr_max:
  #       res.append(seg[curr][2])
  #       curr_min = min(curr_min, seg[curr][0])
  #       curr_max = max(curr_max, seg[curr][1])
  #       curr_min_cost = min(curr_min_cost,seg[curr][2])
  #     elif seg[curr][0] <= curr_min and seg[curr][1] <= curr_max:
  #       res.append(res[-1])
  #     else:
  #       res.append(seg[curr][2] + curr_min_cost)
  #       curr_min = min(curr_min, seg[curr][0])
  #       curr_max = max(curr_max, seg[curr][1])
        curr_min_cost = min(curr_min_cost,seg[curr][2])
      #   if seg[curr][0] > seg[curr-1][0] and seg[curr][1] > seg[curr-1][1]:
      #     res.append(seg[curr][2] + seg[curr-1][2])
      #     curr_min = min(seg[curr][0], seg[curr-1][0])
      #     curr_max = max(seg[curr][1], seg[curr-1][1])
      #     curr_min_cost = min(seg[curr][2],seg[curr-1][2])
      # else:  
    else:
      res.append(seg[curr][2])
      curr_min = seg[curr][0]
      curr_max = seg[curr][1]
      curr_min_cost = seg[curr][2]
  for i in res:
    print(i)
  

t = ii()
for _ in range(t):
  solve()