import math

def ii():
  return int(input())

def li():
  return list(map(int,input().split()))


def solve():
  n = ii()
  ar = li()
  # ar = []
  # print(ar)
  
  # n = len(ar)
  res = True
  gcd = ar[0]

  for i in range(2,n,2):
    gcd = math.gcd(gcd,ar[i])
  # print("even gcd: ", even_gcd)
  for i in range(1,n,2):
    if ar[i] % gcd == 0:
      res = False
      break
  
  if res:
    print(gcd)
    return
  
  gcd = ar[1]

  for i in range(2,n):
    if i % 2 == 1:
      gcd = math.gcd(gcd,ar[i])
  res = True

  for i in range(0,n,2):
    if ar[i] % gcd == 0:
      res = False
      break
  if res:
    print(gcd)
  else:
    print(0)
t = ii()
for _ in range(t):
  solve()