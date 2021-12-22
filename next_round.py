#codeforces

import math

def ii():
  return int(input())

def li():
  return list(map(int,input().split()))


def solve():
    ar = list(map(int,input().split()))
    n = ar[0]
    k = ar[1]

    scores = list(map(int,input().split()))

    target = scores[k-1]
    count = 0
    for i in range(n):
        if scores[i] > 0 and scores[i] >= target:
            # print("scores: ", scores[i])
            count += 1
        else:
            break  
    print(count)
    return

# t = ii()
# for _ in range(t):
solve()