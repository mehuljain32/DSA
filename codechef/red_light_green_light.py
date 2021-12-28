import math

def ii():
  return int(input())

def li():
  return list(map(int,input().split()))


def solve():
    input_ar = li()
    n = input_ar[0]
    k = input_ar[1]
    arr = li()

    res = 0

    for i in arr:
        if i > k:
            res += 1
    print(res)
    return

    
  
  
t = ii()
for _ in range(t):
  solve()