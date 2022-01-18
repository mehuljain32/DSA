#https://codeforces.com/problemset/problem/118/A
import math
import sys
from collections import defaultdict, Counter
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

def solve():
  s = si()
  vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
  #ord('a') - ord('A') = 32
  stack = []

  for i in s:
    if i in vowels:
      continue
    else:
      stack.append('.')
      if ord(i) <= 90:
        stack.append(chr(ord(i) + 32))
      else:
        stack.append(i)
  print(''.join(stack))
# t = ii()
# for _ in range(t):
solve()