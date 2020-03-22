
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
  
for i in range(3, 50):
  ans = relpri(i)
  if len(ans)==4:
    print(i)
    print("\t", seive(i))
    print("\t",ans)
    print("\t",len(ans))
