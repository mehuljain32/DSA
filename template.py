import math
import sys
from collections import defaultdict, Counter
from bisect import bisect_left
sys.setrecursionlimit(10**6)

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

def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a % b)

def solve():



t = ii()
for _ in range(t):
  solve()