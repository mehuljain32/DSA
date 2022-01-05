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
  # arr = sys.stdin.readline().split(" ")
  arr = li()

  left = arr[0] - arr[1]

  print('YES' if left >= sum(arr[2:]) else 'NO')
    
t = ii()
for _ in range(t):
  solve()