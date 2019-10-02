# https://www.hackerrank.com/challenges/designer-door-mat/problem
# atleast 6 lines of code
# A single line containing the space separated values of N and M. 
m = '13 39'
n = int(m.split()[0])
for i in range(n//2):
  print(str('.|.'*(2*i+1)).center(n*3,'-'))
print(str('WELCOME').center(n*3,'-'))
for i in range(n//2):
  print(str('.|.'*(2*((n//2)-i)-1)).center(n*3,'-'))