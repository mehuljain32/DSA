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
  input_ar = li()
  n = input_ar[0]
  r = input_ar[1]
  res = [['.' for i in range(n)] for j in range(n)]
  # print(res)
  row = []
  col = []
  for i in range(0,n,2):
    if r == 0:
      break
    for j in range(0,n,2):
      if i in row or j in col:
        continue
      else:
        res[i][j] = 'R'
        row.append(i)
        col.append(j)
        r -= 1
        break
  # print(res)
  if r == 0:
    for i in res:
      for j in i:
        print(j,end="")
      print()
  else:
    print(-1)
  
  

t = ii()
for _ in range(t):
  solve()