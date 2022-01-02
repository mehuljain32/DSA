import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat


def solve():
  arr = li()
  n = arr[0]
  a = arr[1]
  b = arr[2]
  res = ""
  for i in range(n):
    # if i < a:
    res += chr(ord('a') + i % b)
    # else:
    #   res += res[i-a]
  print(res) 

t = ii()
for _ in range(t):
  solve()