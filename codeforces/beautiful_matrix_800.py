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
  mat = mi(5,5)
  
  loc = []

  for i in range(5):
    for j in range(5):
      if mat[i][j] == 1:
        loc.append(i+1)
        loc.append(j+1)
        break
  # print(loc)
  res = abs(loc[0] - 3) + abs(loc[1] - 3)
  print(res)

# t = ii()
# for _ in range(t):
solve()