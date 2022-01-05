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
  x = arr[1]
  y = arr[2]

  xc =  yc = (n+1) // 2
  count = 0

  if (abs(x-xc) + abs(y-yc)) % 2 == 1:
    count = 1
     
  elif (abs(x-xc) + abs(y-yc)) % 2 == 0:
    count = 0
  
  print(count) 
t = ii()
for _ in range(t):
  solve()