#codeforces

import math

def ii():
  return int(input())

def li():
  return list(map(int,input().split()))


def solve():
    n = ii()
    group = li()
    group.sort()
    # group_sum = sum(group)
    # ans = math.ceil(group_sum/4)
    ans = 0
    start = 0
    end = len(group) - 1
    
    while start < end:
        if group[start] + group[end] <= 4:
            group[end] += group[start]
            start += 1
        else:
            end -= 1
            ans += 1
    print(ans+1)
    return

# t = ii()
# for _ in range(t):
solve()