import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")


n = int(input())
a = [0,0,0]
b = [0,0,0]
c = [0,0,0]
tot1 = 0
tot2 = 0
tot3 = 0
x = ()
a[0] = 1
b[1] = 1
c[2] = 1
for j in range(0,n):
  x = input()
  
  a[int(x[0]) - 1], a[int(x[2]) - 1] = a[int(x[2]) - 1], a[int(x[0]) - 1]
  if (int(x[4]) - 1) == a.index(max(a)):
    tot1 += 1

  
  b[int(x[0]) - 1], b[int(x[2]) - 1] = b[int(x[2]) - 1], b[int(x[0]) - 1]
  if (int(x[4]) - 1) == b.index(max(b)):
    tot2 += 1
  
  
  c[int(x[0]) - 1], c[int(x[2]) - 1] = c[int(x[2]) - 1], c[int(x[0]) - 1]
  if (int(x[4]) - 1) == c.index(max(c)):
    tot3 += 1

print(max(tot1, tot2, tot3))


