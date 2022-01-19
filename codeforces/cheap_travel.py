#https://codeforces.com/problemset/problem/118/A
import math
import sys
from collections import defaultdict, Counter
def ii():
  # return int(input())
  return int(sys.stdin.readline())

def li():
  # return list(map(int,input().split()))
  return list(map(int, sys.stdin.readline().strip().split()))

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
  n,m,a,b = li()
  cost = 0

  if a <= b // m:
    cost = n * a
  else:
    #min done for remaining rides(n%m) after special tickets are selected
    cost = (n // m) * b + min((n%m) * a, b)
  
  print(cost)
  
# t = ii()
# for _ in range(t):
solve()