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


def solve():
  n = ii()
  a = li()

  b = []
  
  start = 0
  end = n-1
  a.sort()
  # b.append(a[0] & a[1])
  # max_so_far = b[0]
  # if n < 3:
  #   print(b[0])
  #   return
  max_el = 0
  min_el = 999999
  max_so_far = 0

  # while start <= end:
  #   max_el = max(max_el,a[end] & a[end-1])
  #   print("max: ", max_el)
  #   min_el = min(min_el,a[start] & a[start + 1])
  #   print("min: ", min_el)
  #   max_so_far = max(max_so_far, max_el | min_el)
  #   print("max so far: ", max_so_far)
  #   start += 1
  #   end -= 1
  p = 1
  for i in range(32):
    # for j in range(i+1,n):
    #   # b.append(a[i] & a[j])
    #   # if len(b) > 1:
    #   #   max_el = b[-1]
    #   #   min_el = b[0]
    #   #   new_el = max_el | min_el
    #   #   b.pop(-1)
    #   #   b.pop(0)
    #   #   b.append(new_el)
    #   curr = a[i] & a[j]

    #   min_el = min(min_el, curr)
    #   max_el = max(max_el, curr)

    #   max_so_far = max(max_so_far, min_el | max_el)

    #   min_el = max_el
    #   max_el = max_so_far
    # curr = a[i] & a[i-1]
    # max_so_far = max(max_so_far, max_so_far | curr)
    count = 0

    for j in range(n):
      if a[j] % 2 == 1:
        count += 1
      a[j] //= 2

    if count > 1:
      max_so_far += p
    p *= 2
  print(max_so_far)
t = ii()
for _ in range(t):
  solve()