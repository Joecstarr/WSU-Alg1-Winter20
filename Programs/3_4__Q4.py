
def seive(M):
  list = [*range(2, M)]
  for i in range(2, M):
    if i in list:
      cnt = 2
      while (i*cnt) < M:
        if (i*cnt) in list:
          list.remove(i * cnt)
        cnt += 1
  return list

def relpri(M):
  list = [*range(1, M)]
  for i in seive(M):
    if M % i==0:
      cnt = 1
      while (i*cnt) < M:
        if (i*cnt) in list:
          list.remove(i * cnt)
        cnt += 1
  return list

def findgen(list, M):
  out = []
  for i in list:
    itout = []
    cnt = 1
    pwr = pow(i, cnt, M)
    while pwr != 1:
      cnt += 1
      itout.append(pwr)
      pwr = pow(i, cnt, M)
    itout.append(pwr)
    out.append(itout)
  return out
  
  
for i in range(3, 50):
  ans = relpri(i)  
  print("------------------------------------------------------------------------------------------------------------------------------------------------------")
  print(i)
  print("\tPrimes less than: ", seive(i))
  print("\tZ_i^x: ", ans)
  orders = findgen(ans, i)
  for ords in orders:
    print("\t<",ords[0],">: ", ords)
  print("\t|Z_i^x|: ",len(ans))
