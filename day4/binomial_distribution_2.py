# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator as op
from functools import reduce

## Used this code from: https://stackoverflow.com/a/4941932
def nCr(n,r):
  r = min(r, n-r)
  numer = reduce(op.mul, range(n, n-r, -1), 1)
  denom = reduce(op.mul, range(1, r+1), 1)
  return numer//denom

#start of the problem
p_r = 0.12
p_a = 0.88
n = 10

a_1 = 0.0
for i in range(0,3):
  a_1 += round(nCr(n,i)*(p_r**i)*(p_a**(n-i)), 4)

a_2 = 0.0
for i in range(2,11):
  a_2 += round(nCr(n,i)*(p_r**i)*(p_a**(n-i)), 4) 

print(round(a_1,3))
print(round(a_2,3))
