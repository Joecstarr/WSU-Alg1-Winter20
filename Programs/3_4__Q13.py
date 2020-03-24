
import numpy as np

def findgen(list, val):
  for m in list:
    i = list[m].item((0, 0)) 
    k = list[m].item((1, 0)) 
    j = list[m].item((0, 1)) 
    l = list[m].item((1, 1))
    vi = val.item((0, 0))
    vk = val.item((1, 0))
    vj = val.item((0, 1))
    vl = val.item((1, 1))
    if i == vi:
      if j == vj:
        if k == vk:
          if l == vl:
            return m


I = np.array([[1, 0], [0, 1]])
A = np.array([[1, 0], [1, 1]])
B = np.array([[1, 0], [1, 2]])
C = np.array([[1, 0], [0, 2]])
D = np.array([[1, 0], [2, 1]])
E = np.array([[1, 0], [2, 2]])
arrys = {"I":I ,"A":A ,"B":B ,"C":C ,"D":D ,"E":E }
cnt = 0
for f in arrys:
  for s in arrys:
    mult = arrys[f].dot(arrys[s])
    i = mult.item((0, 0)) % 3
    k = mult.item((1, 0)) % 3
    j = mult.item((0, 1)) % 3
    l = mult.item((1, 1)) % 3
    mult = np.array([[i, j], [k, l]])
    cnt += 1
    if cnt%4 == 0:
      print(f,"\\times",s,"=",findgen(arrys, mult),"\\\\ \\hspace{.5in} \\\\")
    else:
      print(f,"\\times",s,"=",findgen(arrys, mult),"&")