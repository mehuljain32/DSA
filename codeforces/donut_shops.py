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
  a,b,c = li()
  res = [-1] * 2

  # if a < c:
  #   res[0] = 1

  # if a > c:
  #   res[0] = -1

  print(1 if a < c else -1,end = " ")

  # if c >= a * b:
  #   res[1] = -1

  # if c < a * b:
  #   res[1] = b
  print(b if c < a * b else -1)

  # print(res[0],end=" ")
  # print(res[1])

  
t = ii()
for _ in range(t):
  solve()