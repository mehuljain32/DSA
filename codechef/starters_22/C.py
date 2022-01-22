import math
import sys
from collections import defaultdict, Counter
from bisect import bisect_left
sys.setrecursionlimit(10**6)

def ii():
  # return int(input())
  return int(sys.stdin.readline())

def li():
  # return list(map(int,input().split()))
  return list(map(int, sys.stdin.readline().split()))

def si():
    # return input()
    return sys.stdin.readline().strip()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat

def ti():
  return tuple(int(i) for i in li())

def lengthOfLIS(nums) -> int:
  n = len(nums)

  subSeq = []

  for i in nums:
      if len(subSeq) == 0 or i > subSeq[-1]:
          subSeq.append(i)
      else:
          #index of smallest number greater than i
          index = bisect_left(subSeq, i)
          #replace the number at index in current subsequence with i
          subSeq[index] = i
              
  return len(subSeq)

def permute(curr,start,nums, res):
  if len(nums) == 0:
    # if len(curr) == orig:
    if lengthOfLIS(curr) == lengthOfLIS(curr[::-1]):
      # print("YES")
      # print(*curr)
      res.append(curr)
      # return("YES")
      return
    # else:
      # print("NO")
      # return("NO")

  else:
    for i in range(len(nums)):
      temp = curr + [nums[i]]
      # print("temp: ",temp)
      # print(temp)
      # if permute(temp,i+1, nums[:i] + nums[i+1:], res) == "YES":
        # return "YES"
      # else:
        # return "NO"
      permute(temp,i+1, nums[:i] + nums[i+1:], res)


def solve():
  n = ii()

  if n == 2:
    print("NO")
    return

  if n % 2 != 0:
    print('YES')
    for i in range(1,n//2+1):
      print(i, end=" ")
    print(n,end = " ")
    for i in range(n-1,n//2,-1):
      print(i, end = " ")
    print()
  else:
    print("YES")
    print(n // 2, end = " ")

    for i in range(1, n // 2):
      print(i, end = " ")

    for i in range(n, n // 2, -1):
      print(i, end = " ")

    print()



t = ii()
for _ in range(t):
  solve()