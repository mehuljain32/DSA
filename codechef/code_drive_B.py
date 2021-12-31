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
  s = si()
  flag = False
  
  code = []

  i = 0
  
  # for i in range(len(s)-4):
  #   if s[i:i+4] == 'code':
  #     code.append(i)
  # i = 0
  # res = []
  # while i < len(s)-3:
  #   if s[i:i+4] == 'chef':
  #     if len(code) > 0 and code[-1] < i:
  #       flag = True
  #       code.pop()
  #     else:
  #       flag = False
  #     res.append(flag)
  #   i += 1

  # for i in res:
  #   if not i:
  #     print('WA')
  #     return
  # print('AC')
  n = len(s)
  for i in range(n):
    if s[i:i+4] == 'code':
      print('AC')
      return
    elif s[i:i+4] == 'chef':
      print('WA')
      return
    else:
      continue
t = ii()
for _ in range(t):
  solve()