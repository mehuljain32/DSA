#https://codeforces.com/problemset/problem/118/A
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
  n = ii()
  x, y, z = 0,0,0
  while n:
    for i,j,k in [ti()]:
      x += i
      y += j
      z += k
    n -= 1
  if x == 0 and y == 0 and z == 0:
    print("YES")
  else:
    print("NO")
# t = ii()
# for _ in range(t):
solve()