t = int(input())

while t > 0:
  n = int(input())
  arr = [i for i in input().split(" ")]

  res = ""
  l = len(arr)
  
  start = 0
  res = []
  res.append(arr[0][0])
  while start < l-1:
    if arr[start][1] == arr[start+1][0]:
      res.append(arr[start][1])
    else:
      res.append(arr[start][1])
      res.append(arr[start+1][0])
    start += 1
  res.append(arr[-1][-1])

  if len(res) != n:
    res.append(arr[-1][-1])
  print("".join(res))
  t -= 1

#I/P:
#4
#7
#ab bb ba aa ba
#7
#ab ba aa ab ba
#3
#aa
#5
#bb ab bb

