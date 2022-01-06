# https://www.codechef.com/START21C
# contest link
import math
import sys
def ii():
  # return int(input())
  return int(sys.stdin.readline())

def li():
  # return list(map(int,input().split()))
  return list(map(int, sys.stdin.readline().split()))

def si():
    # return input()
    return sys.stdin.readline()

def mi(row,col):
  mat = []

  for i in range(row):
    arr = li()
    mat.append(arr)
  return mat

def getUniquePrimeCount(num):
  count = 0
  i = 2
  while i * i <= num:
    if num % i == 0:
      count += 1
      while num % i == 0:
        num //= i
    i += 1

  if num != 1:  #incase num is a prime number
    count += 1
  return count

def solve():
  #prime factorisation problem
  arr = li()
  n = arr[0]  #width
  m = arr[1]  #height

  primes = getUniquePrimeCount(m)
  res = 0

  for i in range(primes,0,-1):
    if n % i == 0:
      res = i
      break
  print(res)



t = ii()
for _ in range(t):
  solve()