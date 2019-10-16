#
#https://www.hackerrank.com/challenges/list-comprehensions/problem

x = 2
y = 2
z = 2
n = 2
list = []
for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      if i + j + k == n:
        continue
      list.append([i, j, k])

print(list)