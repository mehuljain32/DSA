import math

def ii():
  return int(input())

def li():
  return list(map(int,input().split()))


def solve():
    n = ii()
    arr = li()

    arr.sort()
    print(sum(arr) - arr[0])
    return
  
  
t = ii()
for _ in range(t):
  solve()