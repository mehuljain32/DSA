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
  div = set()
  # min_d = 9999999999
  # for i in range(2,n+1):
  #   if n % i == 0:
  #     div.append(i)





  for i in [2,3,5,7]:
    if n % i == 0:
      div.add(i)
    else:
      if type(math.sqrt(n)) == int:
        div.add(math.sqrt(n))

  # print(div)
  min_d = 9999999
  count = 0
  for i in div:
    if n % i == 0:
      curr = count_divisors(n // i)
      if curr > count:
        count = curr
        min_d = i
  print(min_d if len(div) > 1 else list(div)[0])

def count_divisors(n):
  res = set()

  for i in range(2,n+1):
    if n % i == 0:
      res.add(i)
  return len(res)



t = ii()
for _ in range(t):
  solve()