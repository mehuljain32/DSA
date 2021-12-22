t = int(input())

while t > 0:
  arr = list((input().split(" ")))
  ar = []
  for i in arr:
    ar.append(int(i))
  n = len(ar)
  res = []

  start = 0
  end = 2
  target = ar[-1]

  num1 = ar[-1] - ar[-2]
  num2 = ar[-1] - ar[-3]
  num3 = abs(num1+num2 - target)

  print(num1,end=" ")
  print(num2,end=" ")
  print(num3)
  
  # print(ar)
  t -= 1
