
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

def findgen(list,M):
  for i in list:
    out = []
    cnt = 1
    pwr = pow(i, cnt, M)
    while pwr != 1:
      cnt += 1
      out.append(pwr)
      pwr = pow(i, cnt, M)
    if cnt == len(list):
      out.append(pwr)
      return out
  return 0
  
for i in range(3, 50):
  ans = relpri(i)  
  print("------------------------------------------------------------------------------------------------------------------------------------------------------")
  print(i)
  print("\tPrimes less than: ", seive(i))
  print("\tZ_i^x: ", ans)
  print("\t<Z_i^x>: ", findgen(ans,i))
  print("\t|Z_i^x|: ",len(ans))
