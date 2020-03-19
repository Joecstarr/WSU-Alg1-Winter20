K=[1,4,10,13,16,19]
H = [1, 8]
G = set([1])
for x in H:
  for y in K:
    print(x, y, (x * y) % 21)
    G.add((x * y) % 21)
print(G)