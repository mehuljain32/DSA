import math
import sys
def ii():
  # return int(input())
  return int(sys.stdin.readline())

def li():
  # return list(map(int,input().split()))
  return list(map(int, sys.stdin.readline().split()))

def si():
    # return input()
    return sys.stdin.readline()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat


def solve():
  n = ii()
  a = li()

  count = [0] * 32
  res = 0

  for i in range(n):
    num = a[i]
    for i in range(32):
      if num & (1 << i):
        count[i] += 1

  for i in range(32):
    if count[i] > 1:
      res |= (1 << i) #multiply 1 with 2^i and bitwise or with ans

  print(res)
t = ii()
for _ in range(t):
  solve()