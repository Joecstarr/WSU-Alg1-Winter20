import numpy as np

def getModArray3b3(mulres,mod):
  # |(0,0) (0,1) (0,2)|==|i j z|
  # |(1,0) (1,1) (1,2)|==|k l y|
  # |(2,0) (2,1) (2,2)|==|v w x|
  i = mulres.item((0, 0)) % mod
  j = mulres.item((0, 1)) % mod
  z = mulres.item((0, 2)) % mod

  k = mulres.item((1, 0)) % mod
  l = mulres.item((1, 1)) % mod
  y = mulres.item((1, 2)) % mod

  v = mulres.item((2, 0)) % mod
  w = mulres.item((2, 1)) % mod
  x = mulres.item((2, 2)) % mod
  return np.array([[i, j, z], [k, l, y], [v, w, x]])
  
def texStrArray3b3(mulres,mod):
  # |(0,0) (0,1) (0,2)|==|i j z|
  # |(1,0) (1,1) (1,2)|==|k l y|
  # |(2,0) (2,1) (2,2)|==|v w x|
  i = mulres.item((0, 0)) % mod
  j = mulres.item((0, 1)) % mod
  z = mulres.item((0, 2)) % mod

  k = mulres.item((1, 0)) % mod
  l = mulres.item((1, 1)) % mod
  y = mulres.item((1, 2)) % mod

  v = mulres.item((2, 0)) % mod
  w = mulres.item((2, 1)) % mod
  x = mulres.item((2, 2)) % mod
  return "\\begin{bmatrix}" + str(i)+ "&"+ str(j)+ "&"+ str(z)+ "\\\\" + str(k)+ "&"+ str(l)+ "&"+ str(y)+ "\\\\" + str(v)+ "&"+ str(w)+ "&"+ str(x)+ "\\end{bmatrix}"

ident = np.array([[1, 0,0], [0, 1,0], [0, 0,1]])
for a in range(0, 3):
  for b in range(0, 3):
    for c in range(0, 3):
      start = np.array([[1, 0, 0], [a, 1, 0], [b, c, 1]])
      print("$$a=",texStrArray3b3(start,2),"\\\\")
      mulres = start
      cnt = 0
      while np.array_equal(mulres,ident) == False:
          mulres = getModArray3b3(np.matmul(start, mulres),2)
          cnt += 1
          print("a^{",cnt+1,"}=\\lrp{",texStrArray3b3(mulres,2),"}")
          if cnt > 48:
              break
      print("$$")


