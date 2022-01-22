import math
import sys
from collections import defaultdict, Counter
def ii():
  # return int(input())
  return int(sys.stdin.readline())

def li():
  # return list(map(int,input().split()))
  return list(map(int, sys.stdin.readline().split()))

def si():
    # return input()
    return sys.stdin.readline().strip()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat

def ti():
  return tuple(int(i) for i in li())

def solve():
  n  = ii()
  res = 0

  if n % 2 > 0:
    print(res)
    return
  while n > 1:
    res += 1
    n = n // 2
    if n % 2 == 1:
      break
  print(res)


t = ii()
for _ in range(t):
  solve()