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

  n = arr[0]
  m = arr[1]

  count = 0

  for i in range(0,n,2):
    for j in range(0,m,2):
      count += 1
  print(count)
    
t = ii()
for _ in range(t):
  solve()