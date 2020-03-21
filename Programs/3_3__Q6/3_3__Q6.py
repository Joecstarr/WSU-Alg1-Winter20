import numpy as np
cnt = 0
start = np.array([[2, 1], [0, 2]])
a = start
while np.array_equal(a, np.array([[1, 0], [0, 1]])) == False:
    a = np.matmul(start, a)
    # |(0,0) (0,1)|==|i j|
    # |(1,0) (1,1)|==|k l|
    i = a.item((0, 0)) % 3
    k = a.item((1, 0)) % 3
    j = a.item((0, 1)) % 3
    l = a.item((1, 1)) % 3
    a = np.array([[i, j], [k, l]])
    cnt += 1
    if cnt%4 == 0:
      print("a^{",cnt+1,"}=\\lrp{\\begin{bmatrix}", i, "&", j, "\\\\", k,
          "&", l, "\\end{bmatrix}}\\\\ \\hspace{.5in} \\\\")
    else:
      print("a^{",cnt+1,"}=\\lrp{\\begin{bmatrix}", i, "&", j, "\\\\", k,
          "&", l, "\\end{bmatrix}}&")
    if cnt > 48:
        break
