import math
import sys
def ii():
  return int(input())

def li():
  return list(map(int,input().split()))

def si():
    return input()


def solve():
  n = ii()
  res = [0] * n
  
  for i in range(n):
    res[i] = i+1

  if n % 2 == 0:
    for i in range(0,n,2):
      res[i], res[i+1] = res[i+1], res[i]
  else:
    for i in range(0,n-1,2):
      res[i],res[i+1] = res[i+1],res[i]

    res[n-2], res[n-1] = res[n-1], res[n-2]
  for i in res:
    print(i,end=" ")
  print()
t = ii()
for _ in range(t):
  solve()