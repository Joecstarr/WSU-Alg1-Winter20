import numpy as np
cnt = 0
for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
      for l in range(0, 3):
        # |i j|
        # |k l|
        det = ((i*l)-(j*k))%3
        if det != 0:
          cnt += 1
          if cnt%5 == 0:
            print("\\text{det}\\lrp{\\begin{bmatrix}",i,"&",j,"\\\\",k,"&",l,"\\end{bmatrix}}=",det,"\\\\ \\hspace{.5in} \\\\")
          else:
            print("\\text{det}\\lrp{\\begin{bmatrix}",i,"&",j,"\\\\",k,"&",l,"\\end{bmatrix}}=",det,"&")

print(cnt)