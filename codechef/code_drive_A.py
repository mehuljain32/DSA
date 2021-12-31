import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()

def solve():
  arr = li()
  a = arr[0]
  b = arr[1]
  c = arr[2]
  d= arr[3]

  if a < b:
    a += c

    if a < b:
      a += d
    else:
      b += d
  else:

    b += c

    if b < a:
      b += d
    else:
      a += d
  print('N' if a >= b else 'S')
t = ii()
for _ in range(t):
  solve()