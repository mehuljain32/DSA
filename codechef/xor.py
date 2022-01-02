import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def solve():
  arr = li()
  n = arr[0]
  k = arr[1]
  s = li()

  res = 0

  for i in range(n):
    f = (i+1) * (n-i)

    if f % 2 == 1:
      res ^= s[i:i+k]
  print(res)



t = ii()
for _ in range(t):
  solve()