n = int(input())

while n > 0:
  arr  = list(input().split(" "))
  ar = []
  for i in arr:
    ar.append(int(i))
  x = ar[0] + ar[2]*10
  y = ar[1] + ar[3] * 10

  if x > y:
    print("Chefina")
  elif x < y:
    print("Chef")
  else:
    print("Draw")
  n -= 1





t = int(input())

while t > 0:
  n,k = input().split(" ")
  n = int(n)
  k = int(k)
  s = input()
  res = 0
  for i in range(0,len(s)-k+1,k):
    # print("i: ",i)
    count = 0
    for j in range(i,i+k):
      # print("s[i]: ",s[j])
      if s[j] == '0':
        count += 1
    # print("count: ", count)
    if count == k:
      res += 1
  print(res)
  t -= 1
