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
  t = arr[1]

  q = si()
  l = []
  #convert string to list character wise
  l[:0] = q

  while t:
    swap = []
    for i in range(1,n):
      if l[i] == 'G' and l[i-1] == 'B' and (i-1) not in swap:
        l[i-1],l[i] = l[i],l[i-1]
        swap.append(i)
    t -= 1
  print(''.join(l))

# t = ii()
# for _ in range(t):
solve()