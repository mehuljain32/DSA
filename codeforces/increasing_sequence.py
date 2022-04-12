import math
import sys
from collections import defaultdict, Counter
from bisect import bisect_left
# sys.setrecursionlimit(10**6)

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
    n,d = li()
    # n = arr[0]
    # d = arr[1]

    nums = li()

    res = 0

    for i in range(1,n):
        if nums[i] > nums[i-1]:
            continue
        else:
            inc = (nums[i-1] - nums[i])//d + 1
            res += inc
            nums[i] += inc * d 
    print(res)
# t = ii()
# for _ in range(t):
solve()