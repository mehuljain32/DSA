import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def solve():
  n = ii()
  res = 0
  if n < 3:
    print(0)
    return

  if n == 3:
    print(10)
    return
  else:
    res = (3 ** (n-3)) * (2 ** 3)*(n-2)

    res += res // 4
  
    print(res)



t = ii()
for _ in range(t):
  solve()