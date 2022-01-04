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
  n = ii()

  max_int = 9999999999

  min_left = max_int
  cost_min_left = max_int

  max_right = 0
  cost_max_right = max_int

  max_len = 0
  cost_len = max_int

  for i in range(n):

    arr = sys.stdin.readline().split(" ")

    l = int(arr[0])
    r = int(arr[1])
    curr_cost = int(arr[2])

    if l < min_left:
      min_left = l
      cost_min_left = max_int

    if l == min_left:
      cost_min_left = min(cost_min_left, curr_cost)

    if max_right < r:
      max_right = r
      cost_max_right = max_int

    if max_right == r:
      cost_max_right = min(cost_max_right, curr_cost)

    if max_len < (r-l+1):
      max_len = r-l+1
      cost_len = max_int

    if max_len == (r-l+1):
      cost_len = min(cost_len, curr_cost)

    res = cost_min_left + cost_max_right

    if max_len == (max_right - min_left + 1):
      res = min(res, cost_len)
    print(res)
t = ii()
for _ in range(t):
  solve()