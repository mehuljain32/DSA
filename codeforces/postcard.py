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


def solve():
  s = si()
  k = ii()

  n = len(s)

  c = s.count('?')
  sf = s.count('*')

  req = n - c - sf

  res = "Impossible"
  #hw?ap*yn?eww*ye*ar
  
  if req == k:
    res = []
    for i in s:
      if i not in "?*":
        res.append(i)

  elif req < k:
    rem = k - req
    if sf:
      res = []
      for i in range(n):
        if s[i] == '?':
          continue
        elif s[i] == '*' and rem:
          res.append(s[i-1] * rem)
          rem = 0
        else:
          res.append(s[i])
  else:
    rem = req - k

    if rem <= c + sf:
      res = []
      for i in range(n):
        if s[i] in '?*':
          if rem:
            res.pop()
            rem -= 1
        else:
          res.append(s[i])

  print(''.join(res))

# t = ii()
# for _ in range(t):
solve()